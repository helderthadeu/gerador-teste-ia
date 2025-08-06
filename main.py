from langchain.agents import initialize_agent, Tool, AgentType
from langchain.tools.python.tool import PythonREPL


tool = [
    Tool(name="ExecCode", func=PythonREPL().run, description="Generate the test and execute for this code")
]

agent = initialize_agent(tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION)


while True:
    code = input("Paste the code that you would like to test: ")

    agent.run(code)
    