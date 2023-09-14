import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import database.models as models
from database.database import engine
from routers import validations

# Define the directory path
static_directory = 'static'
upload_directory = 'upload'

# Create the directory if it doesn't exist
if not os.path.exists(static_directory):
    os.makedirs(static_directory)

if not os.path.exists(upload_directory):
    os.makedirs(upload_directory)

# Enable CORS
origins = ["*"]
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

models.Base.metadata.create_all(engine)

app.include_router(validations.router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)