from fastapi import FastAPI

from app.api.support import router as support_router


app = FastAPI(
    title="AI Customer Support Assistant",
    description="AI-powered customer support API",
    version="1.0.0",
)


app.include_router(support_router, prefix="/support")


@app.get("/")
def home():
    return {"message": "AI Customer Support Assistant API is running!"}


@app.get("/health")
def health_check():
    return {"status": "healthy"}
