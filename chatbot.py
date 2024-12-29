import openai
import os
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("API_KEY")

if not openai.api_key:
    print("API key is missing. Please make sure it's set in your environment.")
    exit()

def chat_with_gpt():
    print("Chatbot: Hello! How can I assist you today? (Type 'exit' to end the chat)")

    conversation = [{"role": "system", "content": "You are a helpful assistant."}]

    while True:
        user_input = input("You: ")

        if user_input.lower() in ["exit", "quit", "bye"]:
            print("Chatbot: Goodbye! Have a great day!")
            break

        conversation.append({"role": "user", "content": user_input})

        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",  
                messages=conversation,
                temperature=0.7,
                max_tokens=150
            )

    
            bot_reply = response['choices'][0]['message']['content']
            print(f"Chatbot: {bot_reply}")

        
            conversation.append({"role": "assistant", "content": bot_reply})

        except openai.OpenAIError as e:  
            print(f"Chatbot: Oops! Something went wrong: {e}")


if __name__ == "__main__":
    chat_with_gpt()
