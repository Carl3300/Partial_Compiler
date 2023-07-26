# Token types
TOKEN_KEYWORD = 'KEYWORD'
TOKEN_IDENTIFIER = 'IDENTIFIER'
TOKEN_TYPE = 'TYPE'
TOKEN_OPERATOR = 'OPERATOR'
TOKEN_PUNCTUATION = 'PUNCTUATION'
TOKEN_EOF = 'EOF'

# C Operators
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

# C Punctuation
TOKEN_SEMI = 'SEMI'
TOKEN_COMMA = 'COMMA'
TOKEN_BAND = 'BAND'
TOKEN_LPAREN = 'LPAREN'
TOKEN_RPAREN = 'RPAREN'
TOKEN_LBRACKET = 'LBRACKET'
TOKEN_RBRACKET = 'RBRACKET'

# C Type Literals
TOKEN_INTLITERAL = 'INTLITERAL'
TOKEN_FLOATLITERAL = 'FLOATLITERAL'
TOKEN_STRLITERAL = 'STRLITERAL'
TOKEN_CHARLITERAL = 'CHARLITERAL'

# C Types
TOKEN_AUTO = 'AUTO'
TOKEN_STRUCT = 'STRUCT'
TOKEN_VOID = 'VOID'

# C Keywords
keywords = [ 'break', 'case', 'const', 'continue', 'default', 'do', 'else', 'enum', 'extern',
             'for', 'printf', 'goto', 'if', 'register', 'return', 'signed', 'sizeof', 'static', 
             'switch', 'typedef', 'union', 'unsigned', 'volatile', 'while']

# C Types
types = [ 'auto', 'char', 'double', 'float', 'int', 'short', 'long', 'struct', 'void']

# C Operators
operators = [ '+', '-', '*', '/', '%','=', '+=', '=+', "-=", "=-", "*=", "=*", "/=", "=/", "%=", "=%", '++', "--",
              '<', '>', '>=', "<=", "<<", ">>", '!', '!=', '&', '|',  '&&', '||', '^', '~', '?', ':', "()", '{}', "[]" ]

# C Punctuation
punctuations = [';', ',', '(', ')', '{', '}', '[', ']']

def tokenize(code):
    tokens = []
    state =''
    word = ''
    for line_number, line in enumerate (code, 1):
        i = 0
        state = ""
        word = ""
        while i < len(line):
            char = line[i]
            if state == "":
                if char.isalpha() or char =='_':
                    state = TOKEN_IDENTIFIER
                    word += char
                elif char.isdigit():
                    state = TOKEN_INTLITERAL
                    word += char
                elif char == '"':
                    state = TOKEN_STRLITERAL
                    word += char
                elif char == "'":
                    state = TOKEN_CHARLITERAL
                    word += char
                elif char in punctuations:
                    state = TOKEN_PUNCTUATION
                    word += char
                elif char in operators:
                    state = TOKEN_OPERATOR
                    word += char
                elif char.isspace():
                    i += 1
                    continue
                else:
                    raise ValueError(f"Invalid Character found {char} on line {line_number}")
            elif state == TOKEN_IDENTIFIER:
                if char.isalnum() or char == '_':
                    word += char
                else:
                    if word in keywords:
                        tokens.append((TOKEN_KEYWORD, word, line_number))
                        state = ""
                        word = ""
                    elif word in types:
                        tokens.append((TOKEN_TYPE, word, line_number))
                        state = "" 
                        word = ""
                    else :
                        tokens.append((TOKEN_IDENTIFIER, word, line_number))
                        state = ""
                        word = ""
                    if char != ' ':
                        i -= 1
            elif state == TOKEN_CHARLITERAL:
                if char == "'":
                    word += char
                    tokens.append((TOKEN_STRLITERAL, word, line_number))
                    state = ""
                    word = ""
                else:
                    word += char
            elif state == TOKEN_STRLITERAL:
                if char == '"':
                    word += char
                    tokens.append((TOKEN_STRLITERAL, word, line_number))
                    state = ""
                    word = ""
                else:
                    word += char
            elif state == TOKEN_INTLITERAL:
                if char.isdigit():
                    word += char
                elif char == '.':
                    state = TOKEN_FLOATLITERAL
                    word += char
                else:
                    tokens.append((TOKEN_INTLITERAL, word, line_number))
                    state = ""
                    word = ""
                    if char != ' ':
                        i -= 1
            elif state == TOKEN_FLOATLITERAL:
                if char.isdigit():
                    word += char
                else:
                    tokens.append((TOKEN_FLOATLITERAL, word, line_number))
                    state = ""
                    word = ""
                    if char != ' ':
                        i -= 1
            elif state == TOKEN_OPERATOR:
                if word + char in operators:
                    word += char
                else:
                    tokens.append((TOKEN_OPERATOR, word, line_number))
                    state = ""
                    word = ""
                    if char != ' ':
                        i -= 1
            elif state == TOKEN_PUNCTUATION:
                if word + char in operators:
                    word += char
                    tokens.append((TOKEN_OPERATOR, word, line_number))
                    state = ""
                    word = ""
                else:
                    tokens.append((TOKEN_PUNCTUATION, word, line_number))
                    state = ""
                    word = ""
                    if char != ' ':
                        i -= 1
            
            i += 1
        if state == TOKEN_IDENTIFIER:
            if word in keywords:
                tokens.append((TOKEN_KEYWORD, word, line_number))
            elif word in types:
                tokens.append((TOKEN_TYPE, word, line_number))
            else:
                tokens.append((TOKEN_IDENTIFIER, word, line_number))
        elif state == TOKEN_CHARLITERAL or state == TOKEN_STRLITERAL:
            tokens.append((TOKEN_STRLITERAL, word, line_number))   
        elif state == TOKEN_INTLITERAL:
            tokens.append((TOKEN_INTLITERAL, word, line_number))
        elif state == TOKEN_FLOATLITERAL:
            tokens.append((TOKEN_FLOATLITERAL, word, line_number))
        elif state == TOKEN_OPERATOR:
            tokens.append((TOKEN_OPERATOR, word, line_number))
        elif state == TOKEN_PUNCTUATION:
            tokens.append((TOKEN_PUNCTUATION, word, line_number))
    return tokens