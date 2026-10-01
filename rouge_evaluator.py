
import argparse
from rouge_score import rouge_scorer


def read_file(file_path):
    """Read text from a file."""
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read().strip()


def evaluate_rouge(reference_text, generated_text):
    """Calculate ROUGE-1 and ROUGE-L scores."""
    scorer = rouge_scorer.RougeScorer(
        ["rouge1", "rougeL"],
        use_stemmer=True
    )

    scores = scorer.score(
        reference_text,
        generated_text
    )

    return scores


def main():
    parser = argparse.ArgumentParser(
        description="Evaluate a machine-generated summary using ROUGE-1 and ROUGE-L."
    )

    parser.add_argument(
        "--reference",
        required=True,
        help="Path to the human-written reference summary."
    )

    parser.add_argument(
        "--generated",
        required=True,
        help="Path to the machine-generated summary."
    )

    args = parser.parse_args()

    reference_text = read_file(args.reference)
    generated_text = read_file(args.generated)

    scores = evaluate_rouge(
        reference_text,
        generated_text
    )

    print("=" * 50)
    print("ROUGE EVALUATION RESULTS")
    print("=" * 50)

    print("\nROUGE-1")
    print(f"Precision : {scores['rouge1'].precision:.4f}")
    print(f"Recall    : {scores['rouge1'].recall:.4f}")
    print(f"F1 Score  : {scores['rouge1'].fmeasure:.4f}")

    print("\nROUGE-L")
    print(f"Precision : {scores['rougeL'].precision:.4f}")
    print(f"Recall    : {scores['rougeL'].recall:.4f}")
    print(f"F1 Score  : {scores['rougeL'].fmeasure:.4f}")


if __name__ == "__main__":
    main()
