from instabot import Bot
import os
from generate_img import generate_image
from download_img import download_image
from generate_prompt import generate_prompt

# Delete config file

os.popen("rm -rf config")

insta_pw = os.getenv("INSTA_PW")
insta_user = os.getenv("INSTA_USER")
API_KEY = os.getenv('API_KEY')

image_count = len(os.listdir("Images/"))

theme = "City life"
prompt = generate_prompt(theme)
print(f"Generated prompt: {prompt}")

# prompt = "A beautiful anime girl with long hair"
image_url = generate_image("eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiMDM1OTFiZDItNWU1MC00ZDU5LWJjYjktOGIwNWRkMzQ3YTMwIiwidHlwZSI6ImFwaV90b2tlbiJ9.-XVnRdkEajvdTpHq8TFxW8mJ2ztr1ucldc66xylY0N8", text=prompt)
download_image(image_url, "Images/", f"image{image_count+1}")

file_path = f"Images/image{image_count+1}.jpeg"


bot = Bot()
bot.login(username="aiarchitectural_images", password="bcshakthi123")


bot.upload_photo(file_path, caption=f"prompt: {prompt}")

