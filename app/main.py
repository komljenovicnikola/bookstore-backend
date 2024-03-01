from fastapi import FastAPI

from app.api.api_routes import api_router

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Bookstore App", version='0.0.1')

app.include_router(api_router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
