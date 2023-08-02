# Type Operations
from tokenizer import Token

#TypeAssignNode
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
            return f"List: {self.identifierToken.value}: {self.type} - Size: {self.size}"
        return f"{self.identifierToken.value}: {self.type}"

class VariableAccessNode(): # this is for variable identifiers
    def __init__(self, identifierToken , index=None) -> None:
        self.identifierToken = identifierToken
        self.index = index
    def __repr__(self) -> str:
        if self.index:
            return f"{self.identifierToken.value} at element {self.index}"
        return f"{self.identifierToken.value}"

class IfNode():
    def __init__(self, conditional, body, otherNodes) -> None:
        self.conditional = conditional
        self.body = body
        self.otherNodes = otherNodes
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

# List Node
class ListNode():
    def __init__(self, elements) -> None:
        self.elements = elements
    def __repr__(self) -> str:
        return f"{self.elements}"

# Functions
class FunctionDefinitionNode():
    def __init__(self, identifier, type_, procedure_list, statement_list) -> None:
        self.declarations = procedure_list
        self.statements = statement_list
        self.identifier = identifier
        self.type = type_
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
    def __init__(self, procedure_list, statement_list) -> None:
        self.declarations = procedure_list
        self.statements = statement_list
    def __repr__(self) -> str:
        return f"{self.declarations}: {self.statements}"

# Symbol Table Definition
class SymbolTable:
    def __init__(self):
        self.symbols = {}

    def add_symbol(self, name, data_type):
        self.symbols[name] = data_type

    def get_symbol_type(self, name):
        return self.symbols.get(name)


class SemanticAnalyzer:
    def __init__(self):
        self.symbol_table = SymbolTable()
        self.errors = []

    def analyze(self, ast):
        self.visit(ast)

    def visit(self, node):
        if isinstance(node, IntNode):
            pass
        elif isinstance(node, FloatNode):
            pass
        elif isinstance(node, StringNode):
            pass
        elif isinstance(node, BooleanNode):
            pass
        elif isinstance(node, BinaryOpNode):
            pass
        elif isinstance(node, UnaryOpNode):
            pass
        elif isinstance(node, VariableAssignmentNode):
            pass
        elif isinstance(node, VariableCreationNode):
            pass
        elif isinstance(node, VariableAccessNode):
            pass
        elif isinstance(node, IfNode):
            pass
        elif isinstance(node, ElseNode):
            pass
        elif isinstance(node, ForNode):
            pass
        elif isinstance(node, ListNode):
            pass
        elif isinstance(node, FunctionDefinitionNode):
            pass
        elif isinstance(node, FunctionAccessNode):
            pass
        elif isinstance(node, ReturnNode):
            pass
        elif isinstance(node, ProgramNode):
            pass
        else:
            self.errors.append(f"Node Handling Not Implimented Yet")
            return None

    def visit_assignment(self, node):
        var_name = node.left.value
        var_type = self.visit(node.right)
        self.symbol_table.add_symbol(var_name, var_type)

    def visit_bin_op(self, node):
        left_type = self.visit(node.left)
        right_type = self.visit(node.right)
        operator = node.operator

        if left_type != "int" or right_type != "int":
            self.errors.append(f"Invalid types for '{operator}': {left_type} and {right_type}")
            return None

        # Return the result type of the binary operation (int in this case)
        return "int"

    def visit_function_def(self, node):
        # Store function name and return type in the symbol table
        func_name = node.name
        return_type = node.return_type
        self.symbol_table.add_symbol(func_name, return_type)

        # Visit the function body to analyze it
        for statement in node.body:
            self.visit(statement)

    def visit_function_call(self, node):
        func_name = node.name
        # Lookup the function name in the symbol table to check if it's defined
        func_return_type = self.symbol_table.get_symbol_type(func_name)
        if func_return_type is None:
            self.errors.append(f"Function '{func_name}' is not defined.")
            return None

        # Check the number of arguments and their types
        func_args = node.args
        # Assuming all arguments are of type int for simplicity
        for arg in func_args:
            arg_type = self.visit(arg)
            if arg_type != "int":
                self.errors.append(f"Invalid argument type for function '{func_name}'.")
                return None

        return func_return_type

def Analyze_Code(ast):
    analyzer = SemanticAnalyzer()
    for node in ast:
        analyzer.analyze(node)

    if analyzer.errors:
        for error in analyzer.errors:
            print("Error:", error)
    else:
        return True