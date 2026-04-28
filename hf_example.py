"""
hf_example.py - Stream a sample of a waste-classification dataset from Hugging Face Hub.

HOW TO RUN:
    pip install datasets
    python3 hf_example.py

Requires Python 3.8+. No API key or account needed.
"""

from datasets import load_dataset  # type: ignore[import-untyped]


def fetch_dataset_from_huggingface():
    """Stream a small sample of a waste-management dataset from the Hugging Face Hub.

    Information structure: Tabular dataset (image classification labels)
    Access technology:     Hugging Face `datasets` library (streaming, no full download)

    PROS:
      - Streaming avoids downloading the full dataset; only fetches what you use.
      - Simple one-line access via the datasets library.
      - Dataset is versioned on HF Hub for reproducibility.
    CONS:
      - Requires installing the datasets library (heavyweight dependency).
      - Streaming datasets don't support random access or shuffling easily.
      - Dependent on Hugging Face's infrastructure being available.
    """
    print("Streaming dataset sample from Hugging Face...")
    dataset = load_dataset(
        "omasteam/waste-garbage-management-dataset",
        split="train",
        streaming=True,
    )

    label_names = dataset.features["label"].names
    print(f"Dataset has {len(label_names)} waste categories: {label_names}")

    sample = list(dataset.take(10))
    print("\nFirst 10 records:")
    for i, record in enumerate(sample, start=1):
        print(f"  record {i}: label {record['label']} -> {label_names[record['label']]}")


if __name__ == "__main__":
    fetch_dataset_from_huggingface()
