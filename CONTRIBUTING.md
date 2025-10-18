# Contributing to SportsHub

Thank you for your interest in contributing to SportsHub! This document provides guidelines and information for contributors.

## How to Contribute

### Reporting Issues
- Use the GitHub issue tracker to report bugs or request features
- Provide clear descriptions and steps to reproduce issues
- Include relevant system information (OS, Python version, etc.)

### Code Contributions
1. Fork the repository
2. Create a feature branch from `main`
3. Make your changes following our coding standards
4. Add tests for new functionality
5. Ensure all tests pass
6. Submit a pull request

### Coding Standards
- Follow PEP 8 style guidelines
- Use meaningful variable and function names
- Add docstrings to functions and classes
- Keep functions focused and small
- Write comprehensive tests

### Testing
- Run the test suite before submitting: `python manage.py test`
- Add tests for new features
- Ensure test coverage doesn't decrease

### Documentation
- Update README.md for significant changes
- Add docstrings to new functions/classes
- Update API documentation if applicable

## Development Setup

1. Clone your fork: `git clone <your-fork-url>`
2. Create virtual environment: `python -m venv venv`
3. Activate environment: `source venv/bin/activate`
4. Install dependencies: `pip install -r requirements.txt`
5. Run migrations: `python manage.py migrate`
6. Create superuser: `python manage.py createsuperuser`
7. Start development server: `python manage.py runserver`

## Pull Request Process

1. Ensure your code follows the project's style guidelines
2. Update documentation as needed
3. Add tests for new functionality
4. Ensure all tests pass
5. Update the CHANGELOG.md if applicable
6. Submit your pull request with a clear description

## Code Review

All submissions require review. We may ask for changes before merging. Please be responsive to feedback and maintain a professional tone.

## License

By contributing, you agree that your contributions will be licensed under the MIT License.
