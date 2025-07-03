import re
import argparse
import openai
from nltk.corpus import stopwords
from collections import defaultdict

# Replace this with your OpenAI key
#
openai.api_key = "ADD YOUR KEY HERE"
#
#--------------------------------------------------

def sent_tokenize(text):
    return re.split(r'(?<=[.!?])\s+', text.strip())

def word_tokenize(text):
    return re.findall(r'\b\w+\b', text.lower())

def summarize(text, num_sentences=3):
    sentences = sent_tokenize(text)
    stop_words = set(stopwords.words("english"))

    word_freq = defaultdict(int)
    for sent in sentences:
        for word in word_tokenize(sent):
            if word not in stop_words:
                word_freq[word] += 1

    sentence_scores = {}
    for sent in sentences:
        score = sum(word_freq.get(word, 0) for word in word_tokenize(sent))
        sentence_scores[sent] = score

    top_sentences = sorted(sentence_scores, key=sentence_scores.get, reverse=True)[:num_sentences]
    return "\n".join(top_sentences)

# Function for ton generation
#
def rephrase_with_tone(text, tone):
    prompt = f"""
Rephrase the following summary in a {tone} tone:

\"\"\"{text}\"\"\"
"""
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.8
        )
        return response.choices[0].message['content'].strip()
    except Exception as e:
        return f"[Error contacting AI: {str(e)}]"
#
#-----------------------------------------------



def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("file", help="Text file to summarize")
    parser.add_argument("-n", type=int, default=3, help="Number of sentences in summary")
    
    #--- Parsing tone generation
    parser.add_argument("--tone", type=str, help="Optional tone to rephrase the summary (e.g., casual, pirate-speak, Shakespearean)")
    args = parser.parse_args()

    with open(args.file, "r", encoding="utf-8") as f:
        text = f.read()

    summary = summarize(text, args.n)
    print("\nSummary:\n", summary)

    if args.tone:
        rephrased = rephrase_with_tone(summary, args.tone)
        print(f"\nRephrased in '{args.tone}' tone:\n", rephrased)

if __name__ == "__main__":
    main()
