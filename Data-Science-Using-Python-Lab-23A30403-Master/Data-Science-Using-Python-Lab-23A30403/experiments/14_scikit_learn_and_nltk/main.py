"""
Experiment 14: Scikit-learn and NLTK
Course Code: 23A30403 - Data Science Using Python Lab
"""
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

def simple_tokenize(text):
    return text.lower().split()

def main():
    print("=== Experiment 14: Sentiment Classifier using Scikit-Learn & NLTK Concepts ===")
    
    train_texts = [
        "Python is fantastic and easy to learn",
        "Data science project execution was a great success",
        "This code has bugs and fails repeatedly",
        "Terrible experience, very poor performance",
        "Excellent algorithm and smooth performance",
        "Bad execution, complete failure"
    ]
    train_labels = ["Positive", "Positive", "Negative", "Negative", "Positive", "Negative"]
    
    # Vectorizer with custom tokenizer
    vectorizer = CountVectorizer(tokenizer=simple_tokenize, token_pattern=None)
    X_train = vectorizer.fit_transform(train_texts)
    
    clf = MultinomialNB()
    clf.fit(X_train, train_labels)
    
    test_sample = ["Python performance is excellent and fantastic"]
    X_test = vectorizer.transform(test_sample)
    prediction = clf.predict(X_test)[0]
    
    print(f"Sample Sentence: \"{test_sample[0]}\"")
    print(f"Predicted Sentiment Label: {prediction}")

if __name__ == "__main__":
    main()
