from auth.config import HUGGINGFACEHUB_API_TOKEN, OPENAI_API_KEY
import os
from utils.logger import logger
import autogen
from autogen import AssistantAgent, UserProxyAgent

os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY
os.environ["HUGGINGFACEHUB_API_TOKEN"] = HUGGINGFACEHUB_API_TOKEN

logger.info("API keys loaded successfully")

# llm_config = {"model": "gpt-4o-mini", "api_key": OPENAI_API_KEY}
# assistant = AssistantAgent("assistant",llm_config=llm_config)

# logger.info("assistant created successfully")

# user_proxy = UserProxyAgent(
#     "user_proxy", code_execution_config={"executor": autogen.coding.LocalCommandLineCodeExecutor(work_dir="coding")}
# )

# # Start the chat
# user_proxy.initiate_chat(
#     assistant,
#     message="Plot a chart of NVDA and TESLA stock price change YTD.",
# )