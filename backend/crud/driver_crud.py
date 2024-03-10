from typing import Type

from fastapi_sqlalchemy import db

from backend.crud.db_operations import DBOperations
from backend.models.models import Driver
from backend.schemas.driver import NewDriver, UpdateDriver


class DriverCRUD(DBOperations):
    async def _check_existence(self, driver_id: int) -> Type[Driver] | None:
        driver = db.session.query(Driver).filter(Driver.id == driver_id).first()
        return driver

    async def add_driver(self, new_driver: NewDriver) -> Exception:
        driver_exist = await self._check_existence(driver_id=new_driver.id)

        if driver_exist is not None:
            return Exception("Driver already exist")

        driver = Driver(
            id=new_driver.id,
            first_name=new_driver.first_name,
            last_name=new_driver.last_name,
            phone=new_driver.phone,
            location=new_driver.location,
            driver_license=new_driver.driver_license,
            is_blocked=new_driver.is_blocked
        )
        await self.db_write(driver)

    async def update_driver(self, driver: UpdateDriver) -> Exception | Type[Driver]:
        driver_exist = await self._check_existence(driver_id=driver.id)

        if driver_exist is None:
            return Exception("Driver is not exists")

        for key, value in driver.dict().items():
            if value is not None:
                setattr(driver_exist, key, value)

        await self.db_update()

        return driver_exist
