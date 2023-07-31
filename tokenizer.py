from error import IllegalChar

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
TOKEN_ASSIGN = 'ASSIGN'
TOKEN_EQ = 'EQ'
#TOKEN_PLUSEQ = 'PLUSEQ'
#TOKEN_RPLUSEQ = 'RPLUSEQ'
#TOKEN_MINUSEQ = 'MINUSEQ'
#TOKEN_RMINUSEQ = 'RMINUSEQ'
#TOKEN_MULTIPLYEQ = 'MULTIPLYEQ'
#TOKEN_RMULTIPLYEQ = 'RMULTIPLYEQ'
#TOKEN_DIVIDEDEQ = 'DIVIDEEQ'
#TOKEN_RDIVIDEEQ = 'RDIVIDEEQ'
#TOKEN_MODEQ = 'MODEQ'
#TOKEN_RMODEQ = 'RMODEQ'
#TOKEN_PLUS1 = 'PLUS1'
#TOKEN_MINUS1 = 'MINUS1'
TOKEN_LTHAN = 'LTHAN'
TOKEN_GTHAN = 'GTHAN'
TOKEN_GEQ = 'GEQ'
TOKEN_LEQ = 'LEQ'
TOKEN_LSHIFT = 'LSHIFT'
TOKEN_RSHIFT = 'RSHIFT'
TOKEN_NOT = 'NOT'
TOKEN_NOTEQ = 'NOTEQ'
TOKEN_BAND = 'BAND'
TOKEN_BOR = 'BOR'
TOKEN_AND = 'AND'
TOKEN_OR = 'OR'
#TOKEN_XOR = 'XOR'
#TOKEN_BNOT = 'BNOT'
#TOKEN_TERNARY = 'TERNARY'
TOKEN_COLON = 'COLON'
TOKEN_PAREN = 'PAREN'
TOKEN_CURLBRACKET = 'CURLBRACKET'
TOKEN_BRACKET = 'BRACKET'

# C Punctuation
TOKEN_SEMI = 'SEMI'
TOKEN_COMMA = 'COMMA'
TOKEN_LPAREN = 'LPAREN'
TOKEN_RPAREN = 'RPAREN'
TOKEN_LCURLBRACKET = 'LCURLBRACKET'
TOKEN_RCURLBRACKET = 'RCURLBRACKET'
TOKEN_LBRACKET = 'LBRACKET'
TOKEN_RBRACKET = 'RBRACKET'
TOKEN_PERIOD = "PERIOD"

# C Type Literals
TOKEN_BOOLLITERAL = "BOOLLITERAL"
TOKEN_INTLITERAL = 'INTLITERAL'
TOKEN_FLOATLITERAL = 'FLOATLITERAL'
TOKEN_STRLITERAL = 'STRLITERAL'
TOKEN_CHARLITERAL = 'CHARLITERAL'

# Comment
TOKEN_COMMENT = 'COMMENT'

# C keywords = [ 'break', 'case', 'const', 'continue', 'default', 'do', 'else', 'enum', 'extern',
#              'for', 'printf', 'goto', 'if', 'register', 'return', 'signed', 'sizeof', 'static', 
#              'switch', 'typedef', 'union', 'unsigned', 'volatile', 'while']
# Keywords
keywords = [ 'list', 'variable', 'global', 'procedure', 'begin', 'endprocedure', "program" , "endprogram" , 'break', 'if', 
             'then', 'else', "endif", "for", "endfor", "true", "false", "is", "return"]

# Comment Operators
comments = ['//', '/*', '*/']

# C Types = [ 'auto', 'char', 'double', 'float', 'int', 'short', 'long', 'struct', 'void']
# Types
types = [ 'bool', 'float', 'integer', 'string']

# C Operators = [ '+', '-', '*', '/', '%','=', '+=', '=+', "-=", "=-", "*=", "=*", "/=", "=/", "%=", "=%", '++', "--",
#              '<', '>', "<=", '>=', "<<", ">>", '!', '!=', '&', '|',  '&&', '||', '^', '~', '?', ':', "()", '{}', "[]" ]
# C Operators
operators = [ '+', '-', '*', '/', '%','=','==', ':', '<', '>', "<=", '>=', "<<", ">>", '!', '!=', '&', '|',  '&&', '||', "()", "[]"]

# C punctuations = [';', ',', '(', ')', '{', '}', '[', ']']
# Punctuation
punctuations = [';', ',', '(', ')', '{', '}', '[', ']', "."]

class Token:
    def __init__(self, Token_Name: str, Token_Val, Token_Line: int) -> None:
        self.type = Token_Name
        self.value = Token_Val
        self.line = Token_Line
    # def inTokenType(self, varType, value):
    #     return self.type == varType and self.value == value
    def __repr__(self) -> str:
        if self.value: 
            return f'{self.type}: {self.value} (line: {self.line})'
        return f'{self.type}'

