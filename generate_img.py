import json
import requests
import random
from download_img import download_image

headers = {"Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiMDM1OTFiZDItNWU1MC00ZDU5LWJjYjktOGIwNWRkMzQ3YTMwIiwidHlwZSI6ImFwaV90b2tlbiJ9.-XVnRdkEajvdTpHq8TFxW8mJ2ztr1ucldc66xylY0N8"}

url = "https://api.edenai.run/v2/image/generation"
payload = {
    "providers": "replicate",
    "text": "A beautiful anime girl with long hair and a sword.",
    "response_as_dict": True,
    "attributes_as_list": False,
    "resolution": "1024x1024",
    "num_images": 1,
    "fallback_providers": "openai",
}

response = requests.post(url, json=payload, headers=headers)
result = json.loads(response.text)
# print(result['replicate']['items'])


image_count = random.randint(1, 1000)

image_url = result['replicate']['items'][0]['image_resource_url']

    
download_image(image_url, "Images/", f"image{image_count}")
