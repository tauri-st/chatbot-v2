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

#TODO: Create a while loop to manage the conversation lifecycle (i.e. keep the conversation running until the user chooses to terminate it) 
#TODO: while the conversation is running:
#TODO: prompt the user for input
	#TODO: if the user types “exit”, stop the loop
	#TODO: add the user’s input in the chat history
	#TODO: make the API call
	#TODO: extract the message content and display it to the user
    #TODO: Use the assistant role to give the chatbot conversation context
	    #add the message content to the chat history
	#*(now the loop starts over!)
  
  #TODO: Greet your user and ask for their name to personalize the conversation