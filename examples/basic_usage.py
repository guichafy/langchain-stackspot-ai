"""Basic usage example for LangChain StackSpot AI."""

import os
from dotenv import load_dotenv
from langchain_stackspot_ai.models import ChatStackSpotAI
from langchain_core.messages import HumanMessage, SystemMessage

# Carregar variáveis de ambiente do arquivo .env
load_dotenv()

def main():
    """Run a basic example of using ChatStackSpotAI."""
    # Verificar se as variáveis de ambiente necessárias estão definidas
    required_env_vars = ["STACKSPOT_CLIENT_ID", "STACKSPOT_CLIENT_SECRET", "STACKSPOT_SLUG"]
    missing_vars = [var for var in required_env_vars if var not in os.environ]
    
    if missing_vars:
        print(f"Erro: As seguintes variáveis de ambiente são necessárias: {', '.join(missing_vars)}")
        print("Por favor, crie um arquivo .env baseado no .env.example e defina essas variáveis.")
        return
    
    # Initialize the StackSpot AI chat model
    chat = ChatStackSpotAI(
        client_id=os.environ["STACKSPOT_CLIENT_ID"],
        client_secret=os.environ["STACKSPOT_CLIENT_SECRET"],
        slug=os.environ["STACKSPOT_SLUG"]
    )

    # Create messages
    messages = [
        SystemMessage(content="You are a helpful assistant specialized in Python programming."),
        HumanMessage(content="How do I read a JSON file in Python?")
    ]

    # Get a response
    response = chat.invoke(messages)
    
    # Print the response
    print("Response from StackSpot AI:")
    print(response.content)

if __name__ == "__main__":
    main()
