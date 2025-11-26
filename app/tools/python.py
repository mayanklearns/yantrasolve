from langchain_core.tools import tool


@tool
def python_tool(code: str) -> str:
    """
    Executes Python code.
    """
    # TODO: Implement actual Python execution
    return f"Executed Python code:\n{code}"
