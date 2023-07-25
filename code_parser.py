# Token types
TOKEN_KEYWORD = 'KEYWORD'
TOKEN_IDENTIFIER = 'IDENTIFIER'
TOKEN_OPERATOR = 'OPERATOR'
TOKEN_LITERAL = 'LITERAL'

curr = 0

def parse_expression(tokens):
    global curr
    left_operand = parse_term(tokens)

    while curr < len(tokens) and tokens[curr][0] in (TOKEN_OPERATOR,):
        operator = tokens[curr][1]
        curr += 1

        right_operand = parse_term(tokens)

        if operator == '+':
            left_operand += right_operand
        elif operator == '-':
            left_operand -= right_operand
    return left_operand

def parse_term(tokens):
    global curr
    term = tokens[curr][1]
    curr += 1
    return term