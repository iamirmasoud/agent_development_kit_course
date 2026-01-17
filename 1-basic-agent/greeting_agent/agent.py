from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm
from dotenv import load_dotenv

load_dotenv()

root_agent = Agent(
    name="greeting_agent",
    model=LiteLlm(
        model="huggingface/together/meta-llama/Llama-3.3-70B-Instruct"
        # or a smaller / different instruct model on HF
    ),
    description="Greeting agent",
    instruction="""
    You are a helpful assistant that greets the user.
    Ask for the user's name and greet them by name.
    """,
)
