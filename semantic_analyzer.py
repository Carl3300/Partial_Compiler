# Type Operations
from code_parser import BinaryOpNode, BooleanNode, ElseNode, FloatNode, ForNode, FunctionAccessNode, FunctionDefinitionNode, GlobalFunctionDefinitionNode, GlobalVariableCreationNode, IfNode, IntNode, ProgramNode, ReturnNode, StringNode, UnaryOpNode, VariableAccessNode, VariableAssignmentNode, VariableCreationNode
from error import InvalidSemantics, ProgramError
from tokenizer import Token

# math ops
TOKEN_PLUS = 'PLUS'
TOKEN_MINUS = 'MINUS'
TOKEN_MULTIPLY = 'MULTIPLY'
TOKEN_DIVIDE = 'DIVIDE'
TOKEN_BAND = 'BAND'
TOKEN_BOR = 'BOR'
TOKEN_BNOT = 'BNOT'

# conditional ops
TOKEN_EQ = 'EQ'
TOKEN_LTHAN = 'LTHAN'
TOKEN_GTHAN = 'GTHAN'
TOKEN_GEQ = 'GEQ'
TOKEN_LEQ = 'LEQ'
TOKEN_NOT = 'NOT'

STRING = "string"
BOOL = "bool"
INT = "integer"
FLOAT = "float"
# Symbol Table Definition
class SymbolTable:
    def __init__(self):
        self.scopes = [{}]
        self.functionScopes = [{}]
        self.tier = 0
        self.define_base_functions()
        self.current_func_type = None
        self.function_type_stack = []

    def add_symbol(self, name, data_type, is_global=False):
        if is_global:
            self.scopes[0][name] = data_type
        else:
            self.scopes[-1][name] = data_type

    def add_function_symbol(self, name, data_type):
        self.functionScopes[-1][name] = data_type

    def get_symbol_type(self, name):
        for scope in reversed(self.scopes):
            if name in scope:
                return scope[name]
        return None

    def get_function_symbol_type(self, name):
        for scope in reversed(self.functionScopes):
            if name in scope:
                return scope[name]
        return None

    def get_global_declarations(self, name):
        try:
           return self.scopes[0][name]
        except KeyError:
            return None

    def enter_scope(self):
        self.scopes.append({})
        self.functionScopes.append({})

    def leave_scope(self):
        if len(self.scopes) > 1:
            return self.scopes.pop()
        if len(self.functionScopes) > 1:
            return self.functionScopes.pop()
        
    def define_base_functions(self):
        self.add_symbol("getbool", BOOL, True)
        self.add_symbol("getinteger", INT, True)
        self.add_symbol("getfloat", FLOAT, True)
        self.add_symbol("getstring", STRING, True)
        self.add_symbol("pubool", BOOL, True)
        self.add_symbol("putinteger", BOOL, True)
        self.add_symbol("putfloat", BOOL, True)
        self.add_symbol("putstring", BOOL, True)
        self.add_symbol("sqrt", FLOAT, True)
        # variable definitions
        self.add_function_symbol("getbool", None)
        self.add_function_symbol("getinteger", None)
        self.add_function_symbol("getfloat", None)
        self.add_function_symbol("getstring", None)
        self.add_function_symbol("pubool", BOOL)
        self.add_function_symbol("putinteger", INT)
        self.add_function_symbol("putfloat", FLOAT)
        self.add_function_symbol("putstring", STRING)
        self.add_function_symbol("sqrt", INT)

