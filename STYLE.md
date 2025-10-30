# Python Coding Style Guide
## Overview
This document defines the coding standards for this project. All code must follow these conventions for consistency and maintainability.
## Indentation
- Use **tab character** for indentation (not spaces)
- Users may configure tab width in their editor as preferred
## Naming Conventions
- **Functions and variables**: `lowercase_with_underscores`
- **Constants**: `UPPERCASE_WITH_UNDERSCORES`
- **Classes**: `CapitalizedWords` (if used)
- **Loop counters**: Short names (`i`, `j`, `idx`)
- Keep names descriptive but concise
## Line Length
- Target: 80 columns
- Maximum: 100 columns
## Functions
- Keep short and focused (24-48 lines ideal)
- Each function does "one thing" well
- If function has 10+ local variables, split it
- Always include docstring with description, parameters, and return value:
```python
def function_name(param1, param2):
	"""
	Brief description of what function does
	param1: description of first parameter
	param2: description of second parameter
	return: description of return value
	"""
```
## Code Structure
- One statement per line
- Maximum nesting depth: 3-4 levels
- Avoid camelCase (except for class names)
## Comments
- Use `# for inline comments`
- Keep comments concise and relevant
- Code should be self-documenting; excessive comments indicate complexity
## Imports
- Group in order: standard library, third-party, local
- One import per line
- Place at top of file
## Whitespace
- Blank line after docstrings
- Blank line between function definitions
- No trailing whitespace
---
_All contributors must adhere to this style guide. Consistency is mandatory across the entire codebase._
