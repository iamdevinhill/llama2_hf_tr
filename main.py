# Import the required function from the Hugging Face Transformers library
from transformers import pipeline

# Create a text generation pipeline using a specific pre-trained model
pipe = pipeline("text-generation", model="meta-llama/Llama-2-7b-chat-hf", use_auth_token="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")

# Define a function to interact with the chatbot
def chat_with_bot():
    # Print a welcome message from the bot and provide instructions
    print("Bot: Hello! I'm your friendly chatbot. Type 'exit' to end the conversation.")
    user_input = ""  # Initialize a variable to store user input

    # Start a loop that continues until the user types 'exit'
    while user_input.lower() != "exit":
        user_input = input("You: ")  # Prompt the user to input a message
        # Generate a response from the chatbot based on the user's input
        response = pipe(user_input, max_length=100, num_return_sequences=1)[0]["generated_text"]

        print("Bot:", response)  # Display the generated response from the bot

# Entry point of the script
if __name__ == "__main__":
    chat_with_bot()  # Call the function to start the chatbot interaction

