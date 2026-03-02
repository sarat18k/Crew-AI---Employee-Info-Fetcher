# tools.py
import json
from typing import Type
from pydantic import BaseModel, Field
from crewai.tools import BaseTool
from config import EMPLOYEE_DATA_FILE
import logging

# Logging setup
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class EmployeeToolInput(BaseModel):
    name: str = Field(..., description="Full name of the employee")

class FetchEmployeeTool(BaseTool):
    name: str = "fetch_employee"
    description: str = "Retrieve employee data by name from internal knowledge base"
    args_schema: Type[BaseModel] = EmployeeToolInput

    def _run(self, name: str) -> str:
        logger.info(f"Fetching employee data for: {name}")
        try:
            with open(EMPLOYEE_DATA_FILE, "r") as f:
                employees = json.load(f)
        except Exception as e:
            return json.dumps({"status": "error", "message": f"Failed to read data: {str(e)}"}, indent=2)

        for emp in employees:
            if emp["name"].lower() == name.lower():
                return json.dumps({"status": "success", "data": emp}, indent=2)

        return json.dumps({"status": "error", "message": "Employee not found"}, indent=2)
