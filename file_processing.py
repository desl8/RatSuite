from datasets import load_dataset
import json

with open("config.json", "r", encoding="utf-8") as f:
    config = json.load(f)

ds = load_dataset(config["dataset_name"], config["dataset_version"])

train_split = ds["train"]

raw = "".join(train_split["text"])

print(f"characters: {len(raw)}")          # total characters
print("First 500 chars:")
print(raw[:500])        # preview instead of dumping millions of chars

fname = config["output_file"]

with open(fname, "w", encoding="utf-8") as f:
    f.write(raw)