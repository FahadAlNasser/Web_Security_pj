from fastapi import FastAPI
from app.api import scanner_path

app = FastAPI(title = "This is partially automated file/link scanner")

app.include_router(scanner_path.routing)