import tokenizer

# test Data
src = """
bool is_operator(char ch) {
    for (int i = 0; i < sizeof(c_operators) / sizeof(c_operators[0]); i++) {
        if (ch == c_operators[i][0]) {
            return true;
        }
        char* = "Dragon";
        str pizza = "8234e234"
        str pizza2 = 78wjdfsdf
    }
return false;
}
"""
src2 = """
x = 42S
y = 3.14
message = "Hello, World!"
"""

if __name__ == "__main__":
    tokens = tokenizer.tokenize(src2)
    for token_type, token_value, line_number in tokens:
        print(f"{token_type}: {token_value} (Line: {line_number})")