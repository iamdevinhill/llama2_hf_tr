from transformers import pipeline

# Use a pipeline as a high-level helper
pipe = pipeline("text-generation", model="meta-llama/Llama-2-7b-chat-hf", use_auth_token="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")

# Define a function to interact with the chatbot
def chat_with_bot():
    print("Bot: Hello! I'm your friendly chatbot. Type 'exit' to end the conversation.")
    user_input = ""

    while user_input.lower() != "exit":
        user_input = input("You: ")
        response = pipe(user_input, max_length=100, num_return_sequences=1)[0]["generated_text"]

        print("Bot:", response)

if __name__ == "__main__":
    chat_with_bot()
