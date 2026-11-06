# Clinical Notes Translator

A simple Streamlit application that uses Google's Gemini API to rewrite clinical notes in clear, patient-friendly language.

The goal is to make medical wording easier to understand while keeping the original clinical meaning intact.

## What It Does

- Accepts a clinical note through a Streamlit interface.
- Sends the note to Gemini using Google's OpenAI-compatible API endpoint.
- Explains medical terms in simple, everyday language.
- Organizes the explanation into relevant sections when the information is available:
  - Reason for Visit
  - Tests and Checks
  - Results
  - Next Steps
- Preserves medication names, doses, measurements, dates, numbers, and uncertainty.
- Identifies input that is unrelated to clinical notes.
- Displays the original note alongside the patient-friendly explanation.

## Tech Stack

- Python
- Streamlit
- Google Gemini API
- OpenAI Python SDK (Gemini-compatible endpoint)
- python-dotenv

## Project Structure

```text
Clinical-Notes-Translator/
├── main.py
├── LLM_Calling.py
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
```

## How It Works

1. The user enters a clinical note in the Streamlit application.
2. The application checks that the input is not empty.
3. The note and system instructions are sent to the configured Gemini model.
4. Gemini rewrites the note using simple language while following the prompt's safety and accuracy rules.
5. The application displays the original note and the generated explanation.

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/duaajaved321/Medical-Jargon-Translator-Streamlit-LLM-API-.git
cd Medical-Jargon-Translator-Streamlit-LLM-API-
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate it:

**Windows PowerShell**
```powershell
venv\Scripts\Activate.ps1
```

**Windows Command Prompt**
```cmd
venv\Scripts\activate
```

**macOS / Linux**
```bash
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure the Gemini API key

Create a file named `.env` in the project root. Copy the values from `.env.example` and add your Gemini API key:

```env
GEMINI_API_KEY=your_gemini_api_key_here
GEMINI_MODEL=gemini-3.8-flash
```

Get an API key from [Google AI Studio](https://aistudio.google.com/app/apikey).

Keep your API key private. The `.env` file is excluded from Git through `.gitignore`; never commit it or share it publicly.

### 5. Run the application

```bash
streamlit run main.py
```

Streamlit will display a local URL in the terminal. Open that URL in your browser to use the application.

## Example

**Input**

```text
Patient presents with hypertension and reports mild dyspnea on exertion.
```

**Illustrative output**

```text
Reason for Visit
- The patient has high blood pressure.
- The patient reports mild shortness of breath during physical activity.
```

This is an illustrative example. Actual wording depends on the note and the model response.

## Configuration

The model is configurable through the `GEMINI_MODEL` variable in your `.env` file. If it is not set, the application uses the default model defined in `LLM_Calling.py`.

## Error Handling

The application handles common API issues, including:

- Missing API key
- Invalid or unauthorized API key
- API quota and rate-limit errors
- Connection errors
- API request failures
- Empty model responses

## Limitations and Responsible Use

- This is an educational/demo application, not a medical device.
- It does not diagnose medical conditions or recommend treatment.
- AI-generated explanations may be incomplete or incorrect. Always compare the output with the original clinical note.
- Do not enter real patient information or identifiable health data unless you have the required authorization, consent, and a compliant environment.
- The entered note is sent to Google's Gemini API for processing. Review Google's applicable privacy and data-handling terms before using the application with sensitive information.

## Future Improvements

- Add support for multiple languages.
- Add automated tests for prompt and API response handling.
- Add an option to download the translated explanation.
- Improve response formatting and validation.

## Author

**Dua Javed**
