class Tokenizer_Basic():
    def __init__(self, char_list: list[str]):
        self.char_list = sorted(set(char_list))
        stoi = {c: i for i, c in enumerate(self.char_list)}
        itos = {i: c for i, c in enumerate(self.char_list)}
        encode = lambda x: [stoi[c] for c in x]
        decode = lambda x: ''.join([itos[i] for i in x])