def assignOperator(tokens, word, line_number):
    if word =='+':
        tokens.append(Token(TOKEN_PLUS, word, line_number))
    elif word == '-':
        tokens.append(Token(TOKEN_MINUS, word, line_number))
    elif word == '*':
        tokens.append(Token(TOKEN_MULTIPLY, word, line_number))
    elif word == '/':
        tokens.append(Token(TOKEN_DIVIDE, word, line_number))
    elif word == '%':
        tokens.append(Token(TOKEN_MOD, word, line_number))
    elif word == '=':
        tokens.append(Token(TOKEN_ASSIGN, word, line_number))
    elif word == '==':
        tokens.append(Token(TOKEN_EQ, word, line_number))
    elif word == ':':
        tokens.append(Token(TOKEN_COLON, word, line_number))
#    elif word == '+=':
#        tokens.append(Token(TOKEN_PLUSEQ, word, line_number))
#    elif word == '=+':
#        tokens.append(Token(TOKEN_RPLUSEQ, word, line_number))
#    elif word == '-=':
#        tokens.append(Token(TOKEN_MINUSEQ, word, line_number))
#    elif word == '=-':
#        tokens.append(Token(TOKEN_RMINUSEQ, word, line_number))
#    elif word == '*=':
#        tokens.append(Token(TOKEN_MULTIPLYEQ, word, line_number))
#    elif word == '=*':
#        tokens.append(Token(TOKEN_RMULTIPLYEQ, word, line_number))
#    elif word == '/=':
#        tokens.append(Token(TOKEN_DIVIDEDEQ, word, line_number))
#    elif word == '=/':
#        tokens.append(Token(TOKEN_RDIVIDEEQ, word, line_number))
#    elif word == '%=':
#        tokens.append(Token(TOKEN_MODEQ, word, line_number))
#    elif word == '=%':
#        tokens.append(Token(TOKEN_RMODEQ, word, line_number))
#    elif word == '++':
#        tokens.append(Token(TOKEN_PLUS1, word, line_number))
#    elif word == '--':
#        tokens.append(Token(TOKEN_MINUS1, word, line_number))
    elif word == '<':
        tokens.append(Token(TOKEN_LTHAN, word, line_number))
    elif word == '>':
        tokens.append(Token(TOKEN_GTHAN, word, line_number))
    elif word == '<=':
        tokens.append(Token(TOKEN_LEQ, word, line_number))
    elif word == '>=':
        tokens.append(Token(TOKEN_GEQ, word, line_number))
    elif word == '<<':
        tokens.append(Token(TOKEN_LSHIFT, word, line_number))
    elif word == '>>':
        tokens.append(Token(TOKEN_RSHIFT, word, line_number))
    elif word == '!':
        tokens.append(Token(TOKEN_NOT, word, line_number))
    elif word == '!=':
        tokens.append(Token(TOKEN_NOTEQ, word, line_number))
    elif word == '&':
        tokens.append(Token(TOKEN_BAND, word, line_number))
    elif word == '|':
        tokens.append(Token(TOKEN_BOR, word, line_number))
    elif word == '&&':
        tokens.append(Token(TOKEN_AND, word, line_number))
    elif word == '||':
        tokens.append(Token(TOKEN_OR, word, line_number))
#    elif word == '^':
#        tokens.append(Token(TOKEN_XOR, word, line_number))
#    elif word == '~':
#        tokens.append(Token(TOKEN_BNOT, word, line_number)) 
#    elif word == '?':
#        tokens.append(Token(TOKEN_TERNARY, word, line_number)) 
#    elif word == ':':
#        tokens.append(Token(TOKEN_COLON, word, line_number))
    elif word == '()':
        tokens.append(Token(TOKEN_PAREN, word, line_number)) 
    elif word == '{}':
        tokens.append(Token(TOKEN_CURLBRACKET, word, line_number)) 
    elif word == '[]':
        tokens.append(Token(TOKEN_BRACKET, word, line_number))
    else:
        tokens.append(Token(TOKEN_OPERATOR, word, line_number))
    return tokens

