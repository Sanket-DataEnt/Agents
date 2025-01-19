'''
Conversable Agent: Introduction
Primary Purpose: Base class for building customizable agents that can talk and interact with other agents, people, and tools to solve tasks.
Customizable: Highly customizable, allowing for the integration of LL.M.s, people and tools.
'''

import os
from utils.logger import logger
from autogen import ConversableAgent
from auth.config import OPENAI_API_KEY

agent = ConversableAgent(
    "chatbot",
    llm_config={"config_list": [{"model": "gpt-4o-mini", "api_key": OPENAI_API_KEY}]},
    code_execution_config=False,  # Turn off code execution, by default it is off.
    function_map=None,  # No registered functions, by default it is None.
    human_input_mode="NEVER",  # Never ask for human input.
)
## https://microsoft.github.io/autogen/0.2/docs/topics/llm_configuration/ (LLM Configuration List)

reply = agent.generate_reply(messages=[{"content": "Tell me a joke.", "role": "user"}])
# logger.info("REPLY : ",reply)
print(reply)