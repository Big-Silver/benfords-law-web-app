from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import random
import string

app = FastAPI()

# Enable CORS
origins = ["*"]
app.add_middleware(CORSMiddleware, allow_origins=origins)


# Check if a file has a valid extension
def allowed_file(filename: str):
    allowed_extensions = {'txt', 'csv'}
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in allowed_extensions

# Function to generate a random filename
def generate_random_filename():
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for _ in range(10))
