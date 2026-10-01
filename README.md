
# Automated Evaluation Script — ROUGE Metrics

## Problem Statement

The objective of this project is to build an automated evaluation script for measuring the quality of machine-generated summaries.

The script compares a machine-generated summary against a human-written reference summary and calculates ROUGE-1 and ROUGE-L metrics.

For the demonstration, the CNN/DailyMail dataset was used. The dataset contains news articles along with human-written reference summaries. A pretrained DistilBART summarization model was used to generate machine summaries from the articles. The generated summaries were then evaluated against their corresponding human-written summaries.

---

## Approach

The project follows this workflow:

CNN/DailyMail Article
        |
        v
Pretrained DistilBART Model
        |
        v
Machine-Generated Summary
        |
        |----------------------|
        |                      |
        v                      v
Human Reference Summary    Machine Summary
        |                      |
        |------ ROUGE ----------|
                  |
                  v
        ROUGE-1 and ROUGE-L
                  |
                  v
        Precision / Recall / F1

### Steps

1. Load articles and human-written summaries from the CNN/DailyMail dataset.
2. Generate machine summaries using the pretrained DistilBART model.
3. Use the dataset's human-written summaries as reference summaries.
4. Compare the generated summaries with their corresponding reference summaries.
5. Calculate ROUGE-1 and ROUGE-L using the `rouge-score` library.
6. Evaluate multiple samples and calculate the average F1 scores.
7. Provide a reusable command-line evaluation script that can evaluate any pair of reference and generated summary files.

---

## ROUGE Metrics

### ROUGE-1

ROUGE-1 measures the overlap of individual words (unigrams) between the generated summary and the reference summary.

### ROUGE-L

ROUGE-L measures similarity based on the Longest Common Subsequence (LCS) between the generated summary and the reference summary.

For both metrics, the evaluator reports:

- Precision
- Recall
- F1 Score

---

## Technologies Used

- Python
- `rouge-score`
- Hugging Face Transformers
- Hugging Face Datasets
- PyTorch
- CNN/DailyMail Dataset
- DistilBART (`sshleifer/distilbart-cnn-12-6`)

---

## Project Structure

```text
mentroid-ml-task6-automated-evaluation-script-rouge-metrics-Abhi/
|
├── README.md
├── requirements.txt
├── rouge_evaluator.py
├── sample_reference.txt
├── sample_generated.txt
└── results.txt
