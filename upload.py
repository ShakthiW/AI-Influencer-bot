from instabot import Bot
import os
from generate_img import generate_image
from download_img import download_image

insta_pw = os.getenv("INSTA_PW")
insta_user = os.getenv("INSTA_USER")
API_KEY = os.getenv('API_KEY')

image_count = len(os.listdir("Images/"))

bot = Bot()
bot.login(username="aiarchitectural_images", password="bcshakthi123")

prompt = "A beautiful anime girl with long hair and a sword"

image_url = generate_image(API_KEY, text=prompt)
download_image(image_url, "Images/", f"image{image_count+1}")


bot.upload_photo("Images/image690.jpg", caption=f"prompt: {prompt}")

