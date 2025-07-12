import os
import re
import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# 🔁 CHANGE THIS if your folder is in a different location
REPORT_DIR = "sample_reports"  # Folder with .txt reports

# 🧼 Text cleaning function
def clean_text(text):
    text = text.lower()
    text = re.sub(r"\W+", " ", text)  # Remove special characters
    return text

# 📥 Load and clean all reports
def load_reports(directory):
    files = sorted([f for f in os.listdir(directory) if f.endswith(".txt")])
    texts = []
    for file in files:
        with open(os.path.join(directory, file), "r", encoding="utf-8") as f:
            texts.append(clean_text(f.read()))
    return files, texts

# 🚀 Main function
def main():
    filenames, texts = load_reports(REPORT_DIR)

    # 🔢 Convert text to TF-IDF vectors
    vectorizer = TfidfVectorizer(stop_words='english')
    tfidf_matrix = vectorizer.fit_transform(texts)

    # 📐 Cosine similarity matrix
    similarity_matrix = cosine_similarity(tfidf_matrix)

    # 📊 Convert to DataFrame for better viewing
    df = pd.DataFrame(similarity_matrix, index=filenames, columns=filenames)
    df = (df * 100).round(2)  # Convert to percentage

    print("\n📊 Cosine Similarity Matrix (%):\n")
    print(df.to_string())

    # 💾 Save to Excel
    df.to_excel("cosine_similarity_matrix.xlsx")
    print("\n✅ Matrix saved to 'cosine_similarity_matrix.xlsx'")

if __name__ == "__main__":
    main()
