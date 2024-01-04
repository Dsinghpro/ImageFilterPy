import openai
import config
 
openai.api_key = config.DevelopmentConfig.OPENAI_KEY
 
def generate_chat_response(prompt):
    try:
        response = openai.Completion.create(
            engine="davinci-codex",
            prompt=prompt,
            max_tokens=150
        )
 
        answer = response['choices'][0]['text'].replace('\n', '<br>')
        return answer
 
    except Exception as e:
        print(f"Error: {e}")
        return "Oops! An error occurred. Please try again later."
 
def chat_with_bot():
    print("Welcome to the ChatGPT Bot!")
    print("You can start chatting. Type 'exit' to end the conversation.")
 
    conversation_history = []
 
    while True:
        user_input = input("You: ")
 
        if user_input.lower() == 'exit':
            print("ChatGPT Bot: Goodbye!")
            break
 
        # Update the conversation history
        conversation_history.append({"role": "user", "content": user_input})
 
        # Generate a response from the chatbot
        bot_response = generate_chat_response(conversation_history)
 
        # Display the bot's response
        print("ChatGPT Bot:", bot_response)
 
        # Update the conversation history with the bot's response
        conversation_history.append({"role": "assistant", "content": bot_response})
 
if __name__ == "__main__":
    chat_with_bot()