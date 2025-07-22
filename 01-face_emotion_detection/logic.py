from dotenv import load_dotenv
import os
import base64
from xai_sdk import Client
from xai_sdk.chat import user, image
import asyncio

load_dotenv()

api_key = os.environ.get('XAI_API_KEY')

sample_response_json = {
    'number_of_faces': 0,
    'faces': [
        {
        "emotion": "Neutral (slight smile, relaxed mouth, no strong expression; appears focused on taking the photo).",
        "position_from_left": 1,
        "bounding_box": {
            "x" :600, "y":500, "width":100, "height":150
        },
        "additional_info":"Male, adult (approx. 25-35 years old), wearing black-framed glasses. Confidence in detection: High."
        }
    ],
    'message':'to be filled in case there are no faces, else leave out this property',
    "additional_notes":"- **Overall Scene Context**: This appears to be a happy group outing (e.g., family vacation) in an outdoor setting like a park or garden at sunset. The emotions lean positive/neutral, fitting a casual selfie.- **Limitations**: Emotion detection isn't 100% accurate as it can vary by cultural context, lighting, or subtle expressions. If the image is processed with AI tools (e.g., Google Cloud Vision or Microsoft Azure Face API), results might slightly differ.  **Background/Non-Prominent Faces**: There's a small face in the background (approx. x=650, y=250, width=30, height=30) of a person sitting on a bench—emotion unclear (neutral?), but its too distant for reliable analysis. If you provide the exact image resolution or need more precise coordinates (e.g., via a tool like OpenCV), I can refine this. If you'd like me to analyze for other attributes (e.g., age, gender probabilities), let me know!"

}

def encode_image(image_path: str) -> str:
    with open(image_path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode("utf-8")
        return encoded_string
    

async def get_emotions_from_image_async(encoded_string: str):
    client = Client(api_key=os.getenv('XAI_API_KEY'))
    chat = client.chat.create(model="grok-4")
    chat.append(
        user(
            f"Detect faces in this image, tell me emotions of each face. Also give x and y axis for a face with its information. The response should be in below json format {sample_response_json}.",
            image(image_url=f"data:image/jpeg;base64,{encoded_string}", detail="high"),
        )
    )
    # Run the blocking sample() call in a thread to avoid blocking the event loop
    response = await asyncio.to_thread(chat.sample)
    print(f"Response from Grok: {response}")
    return response