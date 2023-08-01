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
    def __init__(self, type_, elements_nodes) -> None:
        self.elements = elements_nodes
        self.type = type_
    def __repr__(self) -> str:
        return f"{self.elements}"

# Variables Nodes
class VariableAssignmentNode():
    def __init__(self, type_, identifierToken, valueToken=None, isList=False,) -> None:
        self.identifierToken = identifierToken
        self.type = type_
        self.isList = isList
        self.valueToken = valueToken
    def __repr__(self) -> str:
        if self.isList:
            return f"List: {self.type}, {self.valueToken}"
        return f"{self.type}: {self.valueToken}"

class VariableAccessNode(): # this is for variable identifiers
    def __init__(self, identifierToken) -> None:
        self.identifierToken = identifierToken
    def __repr__(self) -> str:
        return f"{self.identifierToken.type}"

class IfNode():
    def __init__(self, conditional, body, otherNodes) -> None:
        self.conditional = conditional
        self.body = body
        self.otherNodes = otherNodes
    def __repr__(self) -> str:
        if self.otherNodes:
            return f"IF: {self.conditional}: {self.body}, {self.otherNodes}"
        return f"IF: {self.conditional}: {self.body}"

class ElifNode():
    def __init__(self, conditional, body, otherNodes) -> None:
        self.conditional = conditional
        self.body = body
        self.otherNodes = otherNodes
    def __repr__(self) -> str:
        if self.otherNodes:
            return f"ELIF: {self.conditional}: {self.body}, {self.otherNodes}"
        return f"ELIF: {self.conditional}: {self.body}"

class ElseNode():
    def __init__(self, body) -> None:
        self.body = body
    def __repr__(self) -> str:
        return f"Else: {self.body}"

class ForNode():
    def __init__(self, variable, conditional, iter_expr, body) -> None:
        self.variable = variable
        self.conditional = conditional
        self.iter_expr = iter_expr
        self.body = body
    def __repr__(self) -> str:
        return f"For: {self.variable} - {self.conditional} - {self.iter_expr}: {self.body}"

# Functions
class FunctionDefinitionNode():
    def __init__(self) -> None:
        pass

class ReturnNode():
    def __init__(self, expression) -> None:
        self.expression = expression
    def __repr__(self) -> str:
        return f"{self.expression}"

class programNode():
    def __init__(self, functions, globalVariables) -> None:
        self.functions = functions
        self.globalvars = globalVariables
    def __repr__(self) -> str:
        return f"{self.functions}: {self.globalvars}"

# class WhileNode():
#     def __init__(self, conditional, body) -> None:
#         self.conditional = conditional
#         self.body = body
#     def __repr__(self) -> str:
#         return f"while: {self.conditional}: {self.body}"
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

