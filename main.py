import requests
import json
import os

from dotenv import load_dotenv


def main():
    load_dotenv(override=True)
    api_key = os.getenv("GEMINI_API_KEY")
    gemini_base_url = os.getenv("GEMINI_BASE_URL")

    headers = {"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"}
    payload = {
        "model": "gemini-3.1-flash-lite-preview",
        "messages": [{"role": "user", "content": "Tell me a fun fact"}],
    }

    response = requests.post(
        url=gemini_base_url,
        headers=headers,
        json=payload
    )

    print(response.json()["choices"][0]["message"]["content"])
    
if __name__ == "__main__":
    main()
