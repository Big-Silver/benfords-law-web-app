import json
import os
from fastapi import (
    APIRouter,
    Depends,
    File,
    HTTPException,
    UploadFile,
)
from sqlalchemy.orm import Session
from database.models import DataAnalysisHistory
from fastapi.responses import JSONResponse, FileResponse
from utils import allowed_file, generate_random_filename
import database.database as database
from services import validations as validations_service
from services import generate_graph

router = APIRouter()
db = database.get_db
router = APIRouter(tags=["Validations"])

def validate_and_save_csv(file):
    if not file:
        raise HTTPException(status_code=400, detail="No file uploaded")

    if not allowed_file(file.filename):
        raise HTTPException(status_code=400, detail="Invalid file format. Please upload a valid text or CSV file.")

    # Generate a random filename to avoid conflicts
    filename = generate_random_filename() + ".csv"
    system_file_path = os.path.join("uploads", filename)

    try:
        with open(system_file_path, "wb") as f:
            f.write(file.file.read())
    
    except Exception as e:
        print(e)
        return JSONResponse(content="Unable to read file", status_code=500)

    return filename, system_file_path


@router.post("/validate-dataset/json")
async def validate_benfrods_law(file: UploadFile = File(
        ..., description="Upload a file numerical data column"
    ), db: Session = Depends(db)):

    try:
        filename, system_file_path = validate_and_save_csv(file)
    except Exception as e:
        return JSONResponse(content=e, status_code=500)
    
    try:
        data_analysis, _ = validations_service.validate_benfrods_law_service(db, filename, system_file_path)

        return JSONResponse(content={
                "message": data_analysis.result,
                "data": json.dumps(data_analysis.to_dict()),
            }, status_code=201)

    
    except Exception as e:
        print("backend/app/routers/validations.py:64", e)
        return JSONResponse(content="Unable to validate file", status_code=500)
    

@router.post("/validate-dataset/visualize", response_class=FileResponse)
async def validate_benfrods_law(
    file: UploadFile = File(
        ..., description="Upload a file numerical data column"
    ), 
    db: Session = Depends(db),
):
    try:
        filename, system_file_path = validate_and_save_csv(file)
    except Exception as e:
        return JSONResponse(content=e, status_code=500)
    
    try:
        data_analysis, data  = validations_service.validate_benfrods_law_service(db, filename, system_file_path)
        image_path = generate_graph.generate_bar_chart(data.to_dict(), data_analysis.id)
        image =  FileResponse(image_path)

        return image
    
    except Exception as e:
        print("backend/app/routers/validations.py:85", e)
        return JSONResponse(content="Unable to validate file", status_code=500)

@router.get("/validate-dataset/{analysis_id}/json")
async def visualize_validation_analysis(
    analysis_id: int, 
    session: Session = Depends(db)
):
    try:
        data_analysis = validations_service.get_validation_analysis(session, analysis_id)

        # Generate the graph

        return JSONResponse(content={
                "message": data_analysis.result,
                "data": json.dumps(data_analysis.to_dict()),
            }, status_code=201)
    
    except Exception as e:
        print("backend/app/routers/validations.py:10", e)
        return JSONResponse(content="Issues with ", status_code=500)


@router.get("/validate-dataset/{analysis_id}/visualize", response_class=FileResponse)
async def visualize_validation_analysis(
    analysis_id: int, 
    session: Session = Depends(db)
):
    try:
        data_analysis = validations_service.get_validation_analysis(session, analysis_id)

        # Generate the graph
        image_path = generate_graph.generate_bar_chart(json.loads(data_analysis.data), analysis_id)
        image =  FileResponse(image_path)

        return image
    except Exception as e:
        print("backend/app/routers/validations.py:10", e)
        return JSONResponse(content="Unable to generate graph", status_code=500)

@router.get("/validate-dataset/history/")
async def history(db: Session = Depends(db)):
    data_analysis_list = db.query(DataAnalysisHistory).all()
    return data_analysis_list