# request-chat-completions

A minimal Python project that demonstrates how to call Google's **Gemini** models via the **OpenAI-compatible REST API** using the plain `requests` library — no SDK required.

## Overview

Instead of relying on the `openai` SDK, this project sends raw HTTP POST requests directly to Google's OpenAI-compatible Gemini endpoint. This approach is useful for understanding what happens under the hood, or in environments where installing the SDK is not desirable.

## Features

- Calls the Gemini API using only the `requests` library
- No OpenAI SDK dependency — raw HTTP requests
- Environment variable–based configuration via `.env`
- Dependency management with [uv](https://docs.astral.sh/uv/)

## Requirements

- Python 3.12+
- A [Google AI Studio](https://aistudio.google.com/) API key

## Setup

1. **Clone the repository**

   ```bash
   git clone <repo-url>
   cd request-chat-completions
   ```

2. **Install dependencies**

   Using `uv`:
   ```bash
   uv sync
   ```

   Or using `pip`:
   ```bash
   pip install requests python-dotenv
   ```

3. **Configure environment variables**

   Create a `.env` file in the project root:

   ```env
   GEMINI_API_KEY=your_google_ai_studio_api_key
   GEMINI_BASE_URL=https://generativelanguage.googleapis.com/v1beta/openai/chat/completions
   ```

   Get your API key at [aistudio.google.com](https://aistudio.google.com/apikey).

## Usage

```bash
python main.py
```

**Example output:**
```
Did you know that honey never spoils? Archaeologists have found 3,000-year-old honey in Egyptian tombs that was still perfectly edible!
```

## Project Structure

```
request-chat-completions/
├── main.py           # Entry point
├── .env              # API credentials (not committed)
├── pyproject.toml    # Project metadata and dependencies
└── README.md
```

## How It Works

The project manually builds the HTTP request with the appropriate headers and JSON payload, mirroring the OpenAI chat completions format:

```python
headers = {"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"}
payload = {
    "model": "gemini-2.0-flash",
    "messages": [{"role": "user", "content": "Tell me a fun fact"}],
}
response = requests.post(url=gemini_base_url, headers=headers, json=payload)
print(response.json()["choices"][0]["message"]["content"])
```

## Comparison with Other Approaches

| Approach | Library | Abstraction |
|---|---|---|
| `request-chat-completions` (this project) | `requests` | Raw HTTP |
| `open-ai-chat-completions` | `openai` SDK | High-level SDK |

## Notes

- The free tier has rate limits. If you hit a `RESOURCE_EXHAUSTED` error, wait a few minutes or enable billing on your Google Cloud project.
- Supported models: `gemini-2.0-flash`, `gemini-1.5-flash`, `gemini-1.5-pro`, and others listed at [ai.google.dev/gemini-api/docs/models](https://ai.google.dev/gemini-api/docs/models).
