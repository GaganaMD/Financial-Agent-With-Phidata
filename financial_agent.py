from phi.agent import Agent
import os
from phi.model.groq import Groq
# from phi.tools.yfinance import YFinance
from phi.tools.duckduckgo import DuckDuckGo
from phi.tools.yfinance import YFinanceTools


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

# Multi-agent system

multi_agent_system = Agent(
    team = [websearch_agent, financial_agent],
    model = Groq(id="llama3-groq-70b-8192-tool-use-preview"),
    instructions=["Always include sources","Use tabels to display the data"],
    show_tool_calls=True,
    markdown=True
)

multi_agent_system.print_response("Summarise analyst recommendations and share the latest news for NVDA",stream=True)

