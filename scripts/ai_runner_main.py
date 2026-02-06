import os
from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import SystemMessage, UserMessage
from azure.core.credentials import AzureKeyCredential

def run_all_prompts():
    # ✅ Safe token from environment / secrets
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

    # Example prompts
    prompts = [
        ("Basic question", "What is the capital of France?"),
        ("EarnWallet free trial", "Explain the free trial and how coins are earned safely."),
        ("Sponsor simulation", "Simulate a user asking about the Sponsor button in HelloCall."),
        ("Playground test", "Run a test prompt as if using the Playground."),
    ]

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

    return results

# Run automatically when the script is imported or used in workflow
outputs = run_all_prompts()

# Optional: store results in a file for GitHub Actions or Codespaces
with open("ai_runner_outputs.txt", "w", encoding="utf-8") as f:
    for prompt_title, content in outputs.items():
        f.write(f"--- {prompt_title} ---\n{content}\n\n")
