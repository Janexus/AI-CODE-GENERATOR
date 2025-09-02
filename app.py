from ai_code_generator.generator import generate_code
from ai_code_generator.executor import execute_code

def main():
    print("🤖 Welcome to AI Code Generator!")
    prompt = input("👉 Enter your prompt: ")

    code = generate_code(prompt)
    print("\n✨ Generated Code:\n")
    print(code)

    run = input("\n▶️ Do you want to execute this code? (y/n): ")
    if run.lower() == 'y':
        execute_code(code)

if __name__ == "__main__":
    main()
