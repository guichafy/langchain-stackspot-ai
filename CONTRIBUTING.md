# Contributing to LangChain StackSpot AI

Thank you for considering contributing to LangChain StackSpot AI! This document provides guidelines and instructions for contributing to this project.

## Code of Conduct

By participating in this project, you agree to abide by our Code of Conduct. Please be respectful and considerate of others.

## How to Contribute

### Reporting Bugs

If you find a bug, please create an issue with the following information:

- A clear, descriptive title
- Steps to reproduce the issue
- Expected behavior
- Actual behavior
- Any relevant logs or screenshots
- Your environment (Python version, OS, etc.)

### Suggesting Enhancements

We welcome suggestions for enhancements! Please create an issue with:

- A clear, descriptive title
- A detailed description of the proposed enhancement
- Any relevant examples or use cases

### Pull Requests

1. Fork the repository
2. Create a new branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Run tests to ensure they pass
5. Commit your changes (`git commit -m 'Add some amazing feature'`)
6. Push to the branch (`git push origin feature/amazing-feature`)
7. Open a Pull Request

## Development Setup

1. Clone the repository
   ```bash
   git clone https://github.com/stackspot/langchain-stackspot-ai.git
   cd langchain-stackspot-ai
   ```

2. Install development dependencies
   ```bash
   poetry install
   ```

3. Activate the virtual environment
   ```bash
   poetry shell
   ```

## Code Style

We use the following tools to maintain code quality:

- **Black** for code formatting
- **isort** for import sorting
- **mypy** for type checking
- **flake8** for linting

You can run these tools with:

```bash
# Format code
black langchain_stackspot_ai tests

# Sort imports
isort langchain_stackspot_ai tests

# Type checking
mypy langchain_stackspot_ai

# Linting
flake8 langchain_stackspot_ai tests
```

## Testing

We use pytest for testing. Run the tests with:

```bash
pytest
```

To run tests with coverage:

```bash
pytest --cov=langchain_stackspot_ai
```

## Documentation

We use Sphinx for documentation. To build the docs:

```bash
cd docs
make html
```

## Release Process

1. Update version in `pyproject.toml`
2. Update CHANGELOG.md
3. Create a new release on GitHub
4. Publish to PyPI:
   ```bash
   poetry publish --build
   ```

## License

By contributing to this project, you agree that your contributions will be licensed under the project's MIT License.
