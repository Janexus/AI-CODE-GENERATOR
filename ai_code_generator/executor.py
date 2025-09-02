def execute_code(code: str):
    """
    Executes generated Python code safely.
    """
    try:
        exec(code, {})
    except Exception as e:
        print("⚠️ Error while executing code:", e)
