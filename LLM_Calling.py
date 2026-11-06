"""Gemini-powered clinical note translation.

The application uses Google's Gemini API through its OpenAI-compatible endpoint.
"""

import os

from dotenv import load_dotenv
from openai import (
    APIConnectionError,
    APIStatusError,
    AuthenticationError,
    OpenAI,
    RateLimitError,
)

load_dotenv()

GEMINI_BASE_URL = "https://generativelanguage.googleapis.com/v1beta/openai/"
DEFAULT_MODEL = "gemini-3.8-flash"

SYSTEM_PROMPT = """
You are a careful medical communication assistant. Your task is to rewrite
clinical notes into clear, simple, patient-friendly language.

First decide whether the user's message is a clinical note or contains
clinical information that can reasonably be explained.

If it is unrelated to a clinical note, reply with exactly:
Irrelevant prompt

For a clinical note, follow these rules:
- Preserve the original meaning and all clinically relevant details.
- Explain medical terms in simple, everyday language.
- Do not add facts, symptoms, test results, diagnoses, or context that are
  not explicitly present in the note.
- Do not diagnose, recommend treatment, or give medical advice.
- Keep medication names, doses, measurements, dates, and numbers accurate.
- Preserve uncertainty. Do not turn a possibility into a confirmed fact.
- If the source is incomplete or unclear, say so rather than guessing.
- Use a calm, respectful, easy-to-understand tone.

Use the following sections only when the information is present:
1. Reason for Visit
   Explain why the patient came in and which symptoms or concerns were reported.
2. Tests and Checks
   Mention examinations, tests, measurements, or investigations in the note.
   Explain their purpose only when that purpose is clear.
3. Results
   Explain recorded results without changing their meaning.
4. Next Steps
   Include only follow-up, medication instructions, referrals, or next actions
   explicitly written in the note.

Omit sections that are not supported by the note. Use clear headings and
short bullet points. Do not include a diagnosis or treatment recommendation.
"""


def translate_clinical_notes(note: str) -> str:
    """Translate a clinical note using the Gemini API.

    Args:
        note: The clinical note entered by the user.

    Returns:
        A patient-friendly explanation, or a readable error message.
    """
    if not isinstance(note, str) or not note.strip():
        return "Error: Please enter a clinical note."

    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        return "Error: GEMINI_API_KEY is not configured. Add it to your .env file."

    model = os.getenv("GEMINI_MODEL", DEFAULT_MODEL)

    try:
        client = OpenAI(
            api_key=api_key,
            base_url=GEMINI_BASE_URL,
        )

        response = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": note.strip()},
            ],
        )

        content = response.choices[0].message.content
        if not content or not content.strip():
            return "Error: The model returned an empty response."

        return content.strip()

    except AuthenticationError:
        return "Error: The Gemini API key is invalid or unauthorized."
    except RateLimitError:
        return "Error: API quota or rate limit exceeded. Please try again later."
    except APIConnectionError:
        return "Error: Could not connect to the Gemini API. Check your internet connection."
    except APIStatusError as error:
        return (
            f"Error: Gemini API request failed (HTTP {error.status_code}). "
            "Please check the model name and API configuration."
        )
    except Exception:
        # Avoid exposing API keys, request payloads, or internal details in the UI.
        return "Error: An unexpected problem occurred while translating the note."


if __name__ == "__main__":
    sample_note = (
        "Patient presents with hypertension and reports "
        "mild dyspnea on exertion."
    )
    print(translate_clinical_notes(sample_note))
