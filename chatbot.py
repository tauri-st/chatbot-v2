from openai import OpenAI
import tiktoken
import logging
import mylib

#create a module level logger to do the logging
logger = logging.getLogger(__name__)

client = OpenAI()

# accepts a preferred model and a list of messages
# makes chat completions API call
# returns the response message content
def get_api_chat_response_message(model, messages):
    # make the API call
    api_response = client.chat.completions.create(
        model = model,
        messages = messages
    )

    # extract the response text
    response_content = api_response.choices[0].message.content

    # return the response text
    return response_content

model = "gpt-3.5-turbo"

#Tell tiktoken what model used in the script with a tiktoken built-in function
encoding = tiktoken.encoding_for_model(model)

#create an array that will store the chat history
chat_history = []

user_input = ""

#TODO: Append token usage in each while loop iteration
usage = []

#Create a while loop to manage the conversation lifecycle (i.e. keep the conversation running until the user chooses to terminate it) 
#"while the conversation is running:"
while True:
    #Greet your user and ask for their name
    if (user_input == ""):
        user_input = input("Hello! Let's chat! You can type `exit` to exit out anytime. What's your name? ")
        #the model doesn't always recognize the answer as a name
        #hand it directly to the chatbot identified as the user's nameso
        user_name = f"User name is {user_input}"
        chat_history.append({
            "role": "user",
            "content": user_name
        })
    #prompt the user for input
    else:
        user_input = input("You: ")
	#if the user types “exit”, stop the loop
    if user_input.lower() == "exit":
        #TODO: Write the log
        #TODO: Include the date for reporting purposes
        #TODO: Log total token usage
        #TODO: Log output and input
        break
	
    #count the number of tokens in a prompt
    #encode() takes the prompt as an arguement and returns a list of token integers
    #these integers are like unique IDs for tokens
    #user_input_encoded = encoding.encode(user_input)
    #print(user_input_encoded)

    #Add len() function to display total number of tokens instead:
    token_count = len(encoding.encode(user_input))
    print(token_count)

    #make sure user's prompt does not exceed the maximum token limit for the model
    token_input_limit = 12289

    if (token_count > token_input_limit):
        print("Your prompt is too long. Please try again.")
        continue

    #add the user’s input in the chat history
    #*Format it like the messages dictionary for a chat completions 
    #*API call bc it's going to be sent as part of the call
    chat_history.append({
        "role": "user",
        "content": user_input
    })
    
	#make the API call
    response = get_api_chat_response_message(model, chat_history)

	#Display it to the user
    print("Chatbot: ", response)
    #Use the assistant role to give the chatbot conversation context
	    #add the message content to the chat history
    chat_history.append({
	    "role": "assistant",
	    "content": response
    })
	#*(now the loop starts over!)