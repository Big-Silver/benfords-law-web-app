import json
from fastapi import HTTPException
from sqlalchemy.orm import Session
from database.models import DataAnalysisHistory
import database.database as database


import pandas as pd

def apply_benfords_law(file_path):
    try:
        data = pd.read_csv(file_path, sep="\t")
        numerical_columns = data.select_dtypes(include=['int', 'float']).columns

        if (numerical_columns.size == 0):
            return 'No numerical columns found', None

        numerical_column_data = data[numerical_columns[0]]

        leading_digit_counts = numerical_column_data.astype(str).str[0].value_counts(normalize=True)

        for digit in range(1, 10):
            if str(digit) not in leading_digit_counts.index:
                leading_digit_counts[str(digit)] = 0

        leading_digit_counts = leading_digit_counts.sort_index()

        # Check if the proportion of '1' as the leading digit is about 30%
        observed_proportion_1 = leading_digit_counts.get('1', 0)
        is_valid = abs(observed_proportion_1 - 0.301) < 0.02  # Allowing a 2% tolerance

        if is_valid:
            return 'Validation successful', leading_digit_counts
        else:
            return 'Validation failed: Data does not conform to Benford\'s Law', leading_digit_counts

    except Exception as e:
        return f'Validation failed: {str(e)}', None


def validate_benfrods_law_service(session: Session, filename, system_file_path):
    try:
        result, data = apply_benfords_law(system_file_path)
        serialized_data = json.dumps(data.to_dict())
        data_analysis = DataAnalysisHistory(filename=filename, result=result, data=serialized_data)

        session.add(data_analysis)
        session.commit()

        return data_analysis, data
    except Exception as e:
        session.rollback()
        raise HTTPException(status_code=500, detail=f"Validation failed: {str(e)}")
    
def validate_benfrods_law_service(session: Session, filename, system_file_path):
    try:
        result, data = apply_benfords_law(system_file_path)
        serialized_data = json.dumps(data.to_dict())
        data_analysis = DataAnalysisHistory(filename=filename, result=result, data=serialized_data)

        session.add(data_analysis)
        session.commit()

        return data_analysis, data
    except Exception as e:
        session.rollback()
        raise HTTPException(status_code=500, detail=f"Validation failed: {str(e)}")
    
def get_validation_analysis(session: Session, analysis_id):
    try:
        data_analysis = session.query(DataAnalysisHistory).filter_by(id=analysis_id).first()
        
        if not data_analysis:
            raise HTTPException(status_code=404, detail="Analysis not found")

        return data_analysis

    except Exception as e:
        session.rollback()
        raise HTTPException(status_code=500, detail=f"Validation failed: {str(e)}")
    

async def get_data_analysis_history(session: Session):
    data_analysis_list = session.query(DataAnalysisHistory).all()
    return data_analysis_list