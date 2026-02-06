import os
from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import SystemMessage, UserMessage
from azure.core.credentials import AzureKeyCredential

# ✅ Safe token from environment
token = os.environ.get("GITHUB_TOKEN")
if not token:
    raise ValueError("GITHUB_TOKEN is not set!")

# GitHub Models endpoint
endpoint = "https://models.github.ai/inference"
model = "openai/gpt-4.1"

client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(token),
)

# List of example prompts you can run from one file
prompts = [
    ("Basic question", "What is the capital of France?"),
    ("EarnWallet free trial", "Explain the free trial and how coins are earned safely."),
    ("Sponsor simulation", "Simulate a user asking about the Sponsor button in HelloCall."),
    ("Playground test", "Run a test prompt as if using the Playground."),
]

# Run all prompts
for title, user_input in prompts:
    print(f"\n--- Prompt: {title} ---\n")
    response = client.complete(
        messages=[
            SystemMessage("You are a helpful assistant for HelloCall / EarnWallet demo."),
            UserMessage(user_input),
        ],
        temperature=0.8,
        top_p=0.9,
        model=model
    )
    print(response.choices[0].message.content)
