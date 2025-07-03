# Text Summarizer (Python Exercise)

This is a simple text summarization script as part of the OpenConsulting Trainee Exercise.

## Features

- Splits text into sentences
- Scores sentences based on word frequency
- Returns the top N most relevant sentences as the summary

## How to Run

## Make sure to add your own OpenAI key

### 1. Clone the repo and set up a virtual environment

```bash
python -m venv venv
venv\Scripts\activate    # On Windows
pip install -r requirements.txt

## to RUN -

python summarize.py example.txt -n 3


example.txt – your input file (can be replaced with any text)

-n 3 – number of sentences in the summary

## Dependencies

Python 3.x
nltk

note - I used Ai to help me create this, as my experiences are C++ and I dont experience using this library.