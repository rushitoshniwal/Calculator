# analyze_code.py

import openai
import sys
import os

# Get the staged file path (passed by pre-commit)
file_path = sys.argv[1]

# Read code from the file
with open(file_path, "r") as f:
    code = f.read()

# Set API key from environment
openai.api_key = os.getenv("OPENAI_API_KEY")

# Call GPT-4 or GPT-3.5
response = openai.ChatCompletion.create(
    model="gpt-4",  # or "gpt-3.5-turbo"
    messages=[
        {"role": "system", "content": "You are a senior code reviewer. Point out bugs, performance issues, or bad practices in the code."},
        {"role": "user", "content": f"Review the following Python code:\n\n{code}"}
    ]
)

# Print AI feedback
feedback = response.choices[0].message.content
print("\n📋 OpenAI Code Review Feedback:\n")
print(feedback)

# Optional: Block commit if critical issues are found
if "bug" in feedback.lower() or "zero division" in feedback.lower():
    print("\n❌ Commit blocked due to critical issues.\n")
    sys.exit(1)