def assignPunctutation(tokens, word, line_number):
    if word == ';':
        tokens.append(Token(TOKEN_SEMI, word, line_number)) 
    elif word == ',':
        tokens.append(Token(TOKEN_COMMA, word, line_number)) 
    elif word == '(':
        tokens.append(Token(TOKEN_LPAREN, word, line_number)) 
    elif word == ')':
        tokens.append(Token(TOKEN_RPAREN, word, line_number)) 
    elif word == '{':
        tokens.append(Token(TOKEN_LCURLBRACKET, word, line_number)) 
    elif word == '}':
        tokens.append(Token(TOKEN_RCURLBRACKET, word, line_number))
    elif word == '[':
        tokens.append(Token(TOKEN_LBRACKET, word, line_number)) 
    elif word == ']':
        tokens.append(Token(TOKEN_RBRACKET, word, line_number))
    elif word == '.':
        tokens.append(Token(TOKEN_PERIOD, word, line_number))
    else:
        tokens.append(Token(TOKEN_PUNCTUATION, word, line_number))
    return tokens

def tokenize(code):
    tokens = []
    last_line_number = 0
    last_char = ''
    state =''
    word = ''
    for line_number, line in enumerate (code, 1):
        i = 0
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
                    return [], IllegalChar(line_number, char)
            elif state == TOKEN_IDENTIFIER:
                if char.isalnum() or char == '_':
                    word += char
                else:
                    if word.lower() in keywords:
                        if word.lower() in ["true", "false"]: 
                            tokens.append(Token(TOKEN_BOOLLITERAL, word.lower() , line_number))
                        else:
                            tokens.append(Token(TOKEN_KEYWORD, word.lower() , line_number))
                        state = ""
                        word = ""
                    elif word.lower() in types:
                        tokens.append(Token(TOKEN_TYPE, word.lower() , line_number))
                        state = "" 
                        word = ""
                    else :
                        tokens.append(Token(TOKEN_IDENTIFIER, word.lower(), line_number))
                        state = ""
                        word = ""
                    if char != ' ':
                        i -= 1
            elif state == TOKEN_CHARLITERAL:
                if char == "'":
                    word += char
                    tokens.append(Token(TOKEN_STRLITERAL, word, line_number))
                    state = ""
                    word = ""
                else:
                    word += char
            elif state == TOKEN_STRLITERAL:
                if char == '"':
                    word += char
                    tokens.append(Token(TOKEN_STRLITERAL, word, line_number))
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
                    tokens.append(Token(TOKEN_INTLITERAL, word, line_number))
                    state = ""
                    word = ""
                    if char != ' ':
                        i -= 1
            elif state == TOKEN_FLOATLITERAL:
                if char.isdigit():
                    word += char
                else:
                    tokens.append(Token(TOKEN_FLOATLITERAL, word, line_number))
                    state = ""
                    word = ""
                    if char != ' ':
                        i -= 1
            elif state == TOKEN_OPERATOR:
                if word + char in operators:
                    word += char
                elif word + char in comments:
                    word += char
                    state = TOKEN_COMMENT
                    if word == "//":
                        word = ""
                        break
                else:
                    tokens = assignOperator(tokens, word, line_number)
                    state = ""
                    word = ""
                    if char != ' ':
                        i -= 1
            elif state == TOKEN_PUNCTUATION:
                if word + char in operators:
                    word += char
                    tokens = assignOperator(tokens, word, line_number)
                    state = ""
                    word = ""
                else:
                    tokens = assignPunctutation(tokens, word, line_number)
                    state = ""
                    word = ""
                    if char != ' ':
                        i -= 1
            elif state == TOKEN_COMMENT:
                if last_char + char == "*/" and line_number == last_line_number:
                    state = ""
                    word = ""
                else:
                    last_char = char
                    last_line_number = line_number
            i += 1
        if state == TOKEN_IDENTIFIER:
            if word in keywords:
                if word.lower() in ["true", "false"]: 
                    tokens.append(Token(TOKEN_BOOLLITERAL, word.lower() , line_number))
                else:
                    tokens.append(Token(TOKEN_KEYWORD, word.lower(), line_number))
            elif word in types:
                tokens.append(Token(TOKEN_TYPE, word.lower(), line_number))
            else:
                tokens.append(Token(TOKEN_IDENTIFIER, word.lower(), line_number))
        elif state == TOKEN_CHARLITERAL or state == TOKEN_STRLITERAL:
            tokens.append(Token(TOKEN_STRLITERAL, word, line_number))   
            state = ""
        elif state == TOKEN_INTLITERAL:
            tokens.append(Token(TOKEN_INTLITERAL, word, line_number))
            state = ""
        elif state == TOKEN_FLOATLITERAL:
            tokens.append(Token(TOKEN_FLOATLITERAL, word, line_number))
            state = ""
        elif state == TOKEN_OPERATOR:
            tokens = assignOperator(tokens, word, line_number)
            state = ""
        elif state == TOKEN_PUNCTUATION:
            tokens = assignPunctutation(tokens, word, line_number)
            state = ""
    tokens.append(Token(TOKEN_EOF, "", line_number))
    return tokens, None