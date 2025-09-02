# 🤖 AI Code Generator

This project is a simple **AI-powered Code Generator** that takes natural language prompts (like "write a Python program for Fibonacci") and generates working code.

✨ Features:
- Convert English to Code
- Run & Execute Generated Code
- Human-friendly documentation
- Extendable for more languages

---

## 🚀 How to Run
1. Clone the repo
   ```bash
   git clone https://github.com/Janexus/AI-Code-Generator.git
   cd AI-Code-Generator
   ```

2. Install requirements
   ```bash
   pip install -r requirements.txt
   ```

3. Run the app
   ```bash
   python app.py
   ```

---

## 📂 Project Structure
- `app.py` → Main runner
- `ai_code_generator/` → Core logic
- `tests/` → Unit tests
- `examples/` → Demo prompts & outputs

---

## 🧪 Example
**Prompt:**  
👉 "Write a Python program that checks if a number is prime."

**Generated Code:**  
```python
def is_prime(n):
    if n <= 1: return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0: return False
    return True
```
---

## 👨‍💻 Author
Made with ❤️ for learning & college projects.
