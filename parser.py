# Token types
TOKEN_KEYWORD = 'KEYWORD'
TOKEN_IDENTIFIER = 'IDENTIFIER'
TOKEN_OPERATOR = 'OPERATOR'
TOKEN_LITERAL = 'LITERAL'

current_token = 0

def parse_expression(tokens):
    global current_token
    left_operand = parse_term()

    while current_token < len(tokens) and tokens[current_token][0] in (TOKEN_OPERATOR,):
        operator = tokens[current_token][1]
        current_token += 1

        right_operand = parse_term(tokens)

        if operator == '+':
            left_operand += right_operand
        elif operator == '-':
            left_operand -= right_operand

    return left_operand

def parse_term(tokens):
    global current_token
    term = tokens[current_token][1]
    current_token += 1
    return term

def parse():
    result = parse_expression()
    return result

# Parse the expression and print the result
result = parse()
print(result)