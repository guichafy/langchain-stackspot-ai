Welcome to LangChain StackSpot AI's documentation!
==============================================

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   installation
   quickstart
   modules/index
   examples/index
   api_reference
   contributing
   changelog

LangChain StackSpot AI is a Python library that provides seamless integration between StackSpot AI and LangChain, enabling developers to leverage StackSpot AI's capabilities within the LangChain ecosystem.

Features
--------

- Easy-to-use StackSpot AI chat model implementation for LangChain
- Function calling support with StackSpot AI
- Agent executors that work with StackSpot AI
- Adapters for converting between LangChain and StackSpot AI formats
- Comprehensive documentation and examples

Installation
-----------

.. code-block:: bash

   pip install langchain-stackspot-ai

Quick Start
----------

.. code-block:: python

   from langchain_stackspot_ai.models import ChatStackSpotAI
   from langchain_core.messages import HumanMessage, SystemMessage

   # Initialize the StackSpot AI chat model
   chat = ChatStackSpotAI(
       client_id="your-client-id",
       client_secret="your-client-secret",
       slug="your-slug"
   )

   # Use the model
   messages = [
       SystemMessage(content="You are a helpful assistant."),
       HumanMessage(content="What is LangChain?")
   ]

   response = chat.invoke(messages)
   print(response.content)

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
