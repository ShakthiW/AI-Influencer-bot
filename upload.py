from instabot import Bot
import os

insta_pw = os.getenv("INSTA_PW")
insta_user = os.getenv("INSTA_USER")

bot = Bot()
bot.login(username=insta_user, password=insta_pw)







bot.upload_photo("yoda.jpg", caption="biscuit eating baby")

