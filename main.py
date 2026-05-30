from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

import os


def main():
    print("Hello from langchain-course!")
    print(os.getenv("OPENAI_API_KEY"))


if __name__ == "__main__":
    main()
