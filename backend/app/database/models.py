
import json
from sqlalchemy import Column, Integer, String, DateTime, Text
from datetime import datetime
from .database import Base

class DataAnalysisHistory(Base):
    __tablename__ = "data_analysis_history"

    id = Column(Integer, primary_key=True, index=True)
    filename = Column(String, index=True)
    result = Column(String)
    data = Column(Text)
    created_at = Column(DateTime, default=datetime.utcnow)

    def to_dict(self):
        return {
            "id": self.id,
            "filename": self.filename,
            "result": self.result,
            "data": json.loads(self.data),
            "created_at": self.created_at.strftime("%Y-%m-%d %H:%M:%S")
        }