# Still need global and local variables pass
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
        res = self.program()
        res.reg_adv()
        self.advance()
        if not res.error and self.currToken.type != TOKEN_EOF:
            return res.fail(InvalidSyntax(self.currToken.line, f"'{self.currToken.value}' Token out of proper context"))
        return res

    def program(self):
        res = Result()
        if self.currToken.type == TOKEN_KEYWORD and self.currToken.value == "program":
            res.reg_adv()
            self.advance()
            if self.currToken.type == TOKEN_IDENTIFIER:
                res.reg_adv()
                self.advance()
                if self.currToken.type == TOKEN_KEYWORD and self.currToken.value == "is":
                    res.reg_adv()
                    self.advance()
                    if self.currToken.type == TOKEN_KEYWORD and self.currToken.value == "begin":
                        res.reg_adv()
                        self.advance()
                        procedure_list = res.reg(self.procedure_list())
                        if res.error:
                            return res
                        if self.currToken.type == TOKEN_KEYWORD and self.currToken.value == "endprogram":
                            res.reg_adv()
                            self.advance()
                            if self.currToken.type == TOKEN_PERIOD:
                                res.reg_adv()
                                self.advance()
                                return res.success(procedure_list)
                            else:
                                return res.fail(InvalidSyntax(self.currToken.line, "A program must end with a '.'"))
                        else:
                            return res.fail(InvalidSyntax(self.currToken.line, "A program must have 'endprogram' keyword after procedure_list"))
                    else:
                         return res.fail(InvalidSyntax(self.currToken.line, "A program must have 'begin' after the 'is' keyword"))
                else:
                    return res.fail(InvalidSyntax(self.currToken.line, "A program must have 'is' after the name identifier"))
            else:
                return res.fail(InvalidSyntax(self.currToken.line, "A program must have a name identifier"))
        else:
            return res.fail(InvalidSyntax(self.currToken.line, "A program must start with the program keyword"))
                

    def procedure_list(self):
        res = Result()
        functs = []
        variables = []
        while not (self.currToken.type == TOKEN_KEYWORD and self.currToken.value == "endprogram"):
            if self.currToken.type == TOKEN_KEYWORD and self.currToken.value == "procedure":
                function_def = res.reg(self.funct_definition())
                if res.error:
                    return res
                functs.append(function_def)
            elif self.currToken.type == TOKEN_KEYWORD and self.currToken.value == "variable":
                var = res.reg(self.variable_declaration())
                if res.error:
                    return res
                variables.append(var)
            else:
               if self.currToken.type == TOKEN_EOF:
                   return res.fail(InvalidSyntax(self.currToken.line, "Expected keyword endprogram after the procedure list"))
               return res.fail(InvalidSyntax(self.currToken.line, "Expected a variable or function declaration"))
        return res.success(programNode(functs, variables))  

    def statement_list(self, terminator):
        res = Result()
        statements = []
        while not(self.currToken.type == TOKEN_KEYWORD and self.currToken.value in terminator):
            statement = res.reg(self.statement(terminator))
            if res.error:
                return res
            statements.append(statement)
        return res.success(ListNode("Statements", statements))

    def statement(self, terminator):
        res = Result()
        curr = self.currToken
        pass # I need to fix this so that advance works with it and all other types might be 
        # just that statements cannot be called directly from the main parse class
        if curr.type == TOKEN_KEYWORD and curr.value == "variable":
            val = res.reg(self.variable_declaration())
            if res.error:
                return res
            return res.success(val)
        elif curr.type == TOKEN_KEYWORD and curr.value == "list":
            val = res.reg(self.list_assignment())
            if res.error:
                return res
            return res.success(val)
        elif curr.type == TOKEN_IDENTIFIER:
            val = res.reg(self.assignment())
            if res.error:
                return res
            return res.success(val) # non-variable declared
        elif curr.type == TOKEN_KEYWORD and curr.value == "if":
            val = res.reg(self.if_Statement())
            if res.error:
                return res
            return res.success(val)
        elif curr.type == TOKEN_KEYWORD and curr.value == "else":
            val = res.reg(self.else_statement())
            if res.error:
                return res
            return res.success(val)
        elif curr.type == TOKEN_KEYWORD and curr.value == "for":
            val = res.reg(self.for_Statement())
            if res.error:
                return res
            return res.success(val)
        elif curr.type == TOKEN_KEYWORD and curr.value == "return":
            res.reg_adv()
            self.advance()
            expression = res.reg(self.expression())
            if res.error:
                return res
            if self.currToken.type == TOKEN_SEMI:
                res.reg_adv()
                self.advance()
                return res.success(ReturnNode(expression))
        else:
            return res.fail(InvalidSyntax(curr.line, f"Invalid Statement declaration expected a {terminator} to end statements"))   

    def funct_definition(self):
        pass # need to change around the variables
        res = Result()
        if self.currToken.type == TOKEN_KEYWORD and self.currToken.value == "procedure":
            res.reg_adv()
            self.advance()
            if self.currToken.type == TOKEN_IDENTIFIER:
                identifier = self.currToken.value
                res.reg_adv()
                self.advance()
                if self.currToken.type == TOKEN_COLON:
                    res.reg_adv()
                    self.advance()
                    if self.currToken.type == TOKEN_TYPE:
                        type_ = self.currToken.value
                        res.reg_adv()
                        self.advance()
                        if self.currToken.type == TOKEN_LPAREN:
                            res.reg_adv()
                            self.advance()
                            if self.currToken.type == TOKEN_KEYWORD and self.currToken.value == "variable":
                                variables = []
                                var = res.reg(self.variable_declaration())
                                variables.append(var)
                                if res.error:
                                    return res
                                while self.currToken.type == TOKEN_COMMA:
                                    var = res.reg(self.variable_declaration())
                                    variables.append(var)
                                    if res.error:
                                        return res
                                if self.currToken.type == TOKEN_RPAREN:
                                    res.reg_adv()
                                    self.advance()
                                    if self.currToken.type == TOKEN_KEYWORD and self.currToken.value == "begin":
                                        res.reg_adv()
                                        self.advance()
                                        statement_list = res.reg(self.statement_list("endprocedure"))
                                        if self.currToken.type == TOKEN_KEYWORD and self.currToken.value == "endprocedure":
                                            res.reg_adv()
                                            self.advance()
                                            pass
                                            return res.success() # make this acutally return
                                        else:
                                            return res.fail(InvalidSyntax(self.currToken.line, "Expected the 'endprocedure' keyword"))
                                    else:
                                        return res.fail(InvalidSyntax(self.currToken.line, "Expected the 'begin' keyword"))
                                else:
                                    return res.fail(InvalidSyntax(self.currToken.line, "Expected a ')"))
                            elif self.currToken.type == TOKEN_RPAREN:
                                res.reg_adv()
                                self.advance()
                                if self.currToken.type == TOKEN_KEYWORD and self.currToken.value == "begin":
                                    res.reg_adv()
                                    self.advance()
                                    statement_list = res.reg(self.statement_list("endprocedure"))
                                    if self.currToken.type == TOKEN_KEYWORD and self.currToken.value == "endprocedure":
                                        res.reg_adv()
                                        self.advance()
                                        pass
                                        return res.success() # make this acutally return
                                    else:
                                        return res.fail(InvalidSyntax(self.currToken.line, "Expected the 'endprocedure' keyword"))
                                else:
                                    return res.fail(InvalidSyntax(self.currToken.line, "Expected the 'begin' keyword"))
                            else:
                                return res.fail(InvalidSyntax(self.currToken.line, "Expected a ')"))
                        else:
                            return res.fail(InvalidSyntax(self.currToken.line, "Expected a '('"))
                    else:
                         return res.fail(InvalidSyntax(self.currToken.line, "A function must have type assignment after the ':' keyword"))
                else:
                    return res.fail(InvalidSyntax(self.currToken.line, "A function must have ':' after the name identifier"))
            else:
                return res.fail(InvalidSyntax(self.currToken.line, "A function must have a name identifier"))
        else:
            return res.fail(InvalidSyntax(self.currToken.line, "A function must start with the procedure keyword"))

    def list_operators(self):
        pass
    
    def i_operators(self):
        pass

    def variable_declaration(self, needAssignment=False):
        res = Result()
        curr = self.currToken
        if curr.type == TOKEN_KEYWORD and curr.value == "variable":
            res.reg_adv()
            self.advance()
            if self.currToken.type == TOKEN_IDENTIFIER:
                identifier = self.currToken.value
                res.reg_adv()
                self.advance()
                if self.currToken.type == TOKEN_COLON:
                    res.reg_adv()
                    self.advance()
                    if self.currToken.type == TOKEN_TYPE:
                        type_ = self.currToken.value
                        res.reg_adv()
                        self.advance()
                        if self.currToken.type == TOKEN_ASSIGN:
                            expression = res.reg(self.assignment(type_))
                            if res.error:
                                return res
                            return res.success(VariableAssignmentNode(type_, identifier, expression, False))
                        elif self.currToken.type == TOKEN_SEMI and not needAssignment:
                            res.reg_adv()
                            self.advance()
                            return res.success(VariableAssignmentNode(type_, identifier, None, False))
                        else:
                            if needAssignment:
                                return res.fail(InvalidSyntax(self.currToken.line, "Expected an '=' for variable assignment"))
                            return res.fail(InvalidSyntax(self.currToken.line, "Expected a ';'"))
                    else:
                        return res.fail(InvalidSyntax(self.currToken.line, "Expected a (INTEGER|FLOAT|STRING|BOOL) type for the variable"))
                else:
                    return res.fail((InvalidSyntax(self.currToken.line, "Expected a ':'")))
            else:
                return res.fail(InvalidSyntax(self.currToken.line, "Expected an identifier for the list"))
        else:
            return res.fail(InvalidSyntax(curr.line, "Expected the variable keyword for declaration"))   

    def list_declaration(self):
        res = Result()
        curr = self.currToken
        if curr.type == TOKEN_KEYWORD and curr.value == "list":
            res.reg_adv()
            self.advance()
            if self.currToken.type == TOKEN_IDENTIFIER:
                identifier = self.currToken.value
                res.reg_adv()
                self.advance()
                if self.currToken.type == TOKEN_COLON:
                    res.reg_adv()
                    self.advance()
                    if self.currToken.type == TOKEN_TYPE:
                        type_ = self.currToken.value
                        res.reg_adv()
                        self.advance()
                        if self.currToken.type == TOKEN_ASSIGN:
                            listNodes = res.reg(self.list_assignment(type_))
                            if res.error:
                                return res
                            return res.success(VariableAssignmentNode(type_, identifier, listNodes, True))
                        elif self.currToken.type == TOKEN_SEMI:
                            res.reg_adv()
                            self.advance()
                            return res.success(VariableAssignmentNode(type_, identifier, None, True))
                        else:
                            return res.fail(InvalidSyntax(self.currToken.line, "Expected a ';'"))
                    else:
                        return res.fail(InvalidSyntax(self.currToken.line, "Expected a (INTEGER|FLOAT|STRING|BOOL) type for the list"))
                else:
                    return res.fail((InvalidSyntax(self.currToken.line, "Expected a ':'")))
            else:
                return res.fail(InvalidSyntax(self.currToken.line, "Expected an identifier for the list"))
        else:
            return res.fail(InvalidSyntax(curr.line, "Expected the list keyword for declaration"))

    def assignment(self, type_):
        res = Result()
        if self.currToken.type == TOKEN_IDENTIFIER:
            pass # need to handle non token assigned variable 
        if self.currToken.type == TOKEN_ASSIGN:
            res.reg_adv()
            self.advance()
            expression = res.reg(self.expression())
            if res.error:
                return res
            if self.currToken.type == TOKEN_SEMI:
                res.reg_adv()
                self.advance()
                return res.success(expression)
            else:
               return res.fail(InvalidSyntax(self.currToken.line, "Expected an ';'"))
        else: 
            return res.fail(InvalidSyntax(self.currToken.line, "Expected an '=' for variable assignment"))


    def list_assignment(self, type_):
        res = Result()
        if self.currToken.type == TOKEN_IDENTIFIER:
            pass
        if self.currToken.type == TOKEN_ASSIGN:
            res.reg_adv()
            self.advance()
            if self.currToken.type == TOKEN_IDENTIFIER:
                res.reg_adv()
                self.advance()
                pass # still needs to be type checked - semantics checker
                if self.currToken.type == TOKEN_SEMI:
                    res.reg_adv()
                    self.advance()
                    return res.success(ListNode(type_, expressions))
                else:
                    return res.fail(InvalidSyntax(self.currToken.line, "Expected an ';'"))
            if self.currToken.type == TOKEN_LBRACKET:
                res.reg_adv()
                self.advance()
                expressions = []
                expression = res.reg(self.condition())
                if res.error:
                    return res
                expressions.append(expression)
                while self.currToken.type == TOKEN_COMMA:
                    res.reg_adv()
                    self.advance()
                    expression = res.reg(self.condition())
                    if res.error:
                        return res
                    expressions.append(expression)
                if self.currToken.type == TOKEN_RBRACKET:
                    res.reg_adv()
                    self.advance()
                    if self.currToken.type == TOKEN_SEMI:
                        res.reg_adv()
                        self.advance()
                        return res.success(ListNode(type_, expressions))
                    else:
                        return res.fail(InvalidSyntax(self.currToken.line, "Expected an ';'"))
                else:
                    return res.fail(InvalidSyntax(self.currToken.line, f"Expected an ']' but got a '{self.currToken.value}'"))
            else:
                return res.fail(InvalidSyntax(self.currToken.line, "Expected a list declaration or variable"))
        else: 
            return res.fail(InvalidSyntax(self.currToken.line, "Expected an '=' for list assignment"))

    def if_Statement(self):
        res = Result()
        curr = self.currToken
        if curr.type == TOKEN_KEYWORD and curr.value == "if":
            res.reg_adv()
            self.advance()
            conditional = res.reg(self.condition())
            if res.error:
                return res
            if self.currToken.type == TOKEN_KEYWORD and self.currToken.value == 'then':
                statements = res.reg(self.statement_list(["else", "endif"]))
                if res.error:
                    return res
                otherNodes = None
                if self.currToken.type == TOKEN_KEYWORD and self.currToken.value == "else":
                    otherNodes = res.reg(self.else_statement())
                    if res.error:
                        return res
                if self.currToken.type == TOKEN_KEYWORD and self.currToken.value == "endif":
                    return res.success(IfNode(conditional, statements, otherNodes))
                else:
                    return res.fail(InvalidSyntax(self.currToken.line, "Expected keyword endif"))
            else:
                return res.fail(InvalidSyntax(self.currToken.line, "Expected keyword then"))
        else:
            return res.fail(InvalidSyntax(curr.line, "Expected the if keyword"))

    def else_statement(self):
        res = Result()
        curr = self.currToken
        if curr.type == TOKEN_KEYWORD and curr.value == "else":
            res.reg_adv()
            self.advance()
            statements = res.reg(self.statement_list(["endif"]))
            if res.error:
                return res
            return res.success(ElseNode(statements))
        else: 
            return res.fail(InvalidSyntax(curr.line, "Expected the else keyword"))

    def for_Statement(self): # do after assignment 
        res = Result()
        curr = self.currToken
        if curr.type == TOKEN_KEYWORD and curr.value == "for":
            res.reg_adv()
            self.advance()
            if self.currToken.type == TOKEN_LPAREN:
                res.reg_adv()
                self.advance()
                var = res.reg(self.variable_declaration(True))
                if res.error:
                    return res
                conditional = res.reg(self.condition())
                if res.error:
                    return res
                if self.currToken.type == TOKEN_SEMI:
                    res.reg_adv()
                    self.advance()
                    expression = res.reg(self.expression())
                    if res.error:
                        return res
                    if self.currToken.type == TOKEN_SEMI:
                        res.reg_adv()
                        self.advance()
                        if self.currToken.type == TOKEN_RPAREN:
                            res.reg_adv()
                            self.advance()
                            statements = res.reg(self.statement_list(["endfor"]))
                            if res.error:
                                return res
                            if self.currToken.type == TOKEN_KEYWORD and self.currToken.value == "endfor":
                                return res.success(ForNode(var, conditional, expression, statements))
                            else:
                                return res.fail(InvalidSyntax(self.currToken.line, "for loops must end with endfor keyword"))
                        else:
                            return res.fail(InvalidSyntax(self.currToken.line, "Expected an ')' after iteration expression"))
                    else:
                        return res.fail(InvalidSyntax(self.currToken.line, "Expected an ';' after iteration expression"))
                else:
                    return res.fail(InvalidSyntax(self.currToken.line, "Expected an ';' after conditional"))
            else:
                return res.fail(InvalidSyntax(self.currToken.line, "Expected a '('"))
        else:
            return res.fail(InvalidSyntax(curr.line, "Expected the for keyword"))


    def condition(self):
        res = Result()
        curr = self.currToken
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
        while self.currToken.type in [TOKEN_DIVIDE, TOKEN_MULTIPLY, TOKEN_BAND, TOKEN_BOR]:
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
                return res.fail(InvalidSyntax(curr.line, f"Expected (INTEGER, FLOAT, STRING, BOOL) literal or expression but got {curr.value}"))
            return res.fail(BlankFile())

def ParseCode(tokens):
    parser = Parser(tokens)
    ast = parser.Parse()
    return ast.node, ast.error