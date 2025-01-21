'''
Document to explore how to terminate a conversation between AutoGen agents.

Mechanism to terminate a conversation between AutoGen agents:
1.Specify parameters in initiate_chat: When initiating a chat, 
    you can define parameters that determine when the conversation should end.

2. Configure an agent to trigger termination: When defining individual agents, 
    you can specify parameters that allow agents to terminate of a conversation based on 
    particular (configurable) conditions.
'''

### 1. Specify parameters in initiate_chat
# In the following example, we specify the max_turns parameter to limit the conversation to 3 turns.
# The conversation will end after 3 turns.

import os
from utils.logger import logger
from autogen import ConversableAgent
from auth.config import OPENAI_API_KEY

cathy = ConversableAgent(
    "cathy",
    system_message="Your name is Cathy and you are a part of a duo of comedians.",
    llm_config={"config_list": [{"model": "gpt-4o-mini", "temperature": 0.9, "api_key": OPENAI_API_KEY}]},
    human_input_mode="NEVER",  # Never ask for human input.
)

joe = ConversableAgent(
    "joe",
    system_message="Your name is Joe and you are a part of a duo of comedians.",
    llm_config={"config_list": [{"model": "gpt-4o-mini", "temperature": 0.7, "api_key": OPENAI_API_KEY}]},
    human_input_mode="NEVER",  # Never ask for human input.
)

# result = joe.initiate_chat(cathy, 
#                            message="Cathy, tell me a joke.", 
#                            max_turns=3)

### 2. Configure an agent to trigger termination
'''
You can also terminate a conversation by configuring parameters of an agent. Currently, there are two parameters you can configure:

1. max_consecutive_auto_reply: This condition triggers termination if the number of automatic responses to the same 
    sender exceeds a threshold. You can customize this using the max_consecutive_auto_reply argument of the 
    ConversableAgent class. To accomplish this the agent maintains a counter of the number of consecutive automatic 
    responses to the same sender. Note that this counter can be reset because of human intervention. We will 
    describe this in more detail in the next chapter.
2. is_termination_msg: This condition can trigger termination if the received message satisfies a particular condition, 
    e.g., it contains the word “TERMINATE”. You can customize this condition using the is_terminate_msg argument in 
    the constructor of the ConversableAgent class.
'''

# Example of using max_consecutive_auto_reply
# In the example below lets set max_consecutive_auto_reply to 1 and notice how this ensures that Joe only replies once.

joe = ConversableAgent(
    "joe",
    system_message="Your name is Joe and you are a part of a duo of comedians.",
    llm_config={"config_list": [{"model": "gpt-4o-mini", "temperature": 0.7, "api_key": OPENAI_API_KEY}]},
    human_input_mode="NEVER",  # Never ask for human input.
    max_consecutive_auto_reply=1  # Joe will only reply once.
)

# result = joe.initiate_chat(cathy, 
#                            message="Cathy, tell me a joke.", 
#                            )

# Example of using is_termination_msg
# Let’s set the termination message to “GOOD BYE” and see how the conversation terminates.

joe = ConversableAgent(
    "joe",
    system_message="Your name is Joe and you are a part of a duo of comedians.",
    llm_config={"config_list": [{"model": "gpt-4o-mini", "temperature": 0.7, "api_key": OPENAI_API_KEY}]},
    human_input_mode="NEVER",  # Never ask for human input.
    is_termination_msg=lambda msg: "good bye" in msg["content"].lower(),
                    )
result = joe.initiate_chat(cathy, message="Cathy, tell me a joke and then say the words GOOD BYE.")
