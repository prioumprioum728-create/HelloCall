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

# Example AI demo for EarnWallet simulation
response = client.complete(
    messages=[
        SystemMessage("You are a kid-friendly assistant for HelloCall/EarnWallet demo."),
        UserMessage("Explain the free trial and how coins are earned and spent safely."),
    ],
    temperature=0.8,
    top_p=0.9,
    model=model
)

print(response.choices[0].message.content)
