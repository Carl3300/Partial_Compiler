from tokenizer import Tokenize
from code_parser import ParseCode
from semantic_analyzer import Analyze_Code

TOKEN_OPERATOR = 'OPERATOR'
TOKEN_PUNCTUATION = 'PUNCTUATION'
TEST_FILE = "./testPgms/correct/math.src"
TEST_ERROR = "./testPgms/incorrect/test2.src"

if __name__ == "__main__":
    src = open(TEST_FILE).read().splitlines()
    tokens, error = Tokenize(src)
    if error: 
        print(error)
    elif tokens.__contains__(TOKEN_OPERATOR) or tokens.__contains__(TOKEN_PUNCTUATION):
        print("Tokenization Error") 
    else:
        nodes, error = ParseCode(tokens)
        if error:
            print(error)
        else:
            correct = Analyze_Code(nodes)
            if correct:
                print("nice you did it")