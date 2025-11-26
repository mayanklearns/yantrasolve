from langchain_core.tools import tool


@tool
def javascript_tool(code: str) -> str:
    """
    Executes JavaScript code.
    """
    # TODO: Implement actual JavaScript execution in the browser
    return f"Executed JavaScript code:\n{code}"
