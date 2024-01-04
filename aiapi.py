import openai
import config
import time

openai.api_key = config.DevelopmentConfig.OPENAI_KEY

def generateChatResponse(prompt):
    start_time = time.time()
    messages = []
    messages.append({"role": "system", "content": "You are a helpful assistant."})
    question = {}
    question['role'] = 'user'
    question['content'] = prompt
    messages.append(question)
    response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)
    
    try:
        full_answer = response['choices'][0]['message']['content']
        words = full_answer.split()  # Split the response into individual words
        formatted_answer = ' '.join(words)  # Join the words back into a string
    except:
        formatted_answer = 'Oops you beat the AI, try a different question. If the problem persists, come back later.'
    end_time = time.time()
    elapsed_time = end_time - start_time
    return formatted_answer + f" Time taken: {elapsed_time} seconds"
# import openai
# import config
# import time
 
# openai.api_key = config.DevelopmentConfig.OPENAI_KEY
 
# def generateChatResponse(prompt):
#     start_time = time.time()
#     messages = [
#         {"role": "system", "content": "You are a helpful assistant."},
#         {"role": "user", "content": prompt}
#     ]
 
#     try:
#         response = openai.Completion.create(
#             engine="davinci-codex",  # You can choose a different engine if needed
#             prompt=messages,
#             max_tokens=150
#         )
 
#         answer = response['choices'][0]['text'].replace('\n', '<br>')
#         end_time = time.time()
#         response_time = end_time - start_time
 
#         return answer + f" Response Time: {response_time} seconds."
 
#     except Exception as e:
#         print(f"Error: {e}")
#         return "Oops! An error occurred. Please try again later."