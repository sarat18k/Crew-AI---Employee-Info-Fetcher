# crewai_app.py
import json
import os
from dotenv import load_dotenv
from crewai import Crew
from agents import manager
from tasks import create_tasks
from tools import FetchEmployeeTool

# Load environment variables from .env file
load_dotenv()

def get_employee_data(employee_name: str):
    tool = FetchEmployeeTool()
    result = tool._run(employee_name)
    parsed = json.loads(result)
    return parsed

def main():
    employee_name = input("Enter employee name: ").strip()
    employee_data = get_employee_data(employee_name)

    if employee_data.get("status") != "success":
        print(f"\n❌ Error: {employee_data.get('message')}")
        return

    print(f"\n✅ Found {employee_name} in records. Proceeding...\n")

    tasks = create_tasks(employee_name)
    crew = Crew(
        agents=[manager] + [task.agent for task in tasks],
        tasks=tasks,
        manager=manager,
        verbose=True
    )

    result = crew.kickoff(inputs={})

    print("\n🔎 Final Summary for Employee:")
    print("-" * 50)
    print(result)

if __name__ == "__main__":
    main()
