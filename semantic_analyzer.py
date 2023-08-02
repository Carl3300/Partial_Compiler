# Type Operations
from code_parser import BinaryOpNode, BooleanNode, ElseNode, FloatNode, ForNode, FunctionAccessNode, FunctionDefinitionNode, GlobalVariableCreationNode, IfNode, IntNode, ProgramNode, ReturnNode, StringNode, UnaryOpNode, VariableAccessNode, VariableAssignmentNode, VariableCreationNode
from tokenizer import Token

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
            return "integer"
        elif isinstance(node, FloatNode):
            return "float"
        elif isinstance(node, StringNode):
            return "string"
        elif isinstance(node, BooleanNode):
            return "bool"
        elif isinstance(node, BinaryOpNode):
            return self.visit_binaryOpNode(node)
        elif isinstance(node, UnaryOpNode):
            return self.visit_unaryOpNode(node)
        elif isinstance(node, VariableAssignmentNode):
            return self.visit_variableAssignmentNode(node)
        elif isinstance(node, VariableCreationNode):
            return self.visit_variableCreationNode(node)
        elif isinstance(node, GlobalVariableCreationNode):
            return self.visit_globalVariableCreationNode(node)
        elif isinstance(node, VariableAccessNode):
            return self.visit_variableAccessNode(node)
        elif isinstance(node, IfNode):
            return self.visit_ifNode(node)
        elif isinstance(node, ElseNode):
            return self.visit_elseNode(node)
        elif isinstance(node, ForNode):
            return self.visit_forNode(node)
        elif isinstance(node, FunctionDefinitionNode):
            return self.visit_functionDefinition(node)
        elif isinstance(node, FunctionAccessNode):
            return self.visit_functionAccessNode(node)
        elif isinstance(node, ReturnNode):
            return self.visit_returnNode(node)
        elif isinstance(node, ProgramNode):
            return self.visit_programNode(node)
        else:
            self.errors.append(f"Node Handling Not Implimented Yet")
            return None

    def visit_binaryOpNode(self, node):
        pass

    def visit_unaryOpNode(self, node):
        pass

    def visit_variableAssignmentNode(self, node):    
        pass 

    def visit_variableCreationNode(self, node):
        variable_identifier = node.identifierToken.value
        variable_type = node.type
        variable_isList = node.isList
        variable_size = node.size
        self.symbol_table.add_symbol(variable_identifier, variable_type)
        return variable_type
    
    def visit_globalVariableCreationNode(self, node):
        global_variable_identifier = node.identifierToken.value
        global_variable_type = node.type
        global_variable_isList = node.isList
        global_variable_size = node.size
        pass # ensure no overlapping globals 
        self.symbol_table.add_symbol(global_variable_identifier, global_variable_type)
        return global_variable_type

    def visit_variableAccessNode(self, node):
        pass

    def visit_ifNode(self, node):
        pass

    def visit_elseNode(self, node):
        pass

    def visit_forNode(self, node):
        pass

    def visit_functionDefinition(self, node):
        function_declarations = node.declarations
        function_statements = node.statement_list
        function_identifier = node.identifier.value
        function_type = node.type
        pass # ensure return type is correct, add global functions
        self.symbol_table.add_symbol(function_identifier, function_type)
        
        for definition in function_declarations:
            self.visit(definition)

        for statement in function_statements:
            self.visit(statement)

        return function_type

    def visit_functionAccessNode(self, node):
        pass

    def visit_returnNode(self, node):
        pass

    def visit_programNode(self, node):
        self.symbol_table.add_symbol(node.identifier.value, "Main Program")
        program_declarations = node.declarations
        program_statements = node.statements

        for definition in program_declarations:
            self.visit(definition)

        for statement in program_statements:
            self.visit(statement)
        return 0

def Analyze_Code(ast):
    analyzer = SemanticAnalyzer()
    analyzer.analyze(ast)

    if analyzer.errors:
        for error in analyzer.errors:
            print("Error:", error)
    else:
        return True