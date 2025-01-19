import os
import json
import sys

with open("/Users/sanket/Personal/LLM/LangchainTutorial/config.json") as f:
    env_vars = json.load(f)

HUGGINGFACEHUB_API_TOKEN = env_vars["HF_API_KEY"]
OPENAI_API_KEY = env_vars["OPENAI_API_KEY"]