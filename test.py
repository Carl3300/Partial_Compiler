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
        # Assuming the AST is already constructed and available.
        # The AST could be represented in different ways based on the parser used.
        self.visit(ast)

    def visit(self, node):
        if isinstance(node, AssignNode):
            self.visit_assignment(node)
        elif isinstance(node, BinOpNode):
            return self.visit_bin_op(node)
        elif isinstance(node, IntNode):
            return "int"
        elif isinstance(node, FunctionDefNode):
            self.visit_function_def(node)
        elif isinstance(node, FunctionCallNode):
            return self.visit_function_call(node)
        else:
            self.errors.append(f"Unknown node type: {type(node).__name__}")
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


# AST Node Definitions (for illustration purposes)
class AssignNode:
    def __init__(self, left, right):
        self.left = left
        self.right = right


class BinOpNode:
    def __init__(self, left, operator, right):
        self.left = left
        self.operator = operator
        self.right = right


class IntNode:
    def __init__(self, value):
        self.value = value


class FunctionDefNode:
    def __init__(self, name, return_type, body):
        self.name = name
        self.return_type = return_type
        self.body = body


class FunctionCallNode:
    def __init__(self, name, args):
        self.name = name
        self.args = args


if __name__ == "__main__":
    # Sample AST for the program
    ast = [
        FunctionDefNode(name="add", return_type="int", body=[]),
        FunctionDefNode(name="main", return_type=None, body=[
            AssignNode(left=IntNode("x"), right=IntNode(10)),
            AssignNode(left=IntNode("y"), right=IntNode(5)),
            AssignNode(left=IntNode("result"), right=FunctionCallNode(name="add", args=[IntNode("x"), IntNode("y")])),
            FunctionCallNode(name="print", args=[IntNode("result")]),
        ])
    ]

    analyzer = SemanticAnalyzer()
    for node in ast:
        analyzer.analyze(node)

    if analyzer.errors:
        for error in analyzer.errors:
            print("Error:", error)
    else:
        print("Semantic analysis completed successfully.")