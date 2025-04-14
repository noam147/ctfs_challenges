import base64
import os
from google import genai
from google.genai import types
#OPTION1 = """Analyze the personalities of all participants in this WhatsApp group chat. Identify key traits, behavioral patterns, communication styles, and any notable social dynamics between members. Provide a summary for each user individually, if possible."""
#OPTION1 = """Analyze the personalities of all participants in this WhatsApp group chat. Identify key traits, behavioral patterns, communication styles, and any notable social dynamics between members. For each participant, output the result in a JSON object with the fields: name, traits (array of strings), and summary (string). Return the entire response as a JSON array under the key users, and include a status: success and analysis_type: group_summary at the top level."""
OPTION1 = """Analyze the personalities of all participants in this WhatsApp group chat. Identify key traits, behavioral patterns, communication styles, and any notable social dynamics between members. Provide a summary for each user individually, if possible."""
OPTION2 = """Based on the WhatsApp chat messages, analyze the personality of the user named "REPLACE". Focus on their tone, communication style, emotional expressions, habits, and how they interact with others. This should be a detailed and accurate psychological summary based solely on their messages."""
OPTION3 = """Detect and highlight any signs of conflict, arguments, passive-aggressiveness, or ghosting behavior in this WhatsApp group chat. Describe when and between whom these interactions occur, and summarize the nature of the conflict and emotional tones involved."""
OPTION4 = """Identify any sarcastic, toxic, or emotionally charged interactions in this WhatsApp group chat. Highlight specific examples with context, explain why the interaction may be considered sarcastic or toxic, and note how participants responded."""
OPTION5 = """Analyze the chat to determine which users talk the most (in terms of message volume), and which users most frequently initiate new conversations (e.g., first message after long breaks or new topics). Present findings with message counts and user names, and identify patterns if any."""
OPTIONS = [OPTION1,OPTION2,OPTION3,OPTION4,OPTION5]

current_index_for_key = 0
keys = ['AIzaSyA00mRiT8WAW32knuIOkf8aVarn8Q54_Mg','AIzaSyDBvEYzkCUkjg0beTxwpv3yHmrYPyndF2o','AIzaSyD2fqQ-ZCpyIr3YwT2Wlvi87HPt5RMSMDg','AIzaSyDin8ihdJOoB37j6VEQEahpcjpyVBlacTg']
def handle_file(file_txt:str,option:str,username:str=""):
    option = int(option)
    option -=1
    if option >= 0 and option < len(OPTIONS):
        prompt = OPTIONS[option]
        prompt += " Display your answer as HTML with great GUI!. return just the html in your response. "
        if option == 1:
            prompt = prompt.replace("REPLACE",username)#get the usrename
        try:
            print(prompt)
            result = generate(prompt,file_txt)
            if move_token(result) == True:
                return generate(prompt,file_txt)#do not do in while to not get infinte loop..
            return result
        except Exception as e:
            print(e)
            return "Error :("
    return "Error"

def list_available_models():
    try:
        # Assuming `client` is initialized as before
        client = genai.Client(api_key="AIzaSyCe0D0kQAKYS8TR4r_uhx5LKKLkC-ngx3E")

        # Call the ListModels API to get available models
        models = client.models.list()

        # Print all available models
        for model in models:
            print(model.name)

    except Exception as e:
        print(f"Error listing models: {e}")

def move_token(response) -> bool:
    global current_index_for_key
    global keys
    #func will move the api token when it exceeded with code 429
    if response.find("{'code': 429, 'message': 'You exceeded your current") != -1:
        current_index_for_key += 1
        if current_index_for_key == len(keys):
            current_index_for_key = 0
        print("moved token")
        return True#need to send again
    return False#do not need to send again
def generate(input_text, file_raw_txt):
    global current_index_for_key
    global keys
    api_key = keys[current_index_for_key]
    if not api_key:
        return "Error: GEMINI_API_KEY environment variable not set"

    client = genai.Client(api_key=api_key)

    # Prepare the content for the API call
    model = "gemini-2.5-pro-exp-03-25"
    contents = [
        types.Content(
            role="user",
            parts=[
                types.Part.from_text(text=file_raw_txt),  # Use raw file text directly
                types.Part.from_text(text=input_text),
            ],
        ),
    ]

    generate_content_config = types.GenerateContentConfig(
        response_mime_type="text/plain",
    )

    try:
        # Process the content and collect all chunks into a list
        response = client.models.generate_content_stream(
            model=model,
            contents=contents,
            config=generate_content_config,
        )

        # Extract text from each chunk
        result = ''.join([chunk.text for chunk in response])
        return result

    except Exception as e:
        print(e)
        return str(e)
        #return "Error, try again."

