from llm_parser import LLM_Parser
from form import Form

from contextlib import contextmanager
from typing import Generator, Optional
import json


@contextmanager
def chat_session(
    save_to: Optional[str] = None, history_len: Optional[int] = None
) -> Generator[dict[str, list], None, None]:
    session = {"history": []}
    yield session
    if save_to:
        with open(save_to, "w+") as fh:
            if history_len:
                json.dump(
                    obj=session["history"][-history_len:],
                    fp=fh,
                    indent=4,
                    ensure_ascii=False,
                )
            else:
                json.dump(obj=session["history"], fp=fh, indent=4, ensure_ascii=False)


def start_session(save_to: str = None, history_len: int = None) -> None:

    with chat_session(save_to, history_len) as session:

        llm = LLM_Parser()
        form = Form()

        print("Welcome to the Helpdesk AI Assistant!")

        while not form.is_complete():
            print(f"\nCurrent form state: {form.to_json()}\n")
            user_input = input("You: ")
            response = llm.call_gemini(user_input, form, session["history"])
            try:
                response = json.loads(response)
            except json.JSONDecodeError or KeyError:
                response = {"message": "bot failed to respond to that"}

            print(f"AI: {response["message"]}")
            form.update_data(response)

            session["history"].append({user_input: response})

        print("\nForm completed:")
        print(form.to_json())
