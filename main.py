import tokenizer
import code_parser

test_file = "testcode.c"

if __name__ == "__main__":
    src = open(test_file).read().splitlines()
    tokens = tokenizer.tokenize(src)
    #res = code_parser.parse_expression(tokens)
    #print(res)
    for token_type, token_value, line_number in tokens:
        print(f"{token_type}: {token_value} (Line: {line_number})")
    