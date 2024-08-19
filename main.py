from dotenv import load_dotenv
import os
if __name__ == "__main__":
    load_dotenv()
    print("Welcome Langchain")
    print(os.environ['COOL_API_KEY'])
