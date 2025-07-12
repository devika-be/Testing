# 📊 ReportSim - Duplicate Report Detection Using TF-IDF & Cosine Similarity

A lightweight Python tool to find similar or duplicate `.txt` reports using Natural Language Processing.

---

## 🚀 Features

- Compare a specific report with all others
- Cosine similarity scoring (0–100%)
- Clean text preprocessing (lowercasing, symbol removal)
- Export results to Excel
- CLI-based input (choose report name)
- Scales to 25+ reports easily

---

## 🧠 How It Works

1. Load and clean all `.txt` reports from a folder
2. Convert each report into a vector using **TF-IDF**
3. Ask user to enter a target report (e.g., `report12.txt`)
4. Compute **cosine similarity** with all other reports
5. Display and save a ranked similarity list

---

## 🧱 Tech Stack

- Python 3.8+
- Scikit-learn
- NumPy
- Pandas

---

## 📂 Folder Structure

project_folder/
├── report_similarity.py
├── sample_reports/
│ ├── report1.txt
│ ├── report2.txt
│ └── ...

yaml
Copy code

---

## 📥 How to Run

1. Install dependencies:
```bash
pip install numpy pandas scikit-learn
Place .txt reports inside sample_reports/ folder

Run the script:

bash
Copy code
python report_similarity.py
Enter report name when prompted:

yaml
Copy code
Enter the report filename: report12.txt

📈 Output
Terminal output: List of similar reports with % similarity

Excel export: duplicates_of_<report_name>.xlsx