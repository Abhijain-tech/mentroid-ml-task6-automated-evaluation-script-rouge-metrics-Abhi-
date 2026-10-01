# Automated Evaluation Script — ROUGE Metrics

## Problem Statement

The objective of this project is to build an automated evaluation script for measuring the quality of machine-generated summaries.

The script compares a machine-generated summary against a human-written reference summary and calculates ROUGE-1 and ROUGE-L metrics.

For the demonstration, the CNN/DailyMail dataset was used. The dataset contains news articles along with human-written reference summaries. A pretrained DistilBART summarization model was used to generate machine summaries from the articles. The generated summaries were then evaluated against their corresponding human-written summaries.

---

## Approach

The project follows this workflow:

```text
CNN/DailyMail Article
        |
        v
Pretrained DistilBART Model
        |
        v
Machine-Generated Summary
        |
        v
ROUGE Evaluation
        |
        v
ROUGE-1 and ROUGE-L
        |
        v
Precision / Recall / F1

```
## Steps
1. Load articles and human-written summaries from the CNN/DailyMail dataset.
2. Generate machine summaries using the pretrained DistilBART model.
3. Use the dataset's human-written summaries as reference summaries.
4. Compare the generated summaries with their corresponding reference summaries.
5. Calculate ROUGE-1 and ROUGE-L using the `rouge-score` library.
6. Evaluate multiple samples and calculate the average F1 scores.
7. Provide a reusable command-line evaluation script that can evaluate any pair of reference and generated summary files.

## Technologies Used
- Python
- `rouge-score`
- Hugging Face Transformers
- Hugging Face Datasets
- PyTorch
- CNN/DailyMail Dataset
- DistilBART (`sshleifer/distilbart-cnn-12-6`)

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
```


## Setup

### Clone the Repository

```bash
git clone https://github.com/Abhijain-tech/mentroid-ml-task6-automated-evaluation-script-rouge-metrics-Abhi.git
cd mentroid-ml-task6-automated-evaluation-script-rouge-metrics-Abhi
```
### Install Dependencies
```bash
pip install -r requirements.txt
```



## How to Run

The evaluation script accepts two input files:

- `--reference`: path to the human-written reference summary
- `--generated`: path to the machine-generated summary

### Run the Evaluator

```bash
python rouge_evaluator.py --reference sample_reference.txt --generated sample_generated.txt
```
The script prints:

- ROUGE-1 Precision
- ROUGE-1 Recall
- ROUGE-1 F1
- ROUGE-L Precision
- ROUGE-L Recall
- ROUGE-L F1



## Demonstration Results

The evaluator was tested on 5 samples from the CNN/DailyMail dataset.

### Individual Results

| Sample | ROUGE-1 F1 | ROUGE-L F1 |
| ------ | ---------- | ---------- |
| 1      | 0.5352     | 0.4789     |
| 2      | 0.5053     | 0.4421     |
| 3      | 0.2824     | 0.2118     |
| 4      | 0.3750     | 0.3000     |
| 5      | 0.6301     | 0.2740     |

### Average Results

| Metric  | Average F1 Score |
| ------- | ---------------- |
| ROUGE-1 | 0.4656           |
| ROUGE-L | 0.3413           |


## Important Note
The CNN/DailyMail dataset and DistilBART model were used only for demonstrating and validating the evaluation workflow.

The final rouge_evaluator.py script is independent of the dataset and summarization model. It accepts any human-written reference summary and machine-generated summary as input files and calculates ROUGE-1 and ROUGE-L scores.

## Author
**Abhi Jain**

B.Tech — Artificial Intelligence & Robotics

Email: jainabhi1903@gmail.com

