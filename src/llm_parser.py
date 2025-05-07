from google import genai
from google.genai import types
import os
from dotenv import load_dotenv

load_dotenv()


class LLM_Parser:
    def __init__(self):
        self.context = {}
        self.client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

    def call_gemini(self):
        response = self.client.models.generate_content(
            model="gemini-2.0-flash",
            config=types.GenerateContentConfig(
                system_instruction="You are an advanced user assistance. You have to help them fill out a helpdesk form. "
            ),
            contents="Tell me a joke",
        )
