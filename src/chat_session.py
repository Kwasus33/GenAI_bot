from llm_parser import LLM_Parser
from form import Form


def start_session():
    llm = LLM_Parser()
    form = Form()

    print("Welcome to the Helpdesk AI Assistant!")

    while not form.is_complete():
        print(f"\nCurrent form state: {form.to_json()}\n")
        user_input = input("You: ")
        response = llm.call_gemini(user_input, form)
        print(f"AI: {response}")
        form.update_data(response)

    print("\nForm completed:")
    print(form.to_json())
