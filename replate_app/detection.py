from .API_KEY import PAT, USER_ID, APP_ID, OPENAI_API_KEY
from clarifai_grpc.channel.clarifai_channel import ClarifaiChannel
from clarifai_grpc.grpc.api import resources_pb2, service_pb2, service_pb2_grpc
from clarifai_grpc.grpc.api.status import status_code_pb2
import openai

# Create a grpc channel and stub
channel = ClarifaiChannel.get_grpc_channel()
stub = service_pb2_grpc.V2Stub(channel)

# Authorize the application using a personal access token
metadata = (('authorization', 'Key ' + PAT),)

userDataObject = resources_pb2.UserAppIDSet(user_id=USER_ID, app_id=APP_ID)

# Accept an image location then predict its tags
def get_tags(img_location):
    with open(img_location, "rb") as f:
        file_bytes = f.read()

    post_model_outputs_response = stub.PostModelOutputs(
        service_pb2.PostModelOutputsRequest(
            user_app_id=userDataObject,  # The userDataObject is created in the overview and is required when using a PAT
            # Specify for food item recognition
            model_id="food-item-recognition",
            # Input a file as a base64 coded bytestream
            inputs=[
                resources_pb2.Input(
                    data=resources_pb2.Data(
                        image=resources_pb2.Image(
                            base64=file_bytes
                        )
                    )
                )
            ]
        ),
        metadata=metadata
    )

    # Raise an exception if output fails
    if post_model_outputs_response.status.code != status_code_pb2.SUCCESS:
        print(post_model_outputs_response.status)
        raise Exception("Post model outputs failed, status: " + post_model_outputs_response.status.description)

    output = post_model_outputs_response.outputs[0]

    # Create an array of the most likely foods outputted from the clarifai API
    foodlist = []
    for concept in output.data.concepts:
        if concept.value >= 0.5:
            # If probability value is above 0.5, append the name and value as a dict to the foodlist array
            foodlist.append({"name": concept.name, "value": concept.value * 100})
    return foodlist

# A function to turn an array into a list with "and"
# E.g ["item1", "item2", "item3"] -> "item1, item2, and item3"
# For formatting before sending the information as a message to ChatGPT
def put_and_in_array(array):
    text = ""
    if len(array) > 1:
        for i in range(len(array) - 1):
            text += (f"{array[i]}, ")        
        text += ("and " + array[len(array) - 1])
        return text
    elif len(array) == 1:
        return array[0]
    else:
        return array

# Ask chatGPT on suggestions about what to do with leftover food
def ask_food_suggestions(food_array):
    openai.api_key = OPENAI_API_KEY
    messages = [
        {"role": "user", "content": "Hello!"}
    ]
    if len(food_array) > 0:
        messages.append({"role": "user", "content": f"Please give at least 3 suggestions on how we can reuse leftover {put_and_in_array([food_array])}"})
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )

    return completion.choices[0].message