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

# all keywords in C, maybe subcalssify as type, comparison, loops, return and other
keywords = [ 'auto', 'break', 'case', 'char', 'const', 'continue', 'default', 'do', 'double', 'else', 'enum', 'extern',
             'float', 'for', 'goto', 'if', 'int', 'long', 'register', 'return', 'short', 'signed', 'sizeof', 'static', 
             'struct', 'switch', 'typedef', 'union', 'unsigned', 'void', 'volatile', 'while']

# all operators in C
operators = [ '+', '-', '*', '/', '%', '<', '>', '!', '|', '^', '~', '=', '?', ':', ',', '&', '(', ')', '{', '}']

def tokenize(lines):
    tokens = []
    isString = False
    word = ''
    line_num = 0
    for line_number, line in enumerate(lines, 1):
        line_num = line_number
        for char in line:
            if isString:
                if char != '"':
                    word += char
                else:
                    word += '"'
                    tokens.append((TOKEN_LITERAL, word, line_number))
                    isString = False
                    word = ''
            elif char.isalnum() or char == '_' or char == '.':
                word += char
            else:
                if word:
                    if word in keywords:
                        tokens.append((TOKEN_KEYWORD, word, line_number))
                    else:
                        tokens.append((TOKEN_IDENTIFIER, word, line_number))
                    word = ''
                if char.isspace():    
                    continue
                if char in operators:
                    if char =='+':
                        tokens.append((TOKEN_PLUS, char, line_number))
                    elif char == '-':
                        tokens.append((TOKEN_MINUS, char, line_number))
                    elif char == '*':
                        tokens.append((TOKEN_MULTIPLY, char, line_number))
                    elif char == '/':
                        tokens.append((TOKEN_DIVIDE, char, line_number))
                    elif char == '%':
                        tokens.append((TOKEN_MOD, char, line_number))
                    elif char == '<':
                        tokens.append((TOKEN_LTHAN, char, line_number))
                    elif char == '>':
                        tokens.append((TOKEN_RTHAN, char, line_number))
                    elif char == '!':
                        tokens.append((TOKEN_NOT, char, line_number))
                    elif char == '|':
                        tokens.append((TOKEN_BOR, char, line_number))
                    elif char == '^':
                        tokens.append((TOKEN_XOR, char, line_number))
                    elif char == '~':
                        tokens.append((TOKEN_BNOT, char, line_number)) 
                    elif char == '=':
                        tokens.append((TOKEN_ASSIGN, char, line_number))
                    elif char == '?':
                        tokens.append((TOKEN_TERNARY, char, line_number)) 
                    elif char == ':':
                        tokens.append((TOKEN_COLON, char, line_number))
                    elif char == ',':
                        tokens.append((TOKEN_COMMA, char, line_number)) 
                    elif char == '&':
                        tokens.append((TOKEN_BAND, char, line_number))
                    elif char == '(':
                        tokens.append((TOKEN_LPAREN, char, line_number)) 
                    elif char == ')':
                        tokens.append((TOKEN_RPAREN, char, line_number)) 
                    elif char == '{':
                        tokens.append((TOKEN_LBRACKET, char, line_number)) 
                    elif char == '}':
                        tokens.append((TOKEN_RBRACKET, char, line_number)) 
                    word = ''
                if char == '"':
                    word += '"'
                    isString = True
        if word: #word at the end of file
            if word in keywords:
                tokens.append((TOKEN_KEYWORD, word, line_number))
            else:
                tokens.append((TOKEN_IDENTIFIER, word, line_number))
            word = ''
    realTokens = []
    tokens.append((TOKEN_EOF, '', line_num)) 
    for token in tokens:
        if token[0] == TOKEN_IDENTIFIER:
            if token[1][0].isnumeric() or token[1][0] == "-":
                token = list(token)
                token[0] = TOKEN_LITERAL
                token = tuple(token)
        realTokens.append(token)
    return realTokens