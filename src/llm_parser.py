from form import Form

from google import genai
from google.genai import types
from dotenv import load_dotenv
from typing import Union

import os
import re


load_dotenv()


class LLM_Parser:
    def __init__(self) -> None:
        self.client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
        self._init_prompt()

    def _init_prompt(self) -> None:
        try:
            base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
            data_dir = os.path.join(base_dir, "data")
            prompt_path = os.path.join(data_dir, "initial_prompt.txt")
        except Exception as e:
            raise RuntimeError(
                f"Failed to determine the path to initial_prompt.txt: {e}"
            )

        with open(prompt_path, "r") as fh:
            self.initial_prompt = fh.read()

    def call_gemini(
        self, user_prompt: str, form: Form, context: list[dict[str, dict[str, str]]]
    ) -> Union[str, any]:

        prompt = (
            self.initial_prompt
            + f"\nSession history:\n{context}\n"
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

        match = re.search(r"(\{.*?\})", response.text, re.DOTALL)
        if not match:
            raise RuntimeError("Failed to extract JSON from the Gemini response.")

        json_text = match.group(1).strip()

        return json_text
