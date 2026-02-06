import os
from github import GithubIntegration
from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import SystemMessage, UserMessage
from azure.core.credentials import AzureKeyCredential

# -------------------------------
# Step 1: GitHub App authentication
# -------------------------------

# Your GitHub App ID
APP_ID = 1234567  # replace with your App ID

# Private key stored as GitHub Secret (no need to open .pem file)
private_key = os.environ.get("HELLOCALL_APP_PRIVATE_KEY")
if not private_key:
    raise ValueError("HELLOCALL_APP_PRIVATE_KEY is not set in Secrets!")

# Authenticate GitHub App
integration = GithubIntegration(APP_ID, private_key)

# Example: generate installation token for your repo
# (replace with your App installation ID)
INSTALLATION_ID = 987654
github_token = integration.get_access_token(INSTALLATION_ID).token

print("✅ GitHub App token generated successfully!")

# -------------------------------
# Step 2: GitHub Models AI
# -------------------------------

endpoint = "https://models.github.ai/inference"
model = "openai/gpt-4.1"

client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(github_token),  # use token from private key
)

# Example AI prompts for HelloCall / EarnWallet
prompts = [
    ("Basic question", "What is the capital of France?"),
    ("EarnWallet free trial", "Explain the free trial and how coins are earned safely."),
    ("Sponsor simulation", "Simulate a user asking about the Sponsor button in HelloCall."),
    ("Playground test", "Run a test prompt as if using the Playground."),
]

# Run all prompts automatically
results = {}
for title, user_input in prompts:
    response = client.complete(
        messages=[
            SystemMessage("You are a helpful assistant for HelloCall / EarnWallet demo."),
            UserMessage(user_input),
        ],
        temperature=0.8,
        top_p=0.9,
        model=model
    )
    results[title] = response.choices[0].message.content

# Save output for review (optional)
with open("ai_runner_outputs.txt", "w", encoding="utf-8") as f:
    for prompt_title, content in results.items():
        f.write(f"--- {prompt_title} ---\n{content}\n\n")

print("✅ AI prompts executed! Check ai_runner_outputs.txt for results.")
