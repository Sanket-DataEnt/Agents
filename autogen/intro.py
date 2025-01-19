from auth.config import HUGGINGFACEHUB_API_TOKEN, OPENAI_API_KEY
import os
from utils.logger import logger

os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY
os.environ["HUGGINGFACEHUB_API_TOKEN"] = HUGGINGFACEHUB_API_TOKEN

logger.info("API keys loaded successfully")