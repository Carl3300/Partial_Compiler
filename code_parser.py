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
# TOKEN_LSHIFT = 'LSHIFT'
# TOKEN_RSHIFT = 'RSHIFT'
TOKEN_NOT = 'NOT'
TOKEN_NOTEQ = 'NOTEQ'
TOKEN_BAND = 'BAND'
TOKEN_BOR = 'BOR'
TOKEN_BNOT = 'BNOT'
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

class IntNode(TypeNode):
    pass
class FloatNode(TypeNode):
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
        return f"{self.op_token.type}, {self.node}"

# Variables Nodes
class VariableAssignmentNode():
    def __init__(self, identifierToken, valueToken, index=None) -> None:
        self.identifierToken = identifierToken
        self.valueToken = valueToken
        self.index = index
    def __repr__(self) -> str:
        return f"{self.identifierToken.value}: {self.valueToken}"

class VariableCreationNode():
    def __init__(self, type_, identifierToken, isList=False, list_size=None) -> None:
        self.identifierToken = identifierToken
        self.type = type_
        self.isList = isList
        self.size = list_size
    def __repr__(self) -> str:
        if self.isList:
            return f"List: {self.identifierToken.value}: {self.type.value} - Size: {self.size}"
        return f"{self.identifierToken.value}: {self.type.value}"

class GlobalVariableCreationNode():
    def __init__(self, type_, identifierToken, isList=False, list_size=None) -> None:
        self.identifierToken = identifierToken
        self.type = type_
        self.isList = isList
        self.size = list_size
    def __repr__(self) -> str:
        if self.isList:
            return f"List: {self.identifierToken.value}: {self.type.value} - Size: {self.size}"
        return f"{self.identifierToken.value}: {self.type.value}"

class VariableAccessNode(): # this is for variable identifiers
    def __init__(self, identifierToken , index=None) -> None:
        self.identifierToken = identifierToken
        self.index = index
    def __repr__(self) -> str:
        if self.index:
            return f"{self.identifierToken.value} at element {self.index}"
        return f"{self.identifierToken.value}"

class IfNode():
    def __init__(self, conditional, body, otherNode) -> None:
        self.conditional = conditional
        self.body = body
        self.otherNode = otherNode
    def __repr__(self) -> str:
        if self.otherNodes:
            return f"IF: {self.conditional}: {self.body}, {self.otherNodes}"
        return f"IF: {self.conditional}: {self.body}"

class ElseNode():
    def __init__(self, body) -> None:
        self.body = body
    def __repr__(self) -> str:
        return f"Else: {self.body}"

class ForNode():
    def __init__(self, variable, conditional, body) -> None:
        self.variable = variable
        self.conditional = conditional
        self.body = body
    def __repr__(self) -> str:
        return f"For: ({self.variable}, {self.conditional}): {self.body}"

# Functions
class FunctionDefinitionNode():
    def __init__(self, identifier, type_, procedure_list, statement_list, variables=None) -> None:
        self.declarations = procedure_list
        self.statements = statement_list
        self.identifier = identifier
        self.type = type_
        self.variables = variables
    def __repr__(self) -> str:
        return f"Function {self.identifier.value} - {self.declarations}: {self.statements}"

class GlobalFunctionDefinitionNode():
    def __init__(self, identifier, type_, procedure_list, statement_list, variables=None) -> None:
        self.declarations = procedure_list
        self.statements = statement_list
        self.identifier = identifier
        self.type = type_
        self.variables = variables
    def __repr__(self) -> str:
        return f"Function {self.identifier.value} - {self.declarations}: {self.statements}"

class FunctionAccessNode():
    def __init__(self, identifier, variables) -> None:
        self.identifier = identifier
        self.variables = variables
    def __repr__(self) -> str:
        if self.variables:
            return f"Function {self.identifier.value}({self.variables})"
        return f"Function {self.identifier.value}"

class ReturnNode():
    def __init__(self, expression) -> None:
        self.expression = expression
    def __repr__(self) -> str:
        return f"{self.expression}"

