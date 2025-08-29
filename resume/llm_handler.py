from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage
import os
from dotenv import load_dotenv

load_dotenv()

# Get API key
groq_api_key = os.getenv("GROQ_API_KEY")
if not groq_api_key:
    raise ValueError("Missing GROQ_API_KEY in .env file.")

# Initialize LangChain LLM
llm = ChatGroq(
    groq_api_key=groq_api_key,
    model_name="llama3-70b-8192",
    temperature=0.4,
    max_retries=3,
    timeout=30
)

def get_llm_response(prompt):
    """Send prompt to LLM and return response."""
    try:
        response = llm.invoke([HumanMessage(content=prompt)])
        return response.content.strip()
    except Exception as e:
        return f"Error querying LLM: {e}"
