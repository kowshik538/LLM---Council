"""Configuration for the LLM Council."""

import os
from pathlib import Path
from dotenv import load_dotenv

PROJECT_ROOT = Path(__file__).resolve().parent.parent
load_dotenv(PROJECT_ROOT / ".env")

# OpenRouter API key (set in .env / deployment environment).
# Normalize common env formatting mistakes (quotes/newlines/spaces).
_raw_openrouter_key = (os.getenv("OPENROUTER_API_KEY") or "").strip()
if (
    len(_raw_openrouter_key) >= 2
    and _raw_openrouter_key[0] == _raw_openrouter_key[-1]
    and _raw_openrouter_key[0] in {"'", '"'}
):
    _raw_openrouter_key = _raw_openrouter_key[1:-1].strip()
OPENROUTER_API_KEY = _raw_openrouter_key or None

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
