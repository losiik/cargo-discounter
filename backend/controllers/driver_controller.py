from fastapi import APIRouter, UploadFile, Form, File
from fastapi.exceptions import HTTPException
from backend.services.driver_service import DriverService
from backend.schemas.driver import SchemaDriver, SchemaBaseDriver

driver_router = APIRouter(prefix='/driver')

driver_router.tags = ["Driver"]

driver_service = DriverService()


@driver_router.post("/", response_model=SchemaDriver)
async def add_driver(new_driver: SchemaBaseDriver, driver_license: UploadFile = File(...)):
    exception = await driver_service.add_driver(new_driver=new_driver, driver_license=driver_license)
    if exception is not None:
        raise HTTPException(status_code=400, detail=str(exception))

    return new_driver


@driver_router.patch("/", response_model=SchemaDriver)
async def change_driver(update_driver: SchemaDriver):
    driver = await driver_service.update_driver(driver=update_driver)

    if type(driver) is Exception:
        raise HTTPException(status_code=400, detail=str(driver))

    return driver


@driver_router.patch("/driver_license", response_model=SchemaDriver)
async def change_driver_license():
    pass


@driver_router.get("/{driver_id}", response_model=SchemaDriver)
async def get_driver(driver_id: int):
    driver = await driver_service.get_driver(driver_id=driver_id)

    if type(driver) is Exception:
        raise HTTPException(status_code=400, detail=str(driver))

    return driver
