# Token types
TOKEN_KEYWORD = 'KEYWORD'
TOKEN_IDENTIFIER = 'IDENTIFIER'
TOKEN_LITERAL = 'LITERAL'
TOKEN_EOF = 'EOF'

#TOKEN_OPERATORS
TOKEN_PLUS = 'PLUS'
TOKEN_MINUS = 'MINUS'
TOKEN_MULTIPLY = 'MULTIPLY'
TOKEN_DIVIDE = 'DIVIDE'
TOKEN_MOD = 'MOD'
TOKEN_LTHAN = 'LTHAN'
TOKEN_RTHAN = 'RTHAN'
TOKEN_NOT = 'NOT'
TOKEN_BOR = 'BOR'
TOKEN_XOR = 'XOR'
TOKEN_BNOT = 'BNOT'
TOKEN_ASSIGN = 'ASSIGN'
TOKEN_TERNARY = 'TERNARY'
TOKEN_COLON = 'COLON'
TOKEN_COMMA = 'COMMA'
TOKEN_BAND = 'BAND'
TOKEN_LPAREN = 'LPAREN'
TOKEN_RPAREN = 'RPAREN'
TOKEN_LBRACKET = 'LBRACKET'
TOKEN_RBRACKET = 'RBRACKET'


# reference operators = [ '+', '-', '*', '/', '%', '<', '>', '!', '|', '^', '~', '=', '?', ':', ',', '*', '&', '(', ')', '{', '}']
def parse(tokens):
    def get_next_token():
        if tokens:
            return tokens.pop(0)
        return None

    def parse_expr():
        return parse_term()

    def parse_term():
        node = parse_factor()

        while current_token and current_token['type'] in (TOKEN_MULTIPLY, TOKEN_DIVIDE):
            op = current_token
            consume_token()
            right = parse_factor()
            node = {'type': AST_BINOP, 'operator': op, 'left': node, 'right': right}

        return node

    def parse_factor():
        token = current_token
        if token['type'] == TOKEN_INTEGER:
            consume_token()
            return {'type': AST_INTEGER, 'value': token['value']}
        elif token['type'] == TOKEN_IDENTIFIER:
            consume_token()
            return {'type': AST_IDENTIFIER, 'name': token['value']}
        elif token['type'] == TOKEN_LPAREN:
            consume_token()
            node = parse_expr()
            if current_token['type'] == TOKEN_RPAREN:
                consume_token()
            else:
                raise SyntaxError('Expected closing parenthesis')
            return node
        else:
            raise SyntaxError('Invalid token: ' + token['type'])

    def parse_assignment():
        left = parse_factor()
        if current_token['type'] == TOKEN_ASSIGN:
            op = current_token
            consume_token()
            right = parse_expr()
            return {'type': AST_ASSIGN, 'left': left, 'operator': op, 'right': right}
        else:
            raise SyntaxError('Expected assignment operator')

    def consume_token():
        nonlocal current_token
        current_token = get_next_token()

    # Start parsing
    current_token = get_next_token()
    ast = []

    while current_token:
        if current_token['type'] in (TOKEN_IDENTIFIER, TOKEN_INTEGER):
            ast.append(parse_assignment())
        else:
            raise SyntaxError('Unexpected token: ' + current_token['type'])

    return ast