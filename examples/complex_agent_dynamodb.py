"""Complex agent example with DynamoDB memory persistence."""

import os
from dotenv import load_dotenv
from langchain_stackspot_ai.models import ChatStackSpotAI
from langchain_stackspot_ai.agents import create_stackspot_agent_executor
from langchain_core.tools import Tool
from langchain.memory import ConversationBufferMemory
from langchain.memory.chat_message_histories import DynamoDBChatMessageHistory

# Carregar variáveis de ambiente do arquivo .env
load_dotenv()


def search_tool(query: str) -> str:
    """Ferramenta de busca simulada."""
    return f"Resultado de busca para '{query}': isto é apenas um exemplo."


def calculator_tool(expression: str) -> str:
    """Calculadora simples."""
    try:
        result = eval(expression)
        return f"Resultado: {result}"
    except Exception as e:
        return f"Erro ao calcular expressão: {e}"


def main():
    """Executa um agente com memória persistida no DynamoDB."""
    required_env_vars = [
        "STACKSPOT_CLIENT_ID",
        "STACKSPOT_CLIENT_SECRET",
        "STACKSPOT_SLUG",
        "AWS_REGION",
        "DYNAMODB_TABLE_NAME",
    ]
    missing_vars = [var for var in required_env_vars if var not in os.environ]
    if missing_vars:
        print(
            "Erro: As seguintes variáveis de ambiente são necessárias: "
            + ", ".join(missing_vars)
        )
        print(
            "Por favor, crie um arquivo .env baseado no .env.example e defina "
            "essas variáveis."
        )
        return

    # Configuração de memória no DynamoDB
    chat_history = DynamoDBChatMessageHistory(
        table_name=os.environ["DYNAMODB_TABLE_NAME"],
        session_id="example-session",
        region_name=os.environ["AWS_REGION"],
    )
    memory = ConversationBufferMemory(
        memory_key="chat_history", return_messages=True, chat_memory=chat_history
    )

    # Define ferramentas
    tools = [
        Tool(name="search", func=search_tool, description="Busca na web"),
        Tool(name="calculator", func=calculator_tool, description="Calculadora"),
    ]

    chat = ChatStackSpotAI(
        client_id=os.environ["STACKSPOT_CLIENT_ID"],
        client_secret=os.environ["STACKSPOT_CLIENT_SECRET"],
        slug=os.environ["STACKSPOT_SLUG"],
        tools=tools,
    )

    agent_executor = create_stackspot_agent_executor(
        llm=chat,
        tools=tools,
        system_message="Você é um assistente autônomo que usa ferramentas quando necessário.",
        memory=memory,
        verbose=True,
    )

    print("Executando agente com a pergunta inicial...")
    result = agent_executor.invoke({"input": "Qual é a população do Brasil?"})
    print(result["output"])

    print("\nExecutando pergunta de acompanhamento...")
    result = agent_executor.invoke({"input": "Multiplique esse número por 2"})
    print(result["output"])


if __name__ == "__main__":
    main()

