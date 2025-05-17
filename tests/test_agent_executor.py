"""Tests for the StackSpot AI agent executor."""

import unittest
from unittest.mock import patch, MagicMock

from langchain_core.tools import Tool
from langchain_core.messages import AIMessage
from langchain_stackspot_ai.models import ChatStackSpotAI
from langchain_stackspot_ai.agents import create_stackspot_agent_executor


class TestAgentExecutor(unittest.TestCase):
    """Test cases for the StackSpot AI agent executor."""

    def setUp(self):
        """Set up test fixtures."""
        self.model = ChatStackSpotAI(
            client_id="test-client-id",
            client_secret="test-client-secret",
            slug="test-slug"
        )
        
        # Create test tools
        self.tools = [
            Tool(
                name="search",
                func=lambda query: f"Search results for: {query}",
                description="Search the web for information."
            ),
            Tool(
                name="calculator",
                func=lambda expression: eval(expression),
                description="Calculate mathematical expressions."
            )
        ]

    @patch("langchain_stackspot_ai.adapters.function_adapter.StackSpotFunctionCallAdapter.invoke")
    def test_agent_executor_creation(self, mock_invoke):
        """Test creating an agent executor."""
        # Mock the adapter invoke method
        mock_invoke.return_value = AIMessage(content="I'll use the search tool. Use tool: search({\"query\": \"test query\"})")
        
        # Create the agent executor
        agent_executor = create_stackspot_agent_executor(
            llm=self.model,
            tools=self.tools,
            system_message="You are a helpful assistant with access to tools."
        )
        
        # Assertions
        self.assertIsNotNone(agent_executor)
        self.assertEqual(len(agent_executor.tools), 2)
        self.assertEqual(agent_executor.tools[0].name, "search")
        self.assertEqual(agent_executor.tools[1].name, "calculator")

    @patch("langchain_stackspot_ai.adapters.function_adapter.StackSpotFunctionCallAdapter.invoke")
    @patch("langchain_stackspot_ai.adapters.output_parser.StackSpotFunctionsAgentOutputParser.parse")
    def test_agent_executor_invoke(self, mock_parse, mock_invoke):
        """Test invoking the agent executor."""
        from langchain_core.agents import AgentAction, AgentFinish
        
        # Mock the adapter invoke method
        mock_invoke.return_value = AIMessage(content="I'll use the search tool. Use tool: search({\"query\": \"test query\"})")
        
        # Mock the output parser to first return a tool call, then a final answer
        mock_parse.side_effect = [
            AgentAction(tool="search", tool_input={"query": "test query"}, log=""),
            AgentFinish(return_values={"output": "Final answer"}, log="")
        ]
        
        # Create the agent executor
        agent_executor = create_stackspot_agent_executor(
            llm=self.model,
            tools=self.tools,
            system_message="You are a helpful assistant with access to tools."
        )
        
        # Invoke the agent
        result = agent_executor.invoke({"input": "What can you tell me about test query?"})
        
        # Assertions
        self.assertIn("output", result)
        self.assertEqual(result["output"], "Final answer")
        self.assertIn("intermediate_steps", result)
        mock_invoke.assert_called()
        mock_parse.assert_called()


if __name__ == "__main__":
    unittest.main()
