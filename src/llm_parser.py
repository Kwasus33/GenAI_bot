from google import genai
from google.genai import types
from dotenv import load_dotenv
import os
import re
import json


load_dotenv()


class LLM_Parser:
    def __init__(self):
        self.context = {}
        self.client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
        self._init_prompt()

    def _init_prompt(self):
        try:
            base_dir = os.path.dirname(os.path.abspath(__file__))
        except NameError:
            base_dir = os.path.join(os.getcwd(), "/src/")
        prompt_path = os.path.join(base_dir, "initial_prompt.txt")

        with open(prompt_path, "r") as fh:
            self.initial_prompt = fh.read()

    def _update_context(self, user_prompt, ai_response):
        self.context[user_prompt] = ai_response

    def call_gemini(self, user_prompt, form):

        prompt = (
            self.initial_prompt
            + f"\nSession Context:\n{list(self.context.items())}\n"
            + f"\nCurrent form state:\n{form.to_json()}\n"
            + f"User: {user_prompt}\n"
        )

        response = self.client.models.generate_content(
            model="gemini-2.0-flash",
            config=types.GenerateContentConfig(
                system_instruction="You are an advanced user assistance. You have to help them fill out a helpdesk form. "
            ),
            contents=prompt,
        )

        self._update_context(user_prompt, response.text)

        match = re.search(r"```json(.*?)```", response.text, re.DOTALL)
        if not match:
            raise RuntimeError("Failed to extract JSON from the Gemini response.")

        json_text = match.group(1).strip()
        cleaned_response = json.loads(json_text)

        return cleaned_response
