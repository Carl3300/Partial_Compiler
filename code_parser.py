from tokenizer import Token

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



# Type Operations
class TypeNode:
    def __init__(self, token: Token) -> None:
        self.token = token
    def __repr__(self) -> str:
        return f'{self.token}'

class NumberNode(TypeNode):
    pass
class StringNode(TypeNode):
    pass

# Operation Nodes
class BinaryOpNode():
    def __init__(self, left, operator_token, right):
        self.left = left
        self.op_tok = operator_token
        self.right = right
    def __repr__(self) -> str:
        return f"{self.left}, {self.op_tok}, {self.right}"

class IdentifierNode():
    def __init__(self, name):
        self.name = name

class IntegerLiteralNode:
    def __init__(self, value):
        self.value = value

# Conditional Nodes
class IfElseNode():
    def __init__(self, condition, if_block, else_block):
        self.condition = condition
        self.if_block = if_block
        self.else_block = else_block

# Loop Nodes
class WhileLoopNode():
    def __init__(self, condition, body):
        self.condition = condition
        self.body = body

# Function Nodes
class FunctionCallNode():
    def __init__(self, name, arguments):
        self.name = name
        self.arguments = arguments


# Parser
class Parser():
    def __init__(self, tokens) -> None:
        self.tokens = tokens
        self.index = 0
        self.currToken = tokens[0]
    def advance(self):
        self.index += 1
        if self.index < len(self.tokens):
            self.currToken = self.tokens[self.index]
        return self.currToken
    def Parse(self):
        return self.expr

    # Basic Math Operations
    def factor(self):
        if self.currToken.type in [TOKEN_INTLITERAL, TOKEN_FLOATLITERAL]:
            self.advance()
            return NumberNode(self.currToken)

    def term(self):
        return self.bin_op(self.factor, (TOKEN_MULTIPLY, TOKEN_DIVIDE, TOKEN_MOD))

    def expr(self):
        return self.bin_op(self.term, (TOKEN_PLUS, TOKEN_MINUS))

    def bin_op(self, func, ops):
        left = func()
        while self.currToken.type in ops:
            op_tok = self.currToken
            self.advance()
            right = func()
            left = BinaryOpNode(left, op_tok, right)
        return left

def ParseCode(tokens):
    parser = Parser(tokens)
    ast = parser.Parse
    print(ast)