
# **Financial Agent with PhiData**

This project leverages **Phi** and **Groq** models to create a multi-agent system capable of performing web searches and retrieving financial data. **The purpose of this system is to automate the gathering and analysis of financial data, empowering users with timely and accurate insights for making informed decisions.** The system uses a combination of web search tools (DuckDuckGo) and financial data tools (Yahoo Finance) to gather valuable information, such as stock prices, analyst recommendations, company news, and more. The agents work together to fulfill queries related to finance and other domains.


## **Table of Contents**

- [Installation](#installation)
- [Dependencies](#dependencies)
- [Setup](#setup)
- [How to Use](#how-to-use)
- [Recommendation Generated](#recommendation-generated)
- [Configuration](#configuration)
- [License](#license)

## **Installation**

### 1. Clone the repository
Start by cloning this repository to your local machine.

```bash
git clone https://github.com/GaganaMD/Financial-Agent-With-Phidata.git
cd Financial-Agent-With-Phidata
```

### 2. Set up a virtual environment

It is recommended to use a virtual environment to manage the dependencies for the project.

```bash
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

### 3. Install required dependencies

Once the virtual environment is activated, install the necessary dependencies.

```bash
pip install -r requirements.txt
```

## **Dependencies**

This project requires the following Python packages:

- `phi`: A library for fluent functional programming and creating intelligent agents.
- `dotenv`: A library for managing environment variables.
- `yfinance`: To retrieve financial data like stock prices, news, and analyst recommendations.
- `duckduckgo-search`: A library for DuckDuckGo web searches.
- `openai`: The library for OpenAI API integration.

You can install them using the `requirements.txt` file that lists these dependencies.

## **Setup**

### 1. **API Keys**

Before running the program, you need to set up your environment with the required API keys. You need an **OpenAI API key** for Groq models. 

To do this:
- Create a `.env` file in the project root.
- Add your **groq and phi API keys** as follows:
  ```bash
  PHI_API_KEY=your-openai-api-key-here
  GROQ_API_KEY=your-openai-api-key-here
  ```
git
The `.env` file should be loaded automatically with `dotenv` when the script is run.

### 2. **Tools Configuration**
The system uses the following tools:

- **Web Search Agent**: This agent uses DuckDuckGo for querying web search results.
- **Finance AI Agent**: This agent uses Yahoo Finance tools to gather financial data, including:
  - Stock Price
  - Analyst Recommendations
  - Stock Fundamentals
  - Company News
  - Stock History
  - Stock Options

You can customize these agents by modifying their respective configurations in the script.

## **How to Use**

### Run the Multi-Agent System

1. **Start the agent system**:

   The multi-agent system performs actions through a combination of the `websearch_agent` and `financial_agent`. Here's how you can trigger the system:

   ```python
   multi_agent_system.print_response("Summarise analyst recommendations and share the latest news for NVDA", stream=True)
   ```

   This query will instruct the agents to gather and summarize information on **NVIDIA (NVDA)**, including analyst recommendations and the latest company news.

### Modify Queries:

You can modify the query string passed to `multi_agent_system.print_response()` to get different financial or web data. For example:

```python
multi_agent_system.print_response("What is the latest stock news for AAPL?", stream=True)
```

## **Configuration**

You can change the settings of each agent, such as the role, model, instructions, and tools used. For example:

- Change the **model** used by the agents to a different Groq model or any other compatible model.
- Modify the **instructions** to customize how the agents behave when responding to queries.

## **Recommendation Generated**

Here is an example of the recommendation generated by the agent:

![Recommendation Generated](./results/Finance%20Agent%20Recommendations.jpg)


## **License**

This project is licensed under the Apache 2.0 License. See the [LICENSE](LICENSE) file for more details.
