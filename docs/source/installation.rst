Installation
============

Requirements
-----------

* Python 3.11 or higher
* Poetry (recommended for development)

Installing from PyPI
-------------------

The recommended way to install LangChain StackSpot AI is from PyPI:

.. code-block:: bash

   pip install langchain-stackspot-ai

Installing from Source
---------------------

You can also install the package directly from source:

.. code-block:: bash

   git clone https://github.com/stackspot/langchain-stackspot-ai.git
   cd langchain-stackspot-ai
   pip install .

Or using Poetry:

.. code-block:: bash

   git clone https://github.com/stackspot/langchain-stackspot-ai.git
   cd langchain-stackspot-ai
   poetry install

Development Installation
-----------------------

For development, you'll want to install the package with all development dependencies:

.. code-block:: bash

   git clone https://github.com/stackspot/langchain-stackspot-ai.git
   cd langchain-stackspot-ai
   poetry install --with dev

Testing Your Installation
------------------------

You can verify your installation by running:

.. code-block:: python

   import langchain_stackspot_ai
   print(langchain_stackspot_ai.__version__)
