import nltk
from nltk.chat.util import Chat, reflections

pairs = [
    ["my name is (.*)", ["Hello %1!"]],
    # Add more pattern-response pairs as needed
]

chatbot = Chat(pairs, reflections)


def chat_with_user():
    print("Hello! I'm your chatbot. Type 'quit' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'quit':
            break
        response = chatbot.respond(user_input)
        print("Chatbot:", response)


chat_with_user()
