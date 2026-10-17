# Talk to an AI agent is running on external servers 


from openai import OpenAI

# Connect to Ollama running on your Mac
client = OpenAI(
    base_url="http://localhost:11434/v1",
    api_key="ollama",  # Local placeholder, not an OpenAI API key
)

# response = client.chat.completions.create(
#     model="qwen3.5:4b",
#     messages=[
#         {
#             "role": "user",
#             "content": "Hello, how are you?",
#         }
#     ],
# )

# print(response.choices[0].message.content)

# response = client.responses.create(
#     model ="qwen3.5:4b",
#     input="What is the capital of France?"
# )
# print(response.output_text)

while True:
    user_input = input("Ask your question: ")
    if user_input.lower() in ["exit", "quit", "q"]:
        break

    response = client.responses.create(
        model="qwen3.5:4b",
        input=user_input
    )

    answer = response.output_text
    answer = re.sub(r"\*\*", "", answer)

    print("AI Response: ", answer)