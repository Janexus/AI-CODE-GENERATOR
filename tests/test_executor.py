from ai_code_generator.executor import execute_code

def test_executor_runs():
    code = "print('Hello from executor!')"
    execute_code(code)
