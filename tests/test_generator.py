from ai_code_generator.generator import generate_code

def test_fibonacci():
    code = generate_code("fibonacci")
    assert "def fibonacci" in code

def test_prime():
    code = generate_code("prime")
    assert "def is_prime" in code
