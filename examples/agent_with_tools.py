"""Example of using StackSpot AI with tools and agents."""

import os
from dotenv import load_dotenv
from langchain_stackspot_ai.models import ChatStackSpotAI
from langchain_stackspot_ai.agents import create_stackspot_agent_executor
from langchain_core.tools import Tool
from langchain.memory import ConversationBufferMemory

# Carregar variáveis de ambiente do arquivo .env
load_dotenv()

def search_tool(query: str) -> str:
    """Mock search tool that would normally call a search API."""
    return f"Search results for '{query}': This is a simulated search result."

def calculator_tool(expression: str) -> str:
    """Calculator tool that evaluates mathematical expressions."""
    try:
        result = eval(expression)
        return f"Result: {result}"
    except Exception as e:
        return f"Error evaluating expression: {e}"

def main():
    """Run an example of using StackSpot AI with tools and agents."""
    # Verificar se as variáveis de ambiente necessárias estão definidas
    required_env_vars = ["STACKSPOT_CLIENT_ID", "STACKSPOT_CLIENT_SECRET", "STACKSPOT_SLUG"]
    missing_vars = [var for var in required_env_vars if var not in os.environ]
    
    if missing_vars:
        print(f"Erro: As seguintes variáveis de ambiente são necessárias: {', '.join(missing_vars)}")
        print("Por favor, crie um arquivo .env baseado no .env.example e defina essas variáveis.")
        return
    
    # Define tools
    tools = [
        Tool(
            name="search",
            func=search_tool,
            description="Search the web for information. Input should be a search query."
        ),
        Tool(
            name="calculator",
            func=calculator_tool,
            description="Calculate mathematical expressions. Input should be a mathematical expression."
        )
    ]
    
    # Initialize the StackSpot AI chat model with tools
    chat = ChatStackSpotAI(
        client_id=os.environ["STACKSPOT_CLIENT_ID"],
        client_secret=os.environ["STACKSPOT_CLIENT_SECRET"],
        slug=os.environ["STACKSPOT_SLUG"],
        tools=tools
    )

    # Tools are already defined and passed to the chat model

    # Create memory for the conversation
    memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)

    # Create an agent executor
    agent_executor = create_stackspot_agent_executor(
        llm=chat,
        tools=tools,
        system_message="You are a helpful assistant with access to tools. Use them when needed to answer user questions.",
        memory=memory,
        verbose=True
    )

    # Run the agent
    print("Running agent with query: 'What's 25 * 48?'")
    result = agent_executor.invoke({"input": "What's 25 * 48?"})
    print("\nAgent response:")
    print(result["output"])

    # Continue the conversation to demonstrate memory
    print("\nRunning follow-up query: 'Now divide that by 7'")
    result = agent_executor.invoke({"input": "Now divide that by 7"})
    print("\nAgent response:")
    print(result["output"])

if __name__ == "__main__":
    main()
