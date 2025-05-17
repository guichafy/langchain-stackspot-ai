Quickstart
==========

This guide will help you get started with LangChain StackSpot AI quickly.

Basic Usage
----------

First, import the necessary modules:

.. code-block:: python

   from langchain_stackspot_ai.models import ChatStackSpotAI
   from langchain_core.messages import HumanMessage, SystemMessage

Initialize the StackSpot AI chat model with your credentials:

.. code-block:: python

   chat = ChatStackSpotAI(
       client_id="your-client-id",
       client_secret="your-client-secret",
       slug="your-slug"
   )

Now you can use the model to generate responses:

.. code-block:: python

   messages = [
       SystemMessage(content="You are a helpful assistant."),
       HumanMessage(content="What is LangChain?")
   ]

   response = chat.invoke(messages)
   print(response.content)

Using with Tools
---------------

You can also use the StackSpot AI model with LangChain tools:

.. code-block:: python

   from langchain_core.tools import Tool

   # Define tools
   tools = [
       Tool(
           name="search",
           func=lambda query: f"Search results for: {query}",
           description="Search the web for information."
       )
   ]

   # Add tools to the model
   chat.tools = tools

   # Use the model with tools
   messages = [
       SystemMessage(content="You are a helpful assistant."),
       HumanMessage(content="What's the weather in New York?")
   ]

   response = chat.invoke(messages)
   print(response.content)

Creating an Agent
----------------

For more complex interactions, you can create an agent executor:

.. code-block:: python

   from langchain_stackspot_ai.agents import create_stackspot_agent_executor

   # Define tools
   tools = [
       Tool(
           name="search",
           func=lambda query: f"Search results for: {query}",
           description="Search the web for information."
       )
   ]

   # Initialize the StackSpot AI chat model
   chat = ChatStackSpotAI(
       client_id="your-client-id",
       client_secret="your-client-secret",
       slug="your-slug"
   )

   # Create an agent executor
   agent_executor = create_stackspot_agent_executor(
       llm=chat,
       tools=tools,
       system_message="You are a helpful assistant with access to tools."
   )

   # Use the agent
   result = agent_executor.invoke({"input": "What's the weather in New York?"})
   print(result["output"])

Adding Memory
------------

You can add conversation memory to your agent:

.. code-block:: python

   from langchain.memory import ConversationBufferMemory

   # Create memory
   memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)

   # Create an agent executor with memory
   agent_executor = create_stackspot_agent_executor(
       llm=chat,
       tools=tools,
       system_message="You are a helpful assistant with access to tools.",
       memory=memory
   )

   # Use the agent
   result = agent_executor.invoke({"input": "What's the weather in New York?"})
   print(result["output"])

   # Continue the conversation
   result = agent_executor.invoke({"input": "How about tomorrow?"})
   print(result["output"])
