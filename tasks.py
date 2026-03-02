# tasks.py
from crewai import Task
from agents import hr_agent, exp_agent, linkedin_agent, funfact_agent

def create_tasks(employee_name: str):
    return [
        Task(
            agent=hr_agent,
            description=f"Fetch department, role, and date of joining for {employee_name}.",
            expected_output="Department, role, and joining date."
        ),
        Task(
            agent=exp_agent,
            description=f"Summarize work experience for {employee_name}.",
            expected_output="Short summary of prior roles and companies."
        ),
        Task(
            agent=linkedin_agent,
            description=f"Get LinkedIn and any public profile links for {employee_name}.",
            expected_output="List of LinkedIn or GitHub URLs."
        ),
        Task(
            agent=funfact_agent,
            description=f"Retrieve any fun facts or hobbies for {employee_name}.",
            expected_output="A few lines describing hobbies or personal interests."
        )
    ]
