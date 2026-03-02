# agents.py
from crewai import Agent
from tools import FetchEmployeeTool

fetch_employee_tool = FetchEmployeeTool()

def create_agent(name: str, role: str, goal: str, backstory: str) -> Agent:
    return Agent(
        name=name,
        role=role,
        goal=goal,
        backstory=backstory,
        tools=[fetch_employee_tool],
    )

manager = create_agent(
    name="ManagerAgent",
    role="Coordinator",
    goal="Coordinate data retrieval and summarize employee information.",
    backstory="You oversee the data gathering process and create a complete employee profile."
)

hr_agent = create_agent(
    name="HRDataAgent",
    role="Internal Info Finder",
    goal="Fetch internal data (department, role, joining date) from employee records.",
    backstory="You specialize in accessing internal HR data structures."
)

exp_agent = create_agent(
    name="ExperienceAgent",
    role="Experience Retriever",
    goal="Extract and summarize work experience for the employee.",
    backstory="You are adept at interpreting professional experience history."
)

linkedin_agent = create_agent(
    name="LinkedInAgent",
    role="Public Info Retriever",
    goal="Find LinkedIn or GitHub profiles of the employee.",
    backstory="You explore public information sources to locate professional profiles."
)

funfact_agent = create_agent(
    name="FunFactAgent",
    role="Fun Fact Retriever",
    goal="Retrieve fun facts or hobbies from onboarding data.",
    backstory="You help reveal personal touches to make profiles more engaging."
)
