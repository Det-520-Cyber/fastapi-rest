from fastapi import FastAPI
from app.routes import router

app = FastAPI()

# Include the API router
app.include_router(router)

# Run the app:
# $ uvicorn app.main:app --reload
