from chat_session import start_session
import argparse
import os


def parse_arguments():
    parser = argparse.ArgumentParser(
        description="Chatbot Helpdesk AI: Start a chat session and optionally save it to a file."
    )
    parser.add_argument(
        "--path",
        type=str,
        default=None,
        required=False,
        help="Path to json file to store chat session",
    )
    parser.add_argument(
        "--length",
        type=int,
        default=None,
        required=False,
        help="Length of saved to file chat session",
    )
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_arguments()
    start_session(args.path, args.length)
