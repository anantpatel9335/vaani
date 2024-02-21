import random

# Define a function to generate responses
def vaani_response(user_input):
    responses = [
        "Hello! How can I help you today?",
        "I'm here to chat. What's on your mind?",
        "Tell me more about how you're feeling.",
        "Is there anything specific you'd like to talk about?"
    ]
    return random.choice(responses)

# Main function to handle the conversation
def main():
    print("Welcome to Vaani - Your Personal Chat Assistant")
    print("Type 'exit' to end the conversation.")

    while True:
        user_input = input("You: ")
        user_input = user_input.lower()

        if user_input == 'exit':
            print("Goodbye! Take care.")
            break
        else:
            response = vaani_response(user_input)
            print("Vaani:", response)

# Call the main function to start the conversation
if __name__ == "__main__":
    main()
