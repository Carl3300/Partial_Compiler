"""
https://github.com/Carl3300/compiler_for_C/blob/main/tokenizer.py assistance found for Parsing 
"""

from tokenizer import Token
from error import InvalidSyntax
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
TOKEN_PLUSEQ = 'PLUSEQ'
TOKEN_RPLUSEQ = 'RPLUSEQ'
TOKEN_MINUSEQ = 'MINUSEQ'
TOKEN_RMINUSEQ = 'RMINUSEQ'
TOKEN_MULTIPLYEQ = 'MULTIPLYEQ'
TOKEN_RMULTIPLYEQ = 'RMULTIPLYEQ'
TOKEN_DIVIDEDEQ = 'DIVIDEEQ'
TOKEN_RDIVIDEEQ = 'RDIVIDEEQ'
TOKEN_MODEQ = 'MODEQ'
TOKEN_RMODEQ = 'RMODEQ'
TOKEN_PLUS1 = 'PLUS1'
TOKEN_MINUS1 = 'MINUS1'
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
TOKEN_XOR = 'XOR'
TOKEN_BNOT = 'BNOT'
TOKEN_TERNARY = 'TERNARY'
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
        return f'{self.token.type}'

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
        return f"({self.left}, {self.op_tok.type}, {self.right})"

class UnaryOpNode():
    def __init__(self, operation_token, node):
        self.op_token = operation_token
        self.node = node
    def __repr__(self) -> str:
        return f"{self.op_token.Type}, {self.node}"

# Array
class ListNode():
    def __init__(self) -> None:
        pass

# Variables Nodes
class VariableAssignment():
    def __init__(self) -> None:
        pass

class VariableAccess():
    def __init__(self) -> None:
        pass

# Conditionals and loops
class ConditionalOpNode():
    def __init__(self) -> None:
        pass

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
class ReturnNodeOp():
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
    def register(self, res):
        if isinstance(res, Result):
            if res.error:
                self.error = res.error
            return res.node
        return res
    def success(self, node):
        self.node = node
        return self
    def fail(self, error):
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
        res = self.statements()
        if not res.error and self.currToken != TOKEN_EOF:
          return res.failure(InvalidSyntax(self.currToken.line, "Token cannot appear after previous tokens"))
        return res

    # def program(self):
    #     pass

    # def programHeader(self):
    #     pass

    # def programBody(self):
    #     pass

    def declaration(self):
        pass

    def procedureDeclaration(self):
        pass

    def procedureHeader(self):
        pass
    
    def parameterList(self):
        pass

    def parameter(self):
        pass

    def procedureBody(self):
        pass

    def varDeclaration(self):
        pass

    def typeAndValue(self):
        pass

    def statement(self):
        pass

    def procedureCall(self):
        pass

    def assignment(self): # Variable nodes
        pass

    def ifStatement(self): # If Node
        pass

    def loopStatements(self): # loop Node Operation
        pass

    def returnStatement(self): # Return Node Operation
        pass

    def bitExpr(self): # Binary Operation
        pass

    def arithExpr(self): # Binary Operation
        pass

    def comparisonExpr(self): # Conditional Operation
        pass

    def termExpr(self): # Binary Operation
        pass

    def factor(self): 
        pass

    def atom(self): # Literals        
        pass


    # Basic Math Operations
    # def factor(self):
    #     res = Result()

    #     if self.currToken.type in [TOKEN_MINUS]:
    #         res.register(self.advance())
    #         factor = res.register(self.factor())
    #         if res.error:
    #             return res
    #         return res.success(UnaryOpNode(self.currToken, factor))

    #     elif self.currToken.type in [TOKEN_LPAREN]:
    #         res.register(self.advance())
    #         expr = res.register(self.expr())
    #         if res.error:
    #             return res
    #         if self.currToken.type in [TOKEN_RPAREN]:
    #             res.register(self.advance())
    #             return res.success(expr)
    #         else:
    #             return res.fail(InvalidSyntax(self.currToken.line, "Expected a closing ')'"))

    #     elif self.currToken.type in [TOKEN_INTLITERAL, TOKEN_FLOATLITERAL]:
    #         result = NumberNode(self.currToken)
    #         res.register(self.advance())
    #         return res.success(result)
    #     return res.fail(InvalidSyntax(self.currToken.line, "Expected Integer or Float"))

    # def term(self):
    #     return self.bin_op(self.factor, (TOKEN_MULTIPLY, TOKEN_DIVIDE, TOKEN_MOD))

    # def expr(self):
    #     res = Result()
    #     if self.currToken.type  == TOKEN_TYPE:
    #         res.register(self.advance())
    #         if self.currToken.type != TOKEN_IDENTIFIER:
    #             return res.fail(InvalidSyntax(self.currToken.line, f"Expected a Name for the {self.currToken.type}"))
    #         var_name = self.currToken
    #         res.register(self.advance())
    #     return self.bin_op(self.term, (TOKEN_PLUS, TOKEN_MINUS))

    # def bin_op(self, func, ops):
    #     res = Result()
    #     left = res.register(func())
    #     if res.error:
    #         return res
    #     while self.currToken.type in ops:
    #         op_tok = self.currToken
    #         res.register(self.advance())
    #         right = res.register(func())
    #         if res.error:
    #             return res
    #         left = BinaryOpNode(left, op_tok, right)
    #     return res.success(left)

def ParseCode(tokens):
    parser = Parser(tokens)
    ast = parser.Parse()
    return ast.node, ast.error