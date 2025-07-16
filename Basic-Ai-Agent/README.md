# 🚀 My First AI Agent Using `openai-agent-sdk` + Gemini API 🌟

This project marks my first successful attempt at creating an AI agent using the `openai-agent-sdk` and integrating it with **Google Gemini API** via OpenAI-compatible endpoints. Here's a breakdown of the code and its functionality:

---

## 📦 Importing Required Libraries

```
python
import asyncio
import os
from dotenv import load_dotenv
from openai import AsyncOpenAI
from agents import Agent, OpenAIChatCompletionsModel, Runner, set_tracing_disabled
```


- 🔄 `asyncio`: Enables asynchronous execution.
- 🔐 `os` & 🌿 `dotenv`: Load environment variables securely.
- 🤖 `AsyncOpenAI`: Client for OpenAI-compatible APIs.
- 🧠 `agents`: Core SDK components to define and run the AI agent.


---


## 🔐 Loading the Gemini API Key


```
python\nload_dotenv()
gemini_api_key = os.getenv("gemini_api_key")
```


- 🗝️ Loads your Gemini API key from a `.env` file to keep it secure and hidden.


---


## 🌐 Setting Up the Gemini Client


```
client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)
```
            
            
- 🔌 Connects to Gemini using OpenAI-compatible endpoints.
- 🧠 Enables use of Gemini models like `gemini-2.0-flash`.


---


## 🛑 Disabling Tracing (Optional)


```
python
set_tracing_disabled(disabled=True)
```


- 🧭 Turns off internal tracing/logging for cleaner output.


---


## 🧠 Creating the AI Agent


```
     agent = Agent(
    name="Assistant",
    instructions="You are a helpful assistant .",
    model=OpenAIChatCompletionsModel(model="gemini-2.0-flash", openai_client=client),
)       
```
        
        
        
- 🧑‍💼 Defines the agent named **Assistant**.
- 📜 Provides behavior instructions.
- ⚙️ Uses Gemini model via OpenAI-compatible client.

---

## 💬 Running the Agent with User Input

```
userInput = input("inter your prompt: ")
result = await Runner.run(
    agent,
    userInput,
)
print(result.final_output)
```

- 🧑‍💻 Accepts user prompt.
- 🏃‍♂️ Executes the agent using `Runner.run()`.
- 📢 Displays the final output.

---

## 🧪 Executing the Main Function

```
if __name__ == "__main__":
    asyncio.run(main())
```


- 🚀 Launches the asynchronous main function when the script is run.


---

## 📊 Summary Table

| 🔧 Component       | 💡 Description                                 |
|-------------------|------------------------------------------------|
| 🤖 Agent Name      | `Assistant`                                    |
| 🧠 Model Used      | `gemini-2.0-flash`                              |
| 🔗 API Type        | OpenAI-compatible Gemini endpoint              |
| 🛠️ SDK             | `openai-agent-sdk`                             |
| 🧪 Execution       | Asynchronous with `asyncio`                    |

---

## 🎉 Final Thoughts\n\nThis is a major milestone in my AI journey!  
I’ve successfully built an agent that:
- ✅ Uses Gemini via OpenAI-compatible endpoints
- ✅ Responds to user prompts
- ✅ Runs asynchronously
- ✅ Is ready for future enhancements

---

Would you like to add memory, tools, or a web interface next? 😎  
Let’s keep building! 💻✨