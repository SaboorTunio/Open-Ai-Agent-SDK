# 💊 Smart Pharmacy Agent

## 📝 Overview

This project features an AI-powered agent that helps users with medicine guidance based on their symptoms. It uses Google's Gemini API and OpenAI's async client to deliver suggestions, explanations, and safety reminders.

---

## ✨ Features

- 🧠 **Symptom Understanding:** Asks follow-up questions to clarify user symptoms.
- 💡 **Product Suggestions:** Recommends over-the-counter remedies, natural approaches, and advises when to seek professional care.
- 📘 **Medicine Information:** Provides brief explanations of medicines, typical dosages, and precautions.
- ⚖️ **Safety First:** Reminds users to consult licensed healthcare providers for personalized advice.

---

## ⚙️ How It Works — Step by Step


Below is the main code for the Smart Pharmacy Agent, with each step explained inline:

---
## Import All Modules

```python
import asyncio
import os
from dotenv import load_dotenv
from openai import AsyncOpenAI
from agents import Agent, OpenAIChatCompletionsModel, Runner, set_tracing_disabled
```

---

## 1️⃣ Load environment variables from .env file

```
load_dotenv()
gemini_api_key = os.getenv("GEMINI_API_KEY")
```

---

## 2️⃣ Check if the API key is present

```
if not gemini_api_key:
    raise EnvironmentError("GEMINI_API_KEY not found in environment variables.")
```

---


## 3️⃣ Initialize the OpenAI client for Gemini API

```
client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)
```
---

# 4️⃣ Disable tracing for cleaner operation
```
set_tracing_disabled(disabled=True)
```
---
## 5️⃣ Set up the agent with instructions for medicine guidance and safety
```
async def main():
    agent = Agent(
        name="ProductSuggester",
        instructions="""You're an AI agent designed to provide helpful guidance about medicines based on symptoms shared by users. When a user describes a health concern, such as saying “I have a headache,” your role is to:
        - 🧠 Understand the symptom clearly and ask follow-up questions if needed.
        - 💊 Suggest commonly known over-the-counter remedies, natural approaches, or when to seek professional care (without diagnosing).
        - 📘 Offer brief explanations of how certain medicines work, typical dosage ranges, and precautions.
        - ⚖️ Always recommend users consult a licensed healthcare provider for personalized medical advice.""",
        model=OpenAIChatCompletionsModel(model="gemini-2.0-flash", openai_client=client),
    )
``` 
---   
## 6️⃣ Prompt the user for their health concern
```    
    user_input = input("Please describe your health concern: ")
```
---    
## 7️⃣ Run the agent and print the response
```    
    result = await Runner.run(
        agent,
        user_input,
    )
    print(f"Agent Response: {result.final_output}")

if __name__ == "__main__":
    asyncio.run(main())
```
