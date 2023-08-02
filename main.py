from tokenizer import tokenize, Token
from code_parser import ParseCode

TOKEN_OPERATOR = 'OPERATOR'
TOKEN_PUNCTUATION = 'PUNCTUATION'
TEST_FILE = "./testPgms/correct/math.src"

if __name__ == "__main__":
    src = open(TEST_FILE).read().splitlines()
    tokens, error = tokenize(src)
    val = tokens.__contains__(TOKEN_OPERATOR)
    if error: 
        print(error)
    elif tokens.__contains__(TOKEN_OPERATOR) or tokens.__contains__(TOKEN_PUNCTUATION):
        print("Tokenization Error") 
    else:
        nodes, error = ParseCode(tokens)
        if error:
            print(error)
        else:
            print(nodes)