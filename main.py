from tokenizer import tokenize, Token
from code_parser import ParseCode


test_file = "testcode1.c"

if __name__ == "__main__":
    src = open(test_file).read().splitlines()
    tokens: Token = tokenize(src)
    ParseCode(tokens)
    