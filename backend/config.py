"""Configuration for the LLM Council."""

import os
from pathlib import Path
from dotenv import load_dotenv

PROJECT_ROOT = Path(__file__).resolve().parent.parent
load_dotenv(PROJECT_ROOT / ".env")

# OpenRouter API key (set in .env)
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

# Council members - valid OpenRouter model identifiers
COUNCIL_MODELS = [
    "openai/gpt-4o-mini",
    "anthropic/claude-3.5-haiku",
    "x-ai/grok-3-mini-beta",
    "meta-llama/llama-3.1-70b-instruct",
]

# Chairman model - synthesizes final response
CHAIRMAN_MODEL = "openai/gpt-4o-mini"

# OpenRouter API endpoint
OPENROUTER_API_URL = "https://openrouter.ai/api/v1/chat/completions"

# Data directory for conversation storage
DATA_DIR = "data/conversations"
