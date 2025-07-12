import os
import re
import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

REPORT_DIR = "sample_reports"

def clean_text(text):
    text = text.lower()
    text = re.sub(r"\W+", " ", text)
    return text

def load_reports(directory):
    files = sorted([f for f in os.listdir(directory) if f.endswith(".txt")])
    texts = []
    for file in files:
        with open(os.path.join(directory, file), "r", encoding="utf-8") as f:
            texts.append(clean_text(f.read()))
    return files, texts

def main():
    filenames, texts = load_reports(REPORT_DIR)

    print("📝 Available reports:")
    for f in filenames:
        print(f" - {f}")
    
    # 🔁 Ask user to input a report name
    target_report = input("\n📥 Enter the report filename you want to check (e.g., report12.txt): ").strip()

    if target_report not in filenames:
        print(f"❌ Report '{target_report}' not found in '{REPORT_DIR}' folder.")
        return

    # TF-IDF Vectorization
    vectorizer = TfidfVectorizer(stop_words='english')
    tfidf_matrix = vectorizer.fit_transform(texts)

    # Index of target report
    target_index = filenames.index(target_report)

    # Cosine similarity of target report with all others
    similarities = cosine_similarity(tfidf_matrix[target_index], tfidf_matrix).flatten()

    # Build similarity DataFrame
    results_df = pd.DataFrame({
        "Report": filenames,
        "Similarity (%)": (similarities * 100).round(2)
    })

    # Exclude the report itself
    results_df = results_df[results_df["Report"] != target_report]
    results_df = results_df.sort_values(by="Similarity (%)", ascending=False)

    # Output
    print(f"\n📋 Similarity results for: {target_report}\n")
    print(results_df.to_string(index=False))

    # Save to Excel
    results_df.to_excel(f"duplicates_of_{target_report}.xlsx", index=False)
    print(f"\n✅ Results saved to 'duplicates_of_{target_report}.xlsx'")

if __name__ == "__main__":
    main()
