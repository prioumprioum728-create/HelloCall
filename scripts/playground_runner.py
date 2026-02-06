import os
from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import SystemMessage, UserMessage
from azure.core.credentials import AzureKeyCredential

# ✅ Safe token from GitHub Secrets
token = os.environ.get("HELLOCALL_MODELS_TOKEN")
if not token:
    raise ValueError("HELLOCALL_MODELS_TOKEN is not set!")

# GitHub Models endpoint and model
endpoint = "https://models.github.ai/inference"
model = "openai/gpt-4.1"

client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(token),
)

# Example Playground prompt for HelloCall
system_prompt = SystemMessage(
    "You are a helpful assistant for the HelloCall / EarnWallet demo. "
    "Explain how the free trial works, how coins are earned and spent, "
    "and answer questions safely. No real money is used."
)

user_prompt = UserMessage(
    "Simulate a user asking: 'How do I earn coins in EarnWallet?'"
)

# Call the model
response = client.complete(
    messages=[system_prompt, user_prompt],
    temperature=0.7,
    top_p=0.9,
    model=model
)

# Print AI output
print("Playground Runner Output:\n")
print(response.choices[0].message.content)
