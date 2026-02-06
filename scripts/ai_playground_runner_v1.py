import os
from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import SystemMessage, UserMessage
from azure.core.credentials import AzureKeyCredential

# ✅ Safe token from GitHub Secrets
token = os.environ.get("HELLOCALL_MODELS_TOKEN")
if not token:
    raise ValueError("HELLOCALL_MODELS_TOKEN is not set!")

endpoint = "https://models.github.ai/inference"
model = "openai/gpt-4.1"

client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(token),
)

# Unique Playground prompt
system_prompt = SystemMessage(
    "You are a friendly assistant for HelloCall / EarnWallet demo. "
    "Explain the free trial, coin system, and answer safely. No real money is used."
)

user_prompt = UserMessage(
    "Simulate a user asking: 'How do I earn coins and use the free trial?'"
)

response = client.complete(
    messages=[system_prompt, user_prompt],
    temperature=0.7,
    top_p=0.9,
    model=model
)

print("AI Playground Runner V1 Output:\n")
print(response.choices[0].message.content)
