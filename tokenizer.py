# Token types
TOKEN_KEYWORD = 'KEYWORD'
TOKEN_IDENTIFIER = 'IDENTIFIER'
TOKEN_OPERATOR = 'OPERATOR'
TOKEN_LITERAL = 'LITERAL'

# all keywords in C
keywords = [ 'auto', 'break', 'case', 'char', 'const', 'continue', 'default', 'do', 'double', 'else', 'enum', 'extern',
             'float', 'for', 'goto', 'if', 'int', 'long', 'register', 'return', 'short', 'signed', 'sizeof', 'static', 
             'struct', 'switch', 'typedef', 'union', 'unsigned', 'void', 'volatile', 'while']

# all operators in C
operators = [ '+', '-', '*', '/', '%', '<', '>', '!', '|', '^', '~', '=', '?', ':', ',', '*', '&', '(', ')', '{', '}']

def tokenize(source_code):
    tokens = []
    realTokens = []
    lines = source_code.split('\n')
    isString = False
    for line_number, line in enumerate(lines, 1):
        word = ''
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
                    tokens.append((TOKEN_OPERATOR, char, line_number))
                if char == '"':
                    word += '"'
                    isString = True
        # needed if there is word at end of line
        if word:
            if word in keywords:
                tokens.append((TOKEN_KEYWORD, word, line_number))
            else:
                tokens.append((TOKEN_IDENTIFIER, word, line_number))
    # cant think of better way to filter without a bunch of bools
    for token in tokens:
        if token[0] == TOKEN_IDENTIFIER:
            if token[1][0].isnumeric() or token[1][0] == "-":
                token = list(token)
                token[0] = TOKEN_LITERAL
                token = tuple(token)
        realTokens.append(token)
    return realTokens