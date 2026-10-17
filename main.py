
import re
import time
import requests

OLLAMA_URL = "http://localhost:11434/api/chat"
MODEL = "qwen3.5:0.8b"

while True:
    user_input = input("\nAsk your question: ").strip()

    if user_input.lower() in ["exit", "quit", "q"]:
        print("Goodbye!")
        break

    if not user_input:
        continue

    start_time = time.time()

    try:
        response = requests.post(
            OLLAMA_URL,
            json={
                "model": MODEL,
                "messages": [
                    {
                        "role": "system",
                        "content": (
                            "Answer directly and concisely. "
                            "Do not reveal or output your thinking process. "
                            "For simple factual questions, answer in one or two sentences."
                        )
                    },
                    {"role": "user", "content": user_input}
                ],
                "stream": False,
                "think": False,
                "keep_alive": "30m",
                "options": {
                    "num_predict": 300,
                    "temperature": 0.2
                }
            },
            timeout=180,
        )

        response.raise_for_status()
        data = response.json()

        message = data.get("message") or {}
        answer = (message.get("content") or "").strip()

        # Remove Markdown bold markers
        answer = re.sub(r"\*\*", "", answer)

        if answer:
            print("\nAI Response:", answer)
        else:
            print("\nThe model returned an empty answer.")
            print("Finish reason:", data.get("done_reason"))
            print("Thinking length:", len(message.get("thinking") or ""))
            print("Try a model that handles this request more reliably.")

        print(f"Execution time: {time.time() - start_time:.2f} seconds")

    except requests.RequestException as error:
        print(f"Error communicating with Ollama: {error}")
