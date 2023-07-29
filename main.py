from tokenizer import tokenize, Token
from code_parser import ParseCode


test_file = "testcode1.txt"

if __name__ == "__main__":
    src = open(test_file).read().splitlines()
    tokens, error = tokenize(src)
    if error: 
        print(error)
    else:
        nodes, error = ParseCode(tokens)
        if error:
            print(error)
        else:
            print(nodes)