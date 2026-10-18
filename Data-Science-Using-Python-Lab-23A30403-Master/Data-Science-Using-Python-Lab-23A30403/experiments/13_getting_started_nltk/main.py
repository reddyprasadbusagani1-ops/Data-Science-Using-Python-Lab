"""
Experiment 13: Getting Started with NLTK
Course Code: 23A30403 - Data Science Using Python Lab
"""
import nltk

def main():
    print("=== Experiment 13: Getting Started with NLTK ===")
    print(f"NLTK Library Version: {nltk.__version__}")
    
    text = "Data Science is an interdisciplinary field. Python makes NLP easy and fun!"
    print(f"\nOriginal Text:\n\"{text}\"")
    
    # Basic whitespace tokenization
    word_tokens = text.split()
    print(f"\nBasic Word Tokens (via split()):\n{word_tokens}")
    
    # Attempting NLTK word_tokenize with fallback
    try:
        nltk.data.find('tokenizers/punkt')
        from nltk.tokenize import word_tokenize, sent_tokenize
        print(f"\nNLTK Sentence Tokenization:\n{sent_tokenize(text)}")
        print(f"\nNLTK Word Tokenization:\n{word_tokenize(text)}")
    except LookupError:
        print("\nNote: NLTK 'punkt' data package not downloaded.")
        print("To download it, run in Python: import nltk; nltk.download('punkt')")

if __name__ == "__main__":
    main()
