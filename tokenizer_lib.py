class Tokenizer_Basic():
    def __init__(self, char_list: list[str]):
        self.char_list = sorted(set(char_list))
        self.stoi = {c: i for i, c in enumerate(self.char_list)}
        self.itos = {i: c for i, c in enumerate(self.char_list)}

    def encode(self, text: str) -> list[int]:
        return [self.stoi[c] for c in text]

    def decode(self, ids: list[int]) -> str:
        return "".join(self.itos[i] for i in ids)