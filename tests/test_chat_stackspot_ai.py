"""Tests for the ChatStackSpotAI model."""

import unittest
from unittest.mock import patch, MagicMock
import json

from langchain_core.messages import HumanMessage, SystemMessage
from langchain_stackspot_ai.models import ChatStackSpotAI


class TestChatStackSpotAI(unittest.TestCase):
    """Test cases for the ChatStackSpotAI model."""

    def setUp(self):
        """Set up test fixtures."""
        self.model = ChatStackSpotAI(
            client_id="test-client-id",
            client_secret="test-client-secret",
            slug="test-slug"
        )

    @patch("requests.post")
    def test_get_token(self, mock_post):
        """Test getting an authentication token."""
        # Mock the response
        mock_response = MagicMock()
        mock_response.json.return_value = {"access_token": "test-token"}
        mock_post.return_value = mock_response

        # Call the method
        token = self.model._get_token()

        # Assertions
        self.assertEqual(token, "test-token")
        mock_post.assert_called_once()
        url = f"{self.model.auth_url}/{self.model.realm}/oidc/oauth/token"
        self.assertEqual(mock_post.call_args[0][0], url)

    @patch("requests.post")
    @patch("requests.get")
    def test_generate(self, mock_get, mock_post):
        """Test generating a response from the model."""
        # Mock the token request
        token_response = MagicMock()
        token_response.json.return_value = {"access_token": "test-token"}
        
        # Mock the quick command creation
        create_response = MagicMock()
        create_response.json.return_value = {"id": "test-command-id"}
        
        # Mock the polling response
        poll_response = MagicMock()
        poll_response.json.return_value = {
            "status": "completed",
            "result": "This is a test response."
        }
        
        # Set up the mock responses
        mock_post.side_effect = [token_response, create_response]
        mock_get.return_value = poll_response
        
        # Create messages
        messages = [
            SystemMessage(content="You are a helpful assistant."),
            HumanMessage(content="Hello, how are you?")
        ]
        
        # Call the model
        result = self.model.invoke(messages)
        
        # Assertions
        self.assertEqual(result.content, "This is a test response.")
        self.assertEqual(mock_post.call_count, 2)
        self.assertEqual(mock_get.call_count, 1)

    @patch("langchain_stackspot_ai.models.chat_stackspot_ai.ChatStackSpotAI._get_token")
    @patch("langchain_stackspot_ai.models.chat_stackspot_ai.ChatStackSpotAI._create_quick_command")
    @patch("langchain_stackspot_ai.models.chat_stackspot_ai.ChatStackSpotAI._poll_quick_command")
    def test_tool_parsing(self, mock_poll, mock_create, mock_token):
        """Test parsing tool calls from the model response."""
        # Mock the responses
        mock_token.return_value = "test-token"
        mock_create.return_value = "test-command-id"
        mock_poll.return_value = {
            "status": "completed",
            "result": "I'll help you with that. Use tool: search({\"query\": \"weather in New York\"})"
        }
        
        # Create a tool
        from langchain_core.tools import Tool
        search_tool = Tool(
            name="search",
            func=lambda query: f"Search results for: {query}",
            description="Search the web for information."
        )
        
        # Add the tool to the model
        self.model.tools = [search_tool]
        
        # Create messages
        messages = [
            SystemMessage(content="You are a helpful assistant."),
            HumanMessage(content="What's the weather in New York?")
        ]
        
        # Call the model
        result = self.model.invoke(messages)
        
        # The result should contain both the original response and the tool result
        self.assertIn("I'll help you with that", result.content)
        self.assertIn("Tool search result", result.content)
        self.assertIn("Search results for: weather in New York", result.content)


if __name__ == "__main__":
    unittest.main()
