# Sample tokens list for the more complex C program
tokens = [
    ('INT', 'int'),
    ('IDENTIFIER', 'main'),
    ('LPAREN', '('),
    ('RPAREN', ')'),
    ('LBRACE', '{'),
    ('INT', 'int'),
    ('IDENTIFIER', 'num'),
    ('SEMICOLON', ';'),
    ('IDENTIFIER', 'num2'),
    ('ASSIGN', '='),
    ('INTEGER_LITERAL', 10),
    ('SEMICOLON', ';'),
    ('IF', 'if'),
    ('LPAREN', '('),
    ('IDENTIFIER', 'num'),
    ('GREATER', '>'),
    ('INTEGER_LITERAL', 5),
    ('RPAREN', ')'),
    ('LBRACE', '{'),
    ('IDENTIFIER', 'num2'),
    ('ASSIGN', '='),
    ('INTEGER_LITERAL', 100),
    ('SEMICOLON', ';'),
    ('RBRACE', '}'),
    ('ELSE', 'else'),
    ('LBRACE', '{'),
    ('IDENTIFIER', 'num2'),
    ('ASSIGN', '='),
    ('INTEGER_LITERAL', 200),
    ('SEMICOLON', ';'),
    ('RBRACE', '}'),
    ('WHILE', 'while'),
    ('LPAREN', '('),
    ('IDENTIFIER', 'num'),
    ('LESS', '<'),
    ('INTEGER_LITERAL', 10),
    ('RPAREN', ')'),
    ('LBRACE', '{'),
    ('IDENTIFIER', 'num'),
    ('ASSIGN', '='),
    ('IDENTIFIER', 'num'),
    ('PLUS', '+'),
    ('INTEGER_LITERAL', 1),
    ('SEMICOLON', ';'),
    ('RBRACE', '}'),
    ('IDENTIFIER', 'print'),
    ('LPAREN', '('),
    ('STRING_LITERAL', 'Result: %d\n'),
    ('COMMA', ','),
    ('IDENTIFIER', 'num2'),
    ('RPAREN', ')'),
    ('SEMICOLON', ';'),
    ('RETURN', 'return'),
    ('INTEGER_LITERAL', 0),
    ('SEMICOLON', ';'),
    ('RBRACE', '}'),
]

global index

def print_ast(node, indent=0):
    if isinstance(node, BinaryOpNode):
        print(' ' * indent + 'BinaryOpNode:', node.operator)
        print_ast(node.left, indent + 2)
        print_ast(node.right, indent + 2)
    elif isinstance(node, IdentifierNode):
        print(' ' * indent + 'IdentifierNode:', node.name)
    elif isinstance(node, IntegerLiteralNode):
        print(' ' * indent + 'IntegerLiteralNode:', node.value)
    elif isinstance(node, IfElseNode):
        print(' ' * indent + 'IfElseNode')
        print_ast(node.condition, indent + 2)
        print_ast(node.if_block, indent + 2)
        if node.else_block:
            print(' ' * indent + 'Else')
            print_ast(node.else_block, indent + 2)
    elif isinstance(node, WhileLoopNode):
        print(' ' * indent + 'WhileLoopNode')
        print_ast(node.condition, indent + 2)
        print_ast(node.body, indent + 2)
    elif isinstance(node, FunctionCallNode):
        print(' ' * indent + 'FunctionCallNode:', node.name)
        for arg in node.arguments:
            print_ast(arg, indent + 2)
    else:
        raise ValueError("Unknown AST Node type")


# AST Node classes (updated to handle more constructs)
class ASTNode:
    pass

class BinaryOpNode(ASTNode):
    def __init__(self, operator, left, right):
        self.operator = operator
        self.left = left
        self.right = right

class IdentifierNode(ASTNode):
    def __init__(self, name):
        self.name = name

class IntegerLiteralNode(ASTNode):
    def __init__(self, value):
        self.value = value

class IfElseNode(ASTNode):
    def __init__(self, condition, if_block, else_block):
        self.condition = condition
        self.if_block = if_block
        self.else_block = else_block

class WhileLoopNode(ASTNode):
    def __init__(self, condition, body):
        self.condition = condition
        self.body = body

class FunctionCallNode(ASTNode):
    def __init__(self, name, arguments):
        self.name = name
        self.arguments = arguments

# Updated parse_expression function to handle if-else and while constructs
def parse_expression(tokens):
    def term():
        global index
        left = factor()
        while index < len(tokens) and tokens[index][0] in {'MULTIPLY', 'DIVIDE'}:
            operator = tokens[index][0]
            index += 1
            right = factor()
            left = BinaryOpNode(operator, left, right)
        return left

    def factor():
        global index
        token_type, value = tokens[index]
        index += 1
        if token_type == 'IDENTIFIER':
            return IdentifierNode(value)
        elif token_type == 'INTEGER_LITERAL':
            return IntegerLiteralNode(value)
        elif token_type == 'LPAREN':
            result = parse_expression(tokens)
            index += 1  # Move past the RPAREN
            return result
        else:
            raise ValueError("Unexpected token: " + token_type)

    index = 0
    return term()

def parse_statement(tokens):
    global index
    if tokens[index][0] == 'INT':
        index += 1  # Move past 'int'
        var_name = tokens[index][1]
        index += 1  # Move past identifier
        if tokens[index][0] == 'ASSIGN':
            index += 1  # Move past '='
            value = parse_expression(tokens)
            if tokens[index][0] == 'SEMICOLON':
                index += 1  # Move past ';'
                return BinaryOpNode('=', IdentifierNode(var_name), value)
            else:
                raise ValueError("Expected ';'")
        else:
            raise ValueError("Unexpected token after variable declaration")
    elif tokens[index][0] == 'IF':
        index += 1  # Move past 'if'
        if_condition = parse_expression(tokens)
        if_block = parse_statement(tokens)
        else_block = None
        if tokens[index][0] == 'ELSE':
            index += 1  # Move past 'else'
            else_block = parse_statement(tokens)
        return IfElseNode(if_condition, if_block, else_block)
    elif tokens[index][0] == 'WHILE':
        index += 1  # Move past 'while'
        loop_condition = parse_expression(tokens)
        loop_body = parse_statement(tokens)
        return WhileLoopNode(loop_condition, loop_body)
    elif tokens[index][0] == 'IDENTIFIER':
        func_name = tokens[index][1]
        index += 1  # Move past identifier
        if tokens[index][0] == 'LPAREN':
            index += 1  # Move past '('
            arguments = []
            if tokens[index][0] != 'RPAREN':
                while True:
                    argument = parse_expression(tokens)
                    arguments.append(argument)
                    if tokens[index][0] == 'RPAREN':
                        break
                    elif tokens[index][0] == 'COMMA':
                        index += 1  # Move past ','
                    else:
                        raise ValueError("Expected ')' or ','")
                index += 1  # Move past ')'
            else:
                index += 1  # Move past ')'
            if tokens[index][0] == 'SEMICOLON':
                index += 1  # Move past ';'
                return FunctionCallNode(func_name, arguments)
            else:
                raise ValueError("Expected ';'")
        else:
            raise ValueError("Unexpected token after function name")
    else:
        raise ValueError("Unexpected token in statement")

def parse_c_code(tokens):
    statements = []
    global index
    index = 0 # Initialize the index for parsing
    while index < len(tokens):
        statement = parse_statement(tokens)
        statements.append(statement)
    return statements

# Test the parser
result_ast = parse_c_code(tokens)

# Print the AST
print_ast(result_ast)