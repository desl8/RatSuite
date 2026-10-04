from tokenizer_lib import Tokenizer_Basic

fname = "wikitext-2-raw-v1.txt"

with open(fname, "r", encoding="utf-8") as f:
    raw_text = f.read()

tokenizer = Tokenizer_Basic(sorted(list(set(raw_text))))

encoded_text = tokenizer.encode(raw_text)
print(f"encoded length: {len(encoded_text)}")
print("First 50 encoded tokens:")
print(encoded_text[:50])

decoded_text = tokenizer.decode(encoded_text) # for testing purposes
print("First 50 decoded characters:")
print(decoded_text[:50])