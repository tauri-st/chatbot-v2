from openai import OpenAI

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

#TODO: create an array that will store the chat history
chat_history = []

user_input = ""

#TODO: Create a while loop to manage the conversation lifecycle (i.e. keep the conversation running until the user chooses to terminate it) 
#TODO: while the conversation is running:
while True:
    #TODO: Greet your user and ask for their name
    if (user_input == ""):
        user_input = input("Hello! Let's chat! You can type `exit` to exit out anytime. What's your name? ")
        #the model doesn't always recognize the answer as a name
        #hand it directly to the chatbot identified as the user's nameso
        user_name = f"User name is {user_input}"
        chat_history.append({
            "role": "user",
            "content": user_name
        })
    #TODO: prompt the user for input
    else:
        user_input = input("You: ")
	#TODO: if the user types “exit”, stop the loop
    if user_input.lower() == "exit":
        break
	#TODO: add the user’s input in the chat history
    #*Format it like the messages dictionary for a chat completions 
    #*API call bc it's going to be sent as part of the call
    chat_history.append({
        "role": "user",
        "content": user_input
    })
    
	#TODO: make the API call
    response = get_api_chat_response_message(model, chat_history)

	#TODO: Display it to the user
    print("Chatbot: ", response)
    #TODO: Use the assistant role to give the chatbot conversation context
	    #add the message content to the chat history
    chat_history.append({
	    "role": "assistant",
	    "content": response
    })
	#*(now the loop starts over!)