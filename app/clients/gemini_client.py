import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.agents import create_agent
from langchain.tools import tool

from app.core.logger_config import get_logger
from app.core.settings import GOOGLE_GEMINI_API_KEY

logger = get_logger(__name__)


def load_model():
    '''
    loads the Gemini LLM model using the provided API key. 
    '''
    try: 
        llm = ChatGoogleGenerativeAI(
        model="gemini-3.5-flash-lite",  
        api_key="GOOGLE_GEMINI_API_KEY"
        )

        logger.info("Gemini LLM model loaded successfully.")
        return llm
    except Exception as e:
        logger.error(f"Error loading Gemini LLM model: {e}")
        raise e


def create_gemini_agent(llm=None, tools = [], respone_format = None):
    '''
    Creates a Gemini agent using the provided LLM, tools, and response format.
    Args:
        llm: The loaded Gemini LLM model.
        tools (list): A list of tools to be used by the agent.
        response_format: The desired response format for the agent.
        Returns:
            The created Gemini agent.
        '''
    if llm is None:
        llm = load_model()
    return create_agent(model=llm, tools=tools, response_format=respone_format)