import google.generativeai as genai
import requests

# Replace with your actual API keys
GEMINI_API_KEY = "AIzaSyDV0uxsRcEhM5tlWP7TCslxAgWjO4dpIQ4"

def generate_prompt(theme):
  genai.configure(api_key=GEMINI_API_KEY)
  model = genai.GenerativeModel('gemini-pro')
  response = model.generate_content(f"You are a instagram photographer influencer that captures beautiful photos of girls. Describe how the photo should be. You can include features of the model, skin tone, hair color and any other feature. The theme for the day is {theme}")
  return response.text.split("\n")[0]