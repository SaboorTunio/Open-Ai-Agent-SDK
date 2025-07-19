import asyncio
import os
from dotenv import load_dotenv
from openai import AsyncOpenAI
from agents import Agent, OpenAIChatCompletionsModel, Runner ,set_tracing_disabled


# Load environment variables from .env file
load_dotenv()
gemini_api_key = os.getenv("GEMINI_API_KEY")

# Initialize the OpenAI client with the Gemini API key

client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

set_tracing_disabled(disabled=True)

async def main():
    # The agent that will suggest products based on user input
    agent = Agent(
        name="ProductSuggester",
        instructions="""You're an AI agent designed to provide helpful guidance about medicines based on symptoms shared by users. When a user describes a health concern, such as saying “I have a headache,” your role is to:
        - 🧠 Understand the symptom clearly and ask follow-up questions if needed.
        - 💊 Suggest commonly known over-the-counter remedies, natural approaches, or when to seek professional care (without diagnosing).
        - 📘 Offer brief explanations of how certain medicines work, typical dosage ranges, and precautions.
        - ⚖️ Always recommend users consult a licensed healthcare provider for personalized medical advice.""",
        model=OpenAIChatCompletionsModel(model="gemini-2.0-flash", openai_client=client),
    )
    # Create a runner to execute the agent
    
    user_input = input("Please describe your health concern: ")
    result = await Runner.run(
        agent,
        user_input,
    )
    print(f"Agent Response: {result.final_output}")

if __name__ == "__main__":
    asyncio.run(main())
