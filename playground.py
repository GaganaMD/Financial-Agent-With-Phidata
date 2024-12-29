import os
import phi
import phi.api

from dotenv import load_dotenv
from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.duckduckgo import DuckDuckGo
from phi.tools.yfinance import YFinanceTools
from phi.playground import Playground, serve_playground_app

load_dotenv()
phi.api = os.getenv("PHI_API_KEY")

# Web search agent
websearch_agent = Agent(
    name = "Web Search Agent",
    role = "Search the web for information",
    model = Groq(id="llama3-groq-70b-8192-tool-use-preview"),
    tools = [DuckDuckGo()],
    instructions=["Always include sources"],
    show_tool_calls=True,
    markdown=True
)

# Financial agent
financial_agent = Agent(
    name = "Finance AI Agent",
    # role = "Search the web for information",
    model = Groq(id="llama3-groq-70b-8192-tool-use-preview"),
    tools=[YFinanceTools(stock_price=True, analyst_recommendations=True, stock_fundamentals=True,
                         company_news=True)],
    instructions=["Use tabels to display the data"],
    show_tool_calls=True,
    markdown=True
)

# playground
app = Playground(
    agents = [websearch_agent, financial_agent]
    ).get_app(),

if __name__ == "__main__":
    serve_playground_app("playground:app",reload=True)