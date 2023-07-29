"""
https://github.com/Carl3300/compiler_for_C/blob/main/tokenizer.py assistance found for Parsing 
"""

from tokenizer import Token
from error import BlankFile, InvalidSyntax

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
#TOKEN_COLON = 'COLON'
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

# C Type Literals
TOKEN_BOOLLITERAL = "BOOLLITERAL"
TOKEN_INTLITERAL = 'INTLITERAL'
TOKEN_FLOATLITERAL = 'FLOATLITERAL'
TOKEN_STRLITERAL = 'STRLITERAL'
TOKEN_CHARLITERAL = 'CHARLITERAL'

# Comment
TOKEN_COMMENT = 'COMMENT'


# Type Operations
class TypeNode:
    def __init__(self, token: Token) -> None:
        self.token = token
    def __repr__(self) -> str:
        return f'{self.token.type}'

class NumberNode(TypeNode):
    pass
class StringNode(TypeNode):
    pass
class BooleanNode(TypeNode):
    pass

# Operation Nodes
class BinaryOpNode():
    def __init__(self, left, operator_token, right):
        self.left = left
        self.op_tok = operator_token
        self.right = right
    def __repr__(self) -> str:
        return f"({self.left}, {self.op_tok.type}, {self.right})"

class UnaryOpNode():
    def __init__(self, operation_token, node):
        self.op_token = operation_token
        self.node = node
    def __repr__(self) -> str:
        return f"{self.op_token.Type}, {self.node}"

# Array
class ListNode():
    def __init__(self, elements_nodes) -> None:
        self.elements = elements_nodes

# Variables Nodes
class VariableAssignmentNode():
    def __init__(self, identifierToken, valueToken) -> None:
        self.identifierToken = identifierToken
        self.valueToken = valueToken

class VariableAccessNode(): # this is for variable identifiers
    def __init__(self, identifierToken) -> None:
        self.identifierToken = identifierToken

class IfNode():
    def __init__(self) -> None:
        pass

class ForNode():
    def __init__(self) -> None:
        pass

class WhileNode():
    def __init__(self) -> None:
        pass

# Code Jumping
class ReturnNode():
    def __init__(self) -> None:
        pass

class BreakNode():
    def __init__(self) -> None:
        pass

# Functions
class FunctionDefinitionNode():
    def __init__(self) -> None:
        pass



# class IdentifierNode():
#     def __init__(self, name):
#         self.name = name

# class IntegerLiteralNode:
#     def __init__(self, value):
#         self.value = value

# # Conditional Nodes
# class IfElseNode():
#     def __init__(self, condition, if_block, else_block):
#         self.condition = condition
#         self.if_block = if_block
#         self.else_block = else_block

# # Loop Nodes
# class WhileLoopNode():
#     def __init__(self, condition, body):
#         self.condition = condition
#         self.body = body

# # Function Nodes
# class FunctionCallNode():
#     def __init__(self, name, arguments):
#         self.name = name
#         self.arguments = arguments

class Result:
    def __init__(self) -> None:
        self.error = None
        self.node = None
        self.last_reg_adv = 0
        self.adv_count = 0
        self.reverse_count = 0

    def reg_adv(self):
        self.last_reg_adv= 1
        self.adv_count += 1

    def reg(self, res):
        self.last_reg_adv = res.adv_count
        self.adv_count += res.adv_count
        if res.error: 
            self.error = res.error
        return res.node

    def try_reg(self, res):
        if res.error:
          self.reverse_count = res.adv_count
          return None
        return self.register(res)

    def success(self, node):
        self.node = node
        return self

    def fail(self, error):
        if not self.error or self.last_reg_adv == 0:
            self.error = error
        return self


# Parser
class Parser:
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
        res = self.condition()
        if not res.error and self.currToken.type != TOKEN_EOF:
            return res.fail(InvalidSyntax(self.currToken.line, "Token cannot appear after previous tokens"))
        return res

   # Still need global and local variables

    def statement_list(self):
        pass

    def statement(self):
        pass

    def funct_definition(self):
        pass

    def variable_declaration(self):
        pass    

    def list_declaration(self):
        pass

    def assignment(self):
        pass

    def list_assignment(self):
        pass

    def if_Statement(self):
        pass

    def elif_statement(self):
        pass

    def else_statement(self):
        pass

    def while_Statement(self):
        res = Result()
        curr = self.currToken
        if curr.type == TOKEN_KEYWORD and curr.value == "while":
            res.reg_adv()
            self.advance()
            conditonal = res.reg(self.condition)
            if res.error:
                return res
            if self.currToken.type == TOKEN_LCURLBRACKET:
                pass # FINISH TOMORROW

    def for_Statement(self): # do after assignment 
        pass

    def condition(self):
        res = Result()
        left = res.reg(self.expression())
        if res.error:
            return res
        if self.currToken.type in [TOKEN_EQ, TOKEN_GTHAN, TOKEN_LTHAN, TOKEN_GEQ, TOKEN_LEQ]:
            operation_token = self.currToken
            res.reg_adv()
            self.advance()
            right = res.reg(self.expression())
            left = BinaryOpNode(left, operation_token, right)
        return res.success(left)

    def expression(self): 
        res = Result()
        left = res.reg(self.term())
        if res.error:
            return res
        while self.currToken.type in [TOKEN_PLUS, TOKEN_MINUS]:
            operation_token = self.currToken
            res.reg_adv()
            self.advance()
            right = res.reg(self.term())
            left = BinaryOpNode(left, operation_token, right)
        return res.success(left)

    def term(self): 
        res = Result()
        left = res.reg(self.factor())
        if res.error:
            return res
        while self.currToken.type in [TOKEN_DIVIDE, TOKEN_MULTIPLY, TOKEN_MOD, TOKEN_BAND, TOKEN_BOR]:
            operation_token = self.currToken
            res.reg_adv()
            self.advance()
            right = res.reg(self.factor())
            left = BinaryOpNode(left, operation_token, right)
        return res.success(left)

    def factor(self): # Literals        
        res = Result()
        curr = self.currToken

        if curr.type == TOKEN_MINUS:
            res.reg_adv()
            self.advance()
            factor = res.reg(self.factor())
            if res.error:
                return res
            return res.success(UnaryOpNode(curr, factor))

        if curr.type in [TOKEN_INTLITERAL, TOKEN_FLOATLITERAL]:
            res.reg_adv()
            self.advance()
            return res.success(NumberNode(curr))

        elif curr.type in [TOKEN_STRLITERAL]:
            res.reg_adv()
            self.advance()
            return res.success(StringNode(curr))

        elif curr.type in [TOKEN_BOOLLITERAL]:
            res.reg_adv()
            self.advance()
            return res.success(BooleanNode(curr))

        elif curr.type in [TOKEN_IDENTIFIER]:
            res.reg_adv()
            self.advance()
            return res.success(VariableAccessNode(curr))

        elif curr.type in [TOKEN_LPAREN]:
            res.reg_adv()
            self.advance()
            expression = res.reg(self.expression())
            if res.error:
                return res
            if self.currToken.type == TOKEN_RPAREN:
                res.reg_adv()
                self.advance()
                return res.success(expression)
            else:
                return res.fail(InvalidSyntax(self.currToken.line, "Excpected a ')'"))
        else:
            if curr.value:
                return res.fail(InvalidSyntax(curr.line, f"Expected (int, float, string, bool) literal or '(' but got {curr.value}"))
            return res.fail(BlankFile())

def ParseCode(tokens):
    parser = Parser(tokens)
    ast = parser.Parse()
    return ast.node, ast.error