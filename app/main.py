from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
import logging
from app.database import engine, Base
from app.routes import address

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Address Book API",
    version="1.0.0",
    description="A simple address book API with CRUD and distance search functionality."
)

app.include_router(address.router)

@app.get("/", summary="Root Endpoint", tags=["Health Check"])
def read_root():
    """Root endpoint to verify API is running."""
    logger.info("Root endpoint accessed.")
    return {"message": "Hello World"}

# Handle validation errors
@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    logger.error(f"Validation error: {exc.errors()}")
    return JSONResponse(
        status_code=422,
        content={"error": "Validation failed", "details": exc.errors()}
    )

# Handle generic server errors
@app.exception_handler(Exception)
async def generic_exception_handler(request: Request, exc: Exception):
    logger.exception("Unhandled server error")
    return JSONResponse(
        status_code=500,
        content={"error": "Internal Server Error", "message": str(exc)}
    )
