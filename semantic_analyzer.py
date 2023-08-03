# Type Operations
from code_parser import BinaryOpNode, BooleanNode, ElseNode, FloatNode, ForNode, FunctionAccessNode, FunctionDefinitionNode, GlobalVariableCreationNode, IfNode, IntNode, ProgramNode, ReturnNode, StringNode, UnaryOpNode, VariableAccessNode, VariableAssignmentNode, VariableCreationNode
from error import InvalidSemantics, ProgramError
from tokenizer import Token


# Symbol Table Definition
class SymbolTable:
    def __init__(self):
        self.scopes = [{}]
        self.define_base_functions()

    def add_symbol(self, name, data_type, is_global=False):
        if is_global:
            self.scopes[0][name] = data_type
        else:
            self.scopes[-1][name] = data_type

    def get_symbol_type(self, name):
        for scope in reversed(self.scopes):
            if name in scope:
                return scope[name]
        return None

    def get_global_declarations(self, name):
        return self.scopes[0][name]

    def enter_scope(self):
        self.scopes.append({})

    def leave_scope(self):
        if len(self.scopes) > 1:
            return self.scopes.pop()
        
    def define_base_functions(self):
        self.add_symbol("putBool", ["bool", "bool"])
        self.add_symbol("putInteger", ["bool", "integer"])
        self.add_symbol("putFloat", ["bool", "float"])
        self.add_symbol("putString", ["bool", "string"])
        self.add_symbol("sqrt", ["float", "integer"])

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
            self.errors.append(ProgramError(f"Compiler Error Unexpected Parse Result"))
            return None

    def visit_binaryOpNode(self, node):
        pass

    def visit_unaryOpNode(self, node):
        type_ = self.visit(node.node)
        if type_ in ["string", "bool"]:
            self.errors.append(InvalidSemantics(node.op_token.line, f"Cannot assign negative value to boolean or string"))
            return type_
        return type_

    def visit_variableAssignmentNode(self, node):    
        variableType = self.symbol_table.get_symbol_type(node.identifierToken.value)
        if not variableType:
            self.errors.append(InvalidSemantics(node.identifierToken.line, f"Variable referenced before assignment"))
            return None
        type_assigned = self.visit(node.valueToken)
        pass # add in int can be float and those semantics checks here
        if variableType != type_assigned:
            self.errors.append(InvalidSemantics(node.identifierToken.line, f"Expected variable assignment of type {variableType} but got type {type_assigned}"))
            return None   

    def visit_variableCreationNode(self, node):
        variable_identifier = node.identifierToken.value
        variable_type = node.type.value
        pass # list stuff
        self.symbol_table.add_symbol(variable_identifier, variable_type)
        return variable_type
    
    def visit_globalVariableCreationNode(self, node):
        global_variable_identifier = node.identifierToken.value
        global_variable_type = node.type
        nameTaken = self.symbol_table.get_global_declarations(global_variable_identifier)
        pass # list stuff
        if nameTaken:
            self.errors.append(InvalidSemantics(node.identifierToken.line, f"Names can only be used once for global declarations"))
            return None
        self.symbol_table.add_symbol(global_variable_identifier, global_variable_type, True)

    def visit_variableAccessNode(self, node):
        variableType = self.symbol_table.get_symbol_type(node.identifierToken.value)
        if not variableType:
            self.errors.append(InvalidSemantics(node.identifierToken.line, f"Variable referenced before assignment"))
            return None
        return variableType

    def visit_ifNode(self, node):
        pass

    def visit_elseNode(self, node):
        pass

    def visit_forNode(self, node):
        pass

    def visit_functionDefinition(self, node):
        function_name = node.identifier.value
        types = []
        types.append(node.type.value)

        self.symbol_table.add_symbol(function_name, types)
        self.symbol_table.enter_scope()

        if node.variables:
            for var in node.variables:
                types.append(self.visit(var))

        for definition in node.declarations:
            self.visit(definition)

        for statement in node.statements:
            self.visit(statement)

        self.symbol_table.leave_scope()
        self.symbol_table.add_symbol(function_name, types)

    def visit_functionAccessNode(self, node):
        variableType = self.symbol_table.get_symbol_type(node.identifier.value)

        if not variableType:
            self.errors.append(InvalidSemantics(node.identifierToken.line, f"Function referenced before assignment"))
            return None
        type_ = self.visit(node.variables) # modify so it can work with multiple variables in functions
        vars2 = variableType[1:]

        if vars2.__contains__(type_):
            self.errors.append(InvalidSemantics(node.identifierToken.line, f"Mismatched Function Type, type(s) expected: {variableType}; type(s) recieved: {type_}"))
            return variableType
        return variableType[0]

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

def Analyze_Code(ast):
    analyzer = SemanticAnalyzer()
    # ast = [ VariableCreationNode("integer", Token("IDENTIFIER", "a", 1)),
    #         VariableAssignmentNode((Token("IDENTIFIER", "a", 1)), (UnaryOpNode(Token("MINUS", "-", 1), FloatNode(Token("INTLITERAL", 5, 1)))))]
    # for a in ast:
    #     analyzer.analyze(a)

    analyzer.analyze(ast)

    if analyzer.errors:
        for error in analyzer.errors:
            print("Error:", error)
    else:
        return True