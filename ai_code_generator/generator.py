def generate_code(prompt: str) -> str:
    """
    Dummy code generator (replace with real LLM later).
    Currently just handles a few keywords.
    """
    if "fibonacci" in prompt.lower():
        return """def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        print(a, end=" ")
        a, b = b, a+b
"""
    elif "prime" in prompt.lower():
        return """def is_prime(n):
    if n <= 1: return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0: return False
    return True
"""
    else:
        return "# 🤖 Sorry, I don’t know how to generate that yet."