class SemanticAnalyzer:
    def __init__(self):
        self.symbol_table = SymbolTable()
        self.errors = []

    def analyze(self, ast):
        self.visit(ast)

    def visit(self, node):
        if isinstance(node, IntNode):
            return INT
        elif isinstance(node, FloatNode):
            return FLOAT
        elif isinstance(node, StringNode):
            return STRING
        elif isinstance(node, BooleanNode):
            return BOOL
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
        elif isinstance(node, GlobalFunctionDefinitionNode):
            return self.visit_globalFunctionDefinitionNode(node)
        elif isinstance(node, FunctionAccessNode):
            return self.visit_functionAccessNode(node)
        elif isinstance(node, ReturnNode):
            return self.visit_returnNode(node)
        elif isinstance(node, ProgramNode):
            return self.visit_programNode(node)
        else:
            self.errors.append(ProgramError(node, f"Compiler Error Unexpected Parse Result"))
            return None

    def visit_binaryOpNode(self, node):
        left = self.visit(node.left)
        operator = node.op_tok.type
        right = self.visit(node.right)

        if isinstance(left, list):
            if left[0] == "Array":
                left = left[1]
        if isinstance(right, list):
            if right[0] == "Array":
                right = right[1]

        if operator in [TOKEN_PLUS, TOKEN_MINUS, TOKEN_MULTIPLY, TOKEN_DIVIDE]:
            if left == INT and right == INT:
                return INT
            elif left == FLOAT and right == FLOAT:
                return FLOAT
            elif left == INT and right == FLOAT:
                return FLOAT
            elif left == FLOAT and right == INT:
                return FLOAT
            else:
                self.errors.append(ProgramError(node.op_tok.line, f"Type mismatch cannot perform arithmetic operations of type {left} and type {right}. Only floats and integers are allowed"))
                return None
        elif operator in [TOKEN_BAND, TOKEN_BOR, TOKEN_BNOT]:
            if left == INT and right == INT:
                return INT
            else:
                self.errors.append(ProgramError(node.op_tok.line, f"Type mismatch cannot perform logical operations of type {left} and type {right}. Only type integer is allowed"))
                return None
        elif operator in [TOKEN_EQ, TOKEN_NOT]:
            if left == BOOL and right == INT:
                return BOOL
            elif left == INT and right == BOOL:
                return BOOL
            elif left == FLOAT and right == INT:
                return BOOL
            elif left == INT and right == FLOAT:
                return BOOL
            elif left == right:
                return BOOL
            else:
                self.errors.append(ProgramError(node.op_tok.line, f"Type mismatch cannot compare type {left} with type {right}"))
                return None
        elif operator in [TOKEN_GTHAN, TOKEN_LTHAN, TOKEN_GEQ, TOKEN_LEQ]:
            if left == BOOL and right == INT:
                return BOOL
            elif left == INT and right == BOOL:
                return BOOL
            elif left == FLOAT and right == INT:
                return BOOL
            elif left == INT and right == FLOAT:
                return BOOL
            elif left == STRING or right == STRING:
                self.errors.append(ProgramError(node.op_tok.line, f"Type mismatch cannot perform string comparisons of >, >=, <, <="))
                return None
            elif left == right:
                return BOOL
            else:
                self.errors.append(ProgramError(node.op_tok.line, f"Type mismatch cannot compare type {left} with type {right}"))
                return None
        else:
            self.errors.append(ProgramError(node.op_tok.line, f"Compiler Error Unexpected a operator token"))
            return None

    def visit_unaryOpNode(self, node):
        type_ = self.visit(node.node)
        if type_ in [STRING, BOOL]:
            self.errors.append(InvalidSemantics(node.op_token.line, f"Cannot assign negative value to boolean or string"))
            return type_
        return type_

    def visit_variableAssignmentNode(self, node):    
        variableType = self.symbol_table.get_symbol_type(node.identifierToken.value)
        if not variableType:
            self.errors.append(InvalidSemantics(node.identifierToken.line, f"Variable referenced before assignment"))
            return
        
        type_assigned = self.visit(node.valueToken)
        if isinstance(variableType, list):
            size = variableType[2]
            if int(node.index.value) > int(size.value):
                self.errors.append(InvalidSemantics(node.identifierToken.line, f"Index out of range for list"))
                return
            if node.index.value:
                variableType = variableType[1]
        
        if variableType == INT and type_assigned == FLOAT:
            return INT
        elif variableType == FLOAT and type_assigned == INT:
            return FLOAT
        elif variableType == INT and type_assigned == BOOL:
            return INT
        elif variableType == BOOL and type_assigned == INT:
            return BOOL
        elif variableType == type_assigned:
            return variableType
        else:
            self.errors.append(InvalidSemantics(node.identifierToken.line, f"Expected variable assignment of type {variableType} but got type {type_assigned}"))
            return

    def visit_variableCreationNode(self, node):
        variable_identifier = node.identifierToken.value
        variable_type = node.type.value
        if node.isList:
            if not node.size:
                self.errors.append(InvalidSemantics(node.identifierToken.line, f"List size integer needed"))
                return
            self.symbol_table.add_symbol(variable_identifier, ["Array", variable_type, node.size])
            return ["Array", variable_type, node.size]
        else:
            self.symbol_table.add_symbol(variable_identifier, variable_type)
            return variable_type
    
    def visit_globalVariableCreationNode(self, node):
        global_variable_identifier = node.identifierToken.value
        global_variable_type = node.type
        nameTaken = self.symbol_table.get_global_declarations(global_variable_identifier)
        if node.isList:
            if not node.size:
                self.errors.append(InvalidSemantics(node.identifierToken.line, f"List size integer needed"))
                return
            self.symbol_table.add_symbol(global_variable_identifier, ["Array", global_variable_type, node.size])
            return ["Array", global_variable_type, node.size]
        else:
            if nameTaken:
                self.errors.append(InvalidSemantics(node.identifierToken.line, f"Names can only be used once for global declarations"))
                return
            self.symbol_table.add_symbol(global_variable_identifier, global_variable_type.value, True)

    def visit_variableAccessNode(self, node):
        variableType = self.symbol_table.get_symbol_type(node.identifierToken.value)
        if not variableType:
            self.errors.append(InvalidSemantics(node.identifierToken.line, f"Variable referenced before assignment"))
            return None
        if node.index:
            return variableType[1]
        return variableType

    def visit_ifNode(self, node):
        conditional = self.visit(node.conditional)
        if conditional != BOOL:
            self.errors.append(InvalidSemantics(node.identifierToken.line, f"Condtional must be of type Boolean for a if statement"))
            return
        if node.body:
            for statement in node.body:
                self.visit(statement)
        if node.otherNode:
                self.visit(node.otherNode)
        
    def visit_elseNode(self, node):
        if node.body:
            for statement in node.body:
                self.visit(statement)
    
    def visit_forNode(self, node):
        self.symbol_table.enter_scope()
        self.visit(node.variable)
        conditional = self.visit(node.conditional)
        if conditional != BOOL:
            self.errors.append(InvalidSemantics(node.line, f"Condtional must be of type Boolean for a if statement"))
            self.symbol_table.leave_scope()
            return None
        if node.body:
            for statement in node.body:
                self.visit(statement)
        self.symbol_table.leave_scope()

    def visit_functionDefinition(self, node):
        function_name = node.identifier.value
        type_ = node.type.value
        self.symbol_table.add_symbol(function_name, type_)

        types = []
        if node.variables:
            for var in node.variables:
                if var.isList:
                    if not var.size:
                        self.errors.append(InvalidSemantics(node.identifierToken.line, f"List size integer needed"))
                        return
                    types.append(["Array", var.type.value, var.size])
                else:
                    types.append(var.type.value)
        self.symbol_table.add_function_symbol(function_name, types)
        self.symbol_table.current_func_type = type_
        self.symbol_table.function_type_stack.append(type_)
        self.symbol_table.enter_scope()

        if node.variables:
            for var in node.variables:
                self.visit(var)

        if node.declarations:
            for definition in node.declarations:
                self.visit(definition)

        if node.statements:
            for statement in node.statements:
                self.visit(statement)

        self.symbol_table.leave_scope()

    def visit_globalFunctionDefinitionNode(self, node):
        function_name = node.identifier.value
        type_ = node.type.value
        self.symbol_table.add_symbol(function_name, type_, True)

        types = []
        if node.variables:
            for var in node.variables:
                if var.isList:
                    if not var.size:
                        self.errors.append(InvalidSemantics(node.identifierToken.line, f"List size integer needed"))
                        return
                    types.append(["Array", var.type.value, var.size])
                else:
                    types.append(var.type.value)
        self.symbol_table.add_function_symbol(function_name, types)
        self.symbol_table.current_func_type = type_
        self.symbol_table.function_type_stack.append(type_)
        self.symbol_table.enter_scope()

        if node.variables:
            for var in node.variables:
                self.visit(var)

        if node.declarations:
            for definition in node.declarations:
                self.visit(definition)

        if node.statements:
            for statement in node.statements:
                self.visit(statement)

        self.symbol_table.leave_scope()

    def visit_functionAccessNode(self, node):
        function_type = self.symbol_table.get_symbol_type(node.identifier.value)
        if not function_type:
            self.errors.append(InvalidSemantics(node.identifier.line, f"Function referenced before assignment"))
            return

        func_var_types = self.symbol_table.get_function_symbol_type(node.identifier.value)
        need_list =  isinstance(func_var_types, list)
        var_types = []
        if node.variables:
            if isinstance(node.variables, list):
                for var in node.variables:
                   var_types.append(self.visit(var))
            elif need_list:
                var_types.append(self.visit(node.variables))
            else:
                var_types = self.visit(node.variables)
        else:
            var_types = None

        func_var_types = self.symbol_table.get_function_symbol_type(node.identifier.value)
        
        if func_var_types != var_types:
            self.errors.append(InvalidSemantics(node.identifier.line, f"Function call variables do not match typing of function declaration"))
            return
        elif isinstance(function_type, list):
            return function_type[0]
        else:
            return function_type

    def visit_returnNode(self, node):
        expression = self.visit(node.expression)
        if not self.symbol_table.current_func_type:
            self.errors.append(InvalidSemantics(node.line, f"Return statement used before function definition"))
            return
        if expression != self.symbol_table.current_func_type:
            self.errors.append(InvalidSemantics(node.line, f"Return statement statement type {expression} does not match function type {self.symbol_table.current_func_type}"))
            return
        return expression

    def visit_programNode(self, node):
        self.symbol_table.add_symbol(node.identifier.value, "Main Program", True)
        program_declarations = node.declarations
        program_statements = node.statements

        if program_declarations:
            for definition in program_declarations:
                self.visit(definition)
        if program_statements:
            for statement in program_statements:
                self.visit(statement)

def Analyze_Code(ast):
    analyzer = SemanticAnalyzer()
    analyzer.analyze(ast)

    if analyzer.errors:
        for error in analyzer.errors:
            print("Error:", error)
    else:
        return True