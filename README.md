### Run the conversion script:

```bash
python3 run.py
```

> [!WARNING]
> Everything within this repository is in an experimental phase. Unless you know what you're doing, don't expect to come up with a fully processed dataset by using this code.

### Summarize a generated dataset

You can quickly inspect the size and composition of a generated TSV/CSV file using the helper script:

```bash
python3 analyze_dataset.py lp21/dataset-161225.csv
```

By default this prints overall counts, the date range covered, and the most frequent speakers and longest speeches.