# Top level Node
class ProgramNode():
    def __init__(self, identifier, procedure_list, statement_list) -> None:
        self.declarations = procedure_list
        self.identifier = identifier
        self.statements = statement_list
    def __repr__(self) -> str:
        return f"{self.declarations}: {self.statements}"

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
                identifier = self.currToken
                res.reg_adv()
                self.advance()
                if self.currToken.type == TOKEN_KEYWORD and self.currToken.value == "is":
                    res.reg_adv()
                    self.advance()
                    procedure_list = res.reg(self.program_procedure_list())
                    if res.error:
                        return res
                    if self.currToken.type == TOKEN_KEYWORD and self.currToken.value == "begin":
                        res.reg_adv()
                        self.advance()
                        statement_list = res.reg(self.statement_list())
                        if res.error:
                            return res
                        if self.currToken.type == TOKEN_KEYWORD and self.currToken.value == "end":
                            res.reg_adv()
                            self.advance()
                            if self.currToken.type == TOKEN_KEYWORD and self.currToken.value == "program":
                                res.reg_adv()
                                self.advance()
                                if self.currToken.type == TOKEN_PERIOD:
                                    res.reg_adv()
                                    self.advance()
                                    return res.success(ProgramNode(identifier, procedure_list, statement_list))
                                else:
                                    return res.fail(InvalidSyntax(self.currToken.line, "A program must end with a '.'"))
                            else:
                                return res.fail(InvalidSyntax(self.currToken.line, "A program must have 'program' after the 'end' keyword"))
                        else:
                            return res.fail(InvalidSyntax(self.currToken.line, "A program must have 'end' keyword after statement_list"))
                    else:
                         return res.fail(InvalidSyntax(self.currToken.line, "A program must have 'begin' after the procedure_list"))
                else:
                    return res.fail(InvalidSyntax(self.currToken.line, "A program must have 'is' after the name identifier"))
            else:
                return res.fail(InvalidSyntax(self.currToken.line, "A program must have a name identifier"))
        else:
            return res.fail(InvalidSyntax(self.currToken.line, "A program must start with the program keyword"))
                

    def procedure_list(self):
        res = Result()
        declarations = []
        while not (self.currToken.type == TOKEN_KEYWORD and self.currToken.value == "begin"):
            if self.currToken.type == TOKEN_KEYWORD and self.currToken.value == "procedure":
                function_def = res.reg(self.funct_definition())
                if res.error:
                    return res
                declarations.append(function_def)
            elif self.currToken.type == TOKEN_KEYWORD and self.currToken.value == "variable":
                var = res.reg(self.variable_declaration())
                if res.error:
                    return res
                declarations.append(var)
            elif self.currToken.type == TOKEN_KEYWORD and self.currToken.value == "global":
                var = res.reg(self.global_var_declaration())
                if res.error:
                    return res
                declarations.append(var)
            else:
               return res.fail(InvalidSyntax(self.currToken.line, "Expected the keyword 'begin' to start the main function"))
        return res.success(declarations)

    def program_procedure_list(self):
            res = Result()
            declarations = []
            while not (self.currToken.type == TOKEN_KEYWORD and self.currToken.value == "begin"):
                if self.currToken.type == TOKEN_KEYWORD and self.currToken.value == "procedure":
                    function_def = res.reg(self.funct_definition())
                    if res.error:
                        return res
                    declarations.append(function_def)
                elif self.currToken.type == TOKEN_KEYWORD and self.currToken.value == "variable":
                    var = res.reg(self.variable_declaration(True))
                    if res.error:
                        return res
                    declarations.append(var)
                elif self.currToken.type == TOKEN_KEYWORD and self.currToken.value == "global":
                    var = res.reg(self.global_var_declaration())
                    if res.error:
                        return res
                    declarations.append(var)
                else:
                   return res.fail(InvalidSyntax(self.currToken.line, "Expected the keyword 'begin' to start the main function"))
            return res.success(declarations)

    def statement_list(self):
        res = Result()
        statements = []
        while not(self.currToken.type == TOKEN_KEYWORD and self.currToken.value == "end"):
            statement = res.reg(self.statement())
            if res.error:
                return res
            statements.append(statement)
        return res.success(statements)

    def statement(self):
        res = Result()
        curr = self.currToken
        if curr.type == TOKEN_IDENTIFIER:
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
            return res.fail(InvalidSyntax(curr.line, f"Invalid Statement declaration {self.currToken.value} maybe keyword 'end' was desired"))   

    def funct_definition(self, Global=False):
        res = Result()
        if self.currToken.type == TOKEN_KEYWORD and self.currToken.value == "procedure":
            res.reg_adv()
            self.advance()
            if self.currToken.type == TOKEN_IDENTIFIER:
                identifier = self.currToken
                res.reg_adv()
                self.advance()
                if self.currToken.type == TOKEN_COLON:
                    res.reg_adv()
                    self.advance()
                    if self.currToken.type == TOKEN_TYPE:
                        type_ = self.currToken
                        res.reg_adv()
                        self.advance()
                        if self.currToken.type == TOKEN_LPAREN:
                            res.reg_adv()
                            self.advance()
                            if self.currToken.type == TOKEN_KEYWORD and self.currToken.value == "variable":
                                variables = []
                                var = res.reg(self.variable_declaration(True))
                                variables.append(var)
                                if res.error:
                                    return res
                                while self.currToken.type == TOKEN_COMMA:
                                    var = res.reg(self.variable_declaration(True))
                                    variables.append(var)
                                    if res.error:
                                        return res
                                if self.currToken.type == TOKEN_RPAREN:
                                    res.reg_adv()
                                    self.advance()
                                    procedure_list = res.reg(self.procedure_list())
                                    if res.error:
                                        return res
                                    if self.currToken.type == TOKEN_KEYWORD and self.currToken.value == "begin":
                                        res.reg_adv()
                                        self.advance()
                                        statement_list = res.reg(self.statement_list())
                                        if res.error:
                                            return res
                                        if self.currToken.type == TOKEN_KEYWORD and self.currToken.value == "end":
                                            res.reg_adv()
                                            self.advance()
                                            if self.currToken.type == TOKEN_KEYWORD and self.currToken.value == "procedure":
                                                res.reg_adv()
                                                self.advance()
                                                if self.currToken.type == TOKEN_SEMI:
                                                    res.reg_adv()
                                                    self.advance()
                                                    if Global:
                                                        return res.success(GlobalFunctionDefinitionNode(identifier, type_, procedure_list, statement_list, variables))
                                                    return res.success(FunctionDefinitionNode(identifier, type_, procedure_list, statement_list, variables)) # make this acutally return
                                                else:
                                                    return res.fail(InvalidSyntax(self.currToken.line, "Expected a ';' after procedure"))
                                            else:
                                                return res.fail(InvalidSyntax(self.currToken.line, "Expected the 'procedure' keyword"))
                                        else:
                                            return res.fail(InvalidSyntax(self.currToken.line, "Expected the 'end' keyword"))
                                    else:
                                        return res.fail(InvalidSyntax(self.currToken.line, "Expected the 'begin' keyword after function definition"))
                                else:
                                    return res.fail(InvalidSyntax(self.currToken.line, "Expected a ')'"))
                            elif self.currToken.type == TOKEN_RPAREN:
                                res.reg_adv()
                                self.advance()
                                procedure_list = res.reg(self.procedure_list())
                                if res.error:
                                    return res
                                if self.currToken.type == TOKEN_KEYWORD and self.currToken.value == "begin":
                                    res.reg_adv()
                                    self.advance()
                                    statement_list = res.reg(self.statement_list())
                                    if res.error:
                                        return res
                                    if self.currToken.type == TOKEN_KEYWORD and self.currToken.value == "end":
                                        res.reg_adv()
                                        self.advance()
                                        if self.currToken.type == TOKEN_KEYWORD and self.currToken.value == "procedure":
                                            res.reg_adv()
                                            self.advance()
                                            if self.currToken.type == TOKEN_SEMI:
                                                res.reg_adv()
                                                self.advance()
                                                if Global:
                                                    return res.success(GlobalFunctionDefinitionNode(identifier, type_, procedure_list, statement_list))
                                                return res.success(FunctionDefinitionNode(identifier, type_, procedure_list, statement_list)) # make this acutally return
                                            else:
                                                return res.fail(InvalidSyntax(self.currToken.line, "Expected a ';' after procedure"))
                                        else:
                                            return res.fail(InvalidSyntax(self.currToken.line, "Expected the 'procedure' keyword"))
                                    else:
                                        return res.fail(InvalidSyntax(self.currToken.line, "Expected the 'end' keyword"))
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

    def variable_declaration(self, inFunction=False, Global=False):
        res = Result()
        curr = self.currToken
        if curr.type == TOKEN_KEYWORD and curr.value == "variable":
            res.reg_adv()
            self.advance()
            if self.currToken.type == TOKEN_IDENTIFIER:
                identifier = self.currToken
                res.reg_adv()
                self.advance()
                if self.currToken.type == TOKEN_COLON:
                    res.reg_adv()
                    self.advance()
                    if self.currToken.type == TOKEN_TYPE:
                        type_ = self.currToken
                        res.reg_adv()
                        self.advance()
                        if self.currToken.type == TOKEN_LBRACKET:
                            res.reg_adv()
                            self.advance()
                            if self.currToken.type == TOKEN_INTLITERAL:
                                int_literal = self.currToken
                                res.reg_adv()
                                self.advance()
                                if self.currToken.type == TOKEN_RBRACKET:
                                    res.reg_adv()
                                    self.advance()
                                    if self.currToken.type == TOKEN_SEMI:
                                        res.reg_adv()
                                        self.advance()
                                        if Global:
                                            return res.success(GlobalVariableCreationNode(type_, identifier, True, int_literal))
                                        return res.success(VariableCreationNode(type_, identifier, True, int_literal))
                                    else:
                                        return res.fail(InvalidSyntax(self.currToken.line, "Expected a ';' after the brackets"))
                                else:
                                    return res.fail(InvalidSyntax(self.currToken.line, "Expected a ']'"))
                            else:
                                return res.fail(InvalidSyntax(self.currToken.line, "Expected a list size"))
                        elif self.currToken.type == TOKEN_SEMI:
                            res.reg_adv()
                            self.advance()
                            if Global:
                                return res.success(GlobalVariableCreationNode(type_, identifier))
                            return res.success(VariableCreationNode(type_, identifier))
                        elif inFunction:
                            return res.success(VariableCreationNode(type_, identifier))
                        else:
                            return res.fail(InvalidSyntax(self.currToken.line, "Expected a ';' or list declaration [#];"))
                    else:
                        return res.fail(InvalidSyntax(self.currToken.line, "Expected a (INTEGER|FLOAT|STRING|BOOL) type for the variable"))
                else:
                    return res.fail((InvalidSyntax(self.currToken.line, "Expected a ':'")))
            else:
                return res.fail(InvalidSyntax(self.currToken.line, "Expected an identifier for the list"))
        else:
            return res.fail(InvalidSyntax(curr.line, "Expected the variable keyword for declaration"))   

    def global_var_declaration(self):
        res = Result()
        curr = self.currToken
        if curr.type == TOKEN_KEYWORD and curr.value == "global":
            res.reg_adv()
            self.advance()
            if self.currToken.type == TOKEN_KEYWORD and self.currToken.value == "procedure":
                global_function = res.reg(self.funct_definition(True))
                if res.error:
                    return res
                return res.success(global_function)
            elif self.currToken.type == TOKEN_KEYWORD and self.currToken.value == "variable":
                res.reg_adv()
                self.advance()
                if self.currToken.type == TOKEN_IDENTIFIER:
                    identifier = self.currToken
                    res.reg_adv()
                    self.advance()
                    if self.currToken.type == TOKEN_COLON:
                        res.reg_adv()
                        self.advance()
                        if self.currToken.type == TOKEN_TYPE:
                            type_ = self.currToken
                            res.reg_adv()
                            self.advance()
                            if self.currToken.type == TOKEN_LBRACKET:
                                res.reg_adv()
                                self.advance()
                                if self.currToken.type == TOKEN_INTLITERAL:
                                    int_literal = self.currToken
                                    res.reg_adv()
                                    self.advance()
                                    if self.currToken.type == TOKEN_RBRACKET:
                                        res.reg_adv()
                                        self.advance()
                                        if self.currToken.type == TOKEN_SEMI:
                                            res.reg_adv()
                                            self.advance()
                                            return res.success(GlobalVariableCreationNode(type_, identifier, True, int_literal))
                                        else:
                                            return res.fail(InvalidSyntax(self.currToken.line, "Expected a ';' after the brackets"))
                                    else:
                                        return res.fail(InvalidSyntax(self.currToken.line, "Expected a ']'"))
                                else:
                                    return res.fail(InvalidSyntax(self.currToken.line, "Expected a list size"))
                            elif self.currToken.type == TOKEN_SEMI:
                                res.reg_adv()
                                self.advance()
                                return res.success(GlobalVariableCreationNode(type_, identifier, False))
                            else:
                                return res.fail(InvalidSyntax(self.currToken.line, "Expected a ';'"))
                        else:
                            return res.fail(InvalidSyntax(self.currToken.line, "Expected a (INTEGER|FLOAT|STRING|BOOL) type for the variable"))
                    else:
                        return res.fail((InvalidSyntax(self.currToken.line, "Expected a ':'")))
                else:
                    return res.fail(InvalidSyntax(self.currToken.line, "Expected an identifier for the list"))
            else:
                return res.fail(InvalidSyntax(curr.line, "Expected the variable or procedure keyword for declaration"))   
        else: 
            return res.fail(InvalidSyntax(curr.line, "Expected the global keyword for declaration"))   

    def assignment(self):
        res = Result()
        if self.currToken.type == TOKEN_IDENTIFIER:
            identifier =  self.currToken
            res.reg_adv()
            self.advance()
            int_literal = None
            if self.currToken.type == TOKEN_LBRACKET:
                res.reg_adv()
                self.advance()
                if self.currToken.type == TOKEN_INTLITERAL:
                    int_literal = self.currToken
                    res.reg_adv()
                    self.advance()
                    if self.currToken.type == TOKEN_RBRACKET:
                        res.reg_adv()
                        self.advance()
                    else:
                        return res.fail(InvalidSyntax(self.currToken.line, "Expected ']' to close array indexing"))
                else:
                    return res.fail(InvalidSyntax(self.currToken.line, "Expected integer for array indexing"))
            if self.currToken.type == TOKEN_ASSIGN:
                res.reg_adv()
                self.advance()
                condition = res.reg(self.condition())
                if res.error:
                    return res
                if self.currToken.type == TOKEN_SEMI:
                    res.reg_adv()
                    self.advance()
                    if int_literal:
                        return res.success(VariableAssignmentNode(identifier, condition, int_literal))
                    return res.success(VariableAssignmentNode(identifier, condition))
                else:
                   return res.fail(InvalidSyntax(self.currToken.line, "Expected an ';'"))
            else: 
                return res.fail(InvalidSyntax(self.currToken.line, "Expected an ':=' for variable assignment"))
        else:
            return res.fail(InvalidSyntax(self.currToken.line, "Expected an variable identifier"))

    def if_Statement(self):
        res = Result()
        curr = self.currToken
        if curr.type == TOKEN_KEYWORD and curr.value == "if":
            res.reg_adv()
            self.advance()
            if self.currToken.type == TOKEN_LPAREN:
                res.reg_adv()
                self.advance()
                conditional = res.reg(self.condition())
                if res.error:
                    return res
                if self.currToken.type == TOKEN_RPAREN:
                    res.reg_adv()
                    self.advance()
                    if self.currToken.type == TOKEN_KEYWORD and self.currToken.value == 'then':
                        res.reg_adv()
                        self.advance()
                        statements = res.reg(self.statement_list())
                        if res.error:
                            return res
                        otherNode = None
                        if self.currToken.type == TOKEN_KEYWORD and self.currToken.value == "else":
                            otherNode = res.reg(self.else_statement())
                            if res.error:
                                return res
                        if self.currToken.type == TOKEN_KEYWORD and self.currToken.value == "end":
                            res.reg_adv()
                            self.advance()
                            if self.currToken.type == TOKEN_KEYWORD and self.currToken.value == "if":
                                res.reg_adv()
                                self.advance()
                                if self.currToken.type == TOKEN_SEMI:
                                    res.reg_adv()
                                    self.advance()
                                    return res.success(IfNode(conditional, statements, otherNode))
                                else:
                                    return res.fail(InvalidSyntax(self.currToken.line, "Expected ';' after 'if'"))
                            else:
                                return res.fail(InvalidSyntax(self.currToken.line, "Expected keyword 'if'"))
                        else:
                            return res.fail(InvalidSyntax(self.currToken.line, "Expected keyword 'end'"))
                    else:
                        return res.fail(InvalidSyntax(self.currToken.line, "Expected keyword 'then'"))
                else:
                    return res.fail(InvalidSyntax(curr.line, "Expected a ')'"))
            else:
                return res.fail(InvalidSyntax(curr.line, "Expected a '('"))
        else:
            return res.fail(InvalidSyntax(curr.line, "Expected keyword 'if'"))

    def else_statement(self):
        res = Result()
        curr = self.currToken
        if curr.type == TOKEN_KEYWORD and curr.value == "else":
            res.reg_adv()
            self.advance()
            statements = res.reg(self.statement_list())
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
                if self.currToken.type == TOKEN_IDENTIFIER:
                    var = res.reg(self.assignment())
                elif self.currToken.type == TOKEN_KEYWORD and self.currToken.value == "variable": 
                    var = res.reg(self.variable_declaration())
                else:
                    return res.fail(InvalidSyntax(curr.line, "Expected a variable declaration or assigment"))
                conditional = res.reg(self.condition())
                if res.error:
                    return res
                if self.currToken.type == TOKEN_RPAREN:
                    res.reg_adv()
                    self.advance()
                    statements = res.reg(self.statement_list())
                    if res.error:
                        return res
                    if self.currToken.type == TOKEN_KEYWORD and self.currToken.value == "end":
                        res.reg_adv()
                        self.advance()
                        if self.currToken.type == TOKEN_KEYWORD and self.currToken.value == "for":
                            res.reg_adv()
                            self.advance()
                            if self.currToken.type == TOKEN_SEMI:
                                res.reg_adv()
                                self.advance()
                                return res.success(ForNode(var, conditional, statements))
                            else:
                                return res.fail(InvalidSyntax(self.currToken.line, "Expected ';' after for"))
                        else:
                            return res.fail(InvalidSyntax(self.currToken.line, "'for' keyword expected after 'end' keyword"))
                    else:
                        return res.fail(InvalidSyntax(self.currToken.line, "for loops must end with 'end' keyword"))
                else:
                    return res.fail(InvalidSyntax(self.currToken.line, "Expected an ')' after iteration expression"))
            else:
                return res.fail(InvalidSyntax(self.currToken.line, "Expected a '('"))
        else:
            return res.fail(InvalidSyntax(curr.line, "Expected the for keyword"))


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
        while self.currToken.type in [TOKEN_DIVIDE, TOKEN_MULTIPLY, TOKEN_BAND, TOKEN_BOR, TOKEN_BNOT]:
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

        if curr.type == TOKEN_INTLITERAL:
            res.reg_adv()
            self.advance()
            return res.success(IntNode(curr))

        elif curr.type == TOKEN_FLOATLITERAL:
            res.reg_adv()
            self.advance()
            return res.success(FloatNode(curr))

        elif curr.type in [TOKEN_STRLITERAL]:
            res.reg_adv()
            self.advance()
            return res.success(StringNode(curr))

        elif curr.type in [TOKEN_BOOLLITERAL]:
            res.reg_adv()
            self.advance()
            return res.success(BooleanNode(curr))

        elif curr.type in [TOKEN_IDENTIFIER]:
            identifier = curr
            res.reg_adv()
            self.advance()
            if self.currToken.type == TOKEN_LPAREN:
                res.reg_adv()
                self.advance()
                expression = None
                if self.currToken.type != TOKEN_RPAREN:
                    expression = res.reg(self.expression())
                    if res.error:
                        return res
                if self.currToken.type == TOKEN_RPAREN:
                    res.reg_adv()
                    self.advance()
                    return res.success(FunctionAccessNode(identifier, expression))
                else:
                    return res.fail(InvalidSyntax(self.currToken.line, "Excpected a ')'"))
            if self.currToken.type == TOKEN_LBRACKET:
                res.reg_adv()
                self.advance()
                if self.currToken.type == TOKEN_INTLITERAL:
                    index = self.currToken
                    res.reg_adv()
                    self.advance()
                    if self.currToken.type == TOKEN_RBRACKET:
                        res.reg_adv()
                        self.advance()
                        return res.success(VariableAccessNode(identifier, index))
                    else:
                        return res.fail(InvalidSyntax(self.currToken.line, "Excpected a ']'"))
                else:
                    return res.fail(InvalidSyntax(self.currToken.line, "Excpected an integer access index"))
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