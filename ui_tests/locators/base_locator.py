from typing import Optional

from pydantic import BaseModel, ConfigDict, Field, field_validator
from selenium.webdriver.common.by import By


class Locator(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)

    by: str = Field(default=By.XPATH)
    value: str
    name: Optional[str] = None

    @field_validator("by")
    def validate_by(cls, v):
        if v != By.XPATH:
            raise ValueError(
                f"Неподдерживаемый тип локатора: {v}. Разрешен только XPATH"
            )
        return v

    def __repr__(self):
        return f"Locator(by={self.by}, value={self.value}, name={self.name})"

    def format(self, *args, **kwargs):
        formatted_value = self.value.format(*args, **kwargs)
        return Locator(by=self.by, value=formatted_value, name=self.name)



