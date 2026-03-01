import os
from dotenv import load_dotenv

load_dotenv()

if not os.getenv("GITHUB_TOKEN"):
  raise ValueError("GITHUB_TOKEN is not set")

os.environ["OPENAI_API_KEY"] = os.getenv("GITHUB_TOKEN")
os.environ["OPENAI_BASE_URL"] = "https://models.inference.ai.azure.com/"