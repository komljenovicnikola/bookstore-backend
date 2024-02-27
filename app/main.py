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

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='0.0.0.0', port=8082, timeout_keep_alive=10)