from code_parser import BinaryOpNode, BooleanNode, ElseNode, FloatNode, ForNode, FunctionAccessNode, FunctionDefinitionNode, GlobalFunctionDefinitionNode, GlobalVariableCreationNode, IfNode, IntNode, ProgramNode, ReturnNode, StringNode, UnaryOpNode, VariableAccessNode, VariableAssignmentNode, VariableCreationNode
from error import InvalidCodeGeneration
import llvmlite.ir as ir # basic conversion to llvm the project description states basic translators are allowed


# Need to define Base funcitons and ensure their global use
class CodeGenerator:
    def __init__(self):
        self.module = ir.Module()
        self.errors = []
        self.kickOffCodeGen()

    def kickOffCodeGen(self):
        func_ty = ir.FunctionType(ir.VoidType(), []) # probably may need to add declarations
        main_func = ir.Function(self.module, func_ty, name="main")

    def generate(self):
        pass

    def generate_expr_ir(self, node, builder):
        if isinstance(node, IntNode):
            return ir.Constant(ir.IntType(32), node.value)

        elif isinstance(node, FloatNode):
            return ir.Constant(ir.FloatType(), node.value)

        elif isinstance(node, BooleanNode):
            return ir.Constant(ir.IntType(1), node.value)

        elif isinstance(node, StringNode):
            return ir.Constant(ir.PointerType(), node.value)

        elif isinstance(node, BinaryOpNode):
            left_val = self.generate_expr_ir(node.left, builder)
            right_val = self.generate_expr_ir(node.right, builder)

            pass # add in operations
        elif isinstance(node, UnaryOpNode):
            pass
        elif isinstance(node, VariableAssignmentNode):
            pass
        elif isinstance(node, VariableCreationNode):
            pass
        elif isinstance(node, GlobalVariableCreationNode):
            pass
        elif isinstance(node, VariableAccessNode):
            pass
        elif isinstance(node, IfNode):
            pass
        elif isinstance(node, ElseNode):
            pass
        elif isinstance(node, ForNode):
            pass
        elif isinstance(node, FunctionDefinitionNode):
            pass
        elif isinstance(node, GlobalFunctionDefinitionNode):
            pass
        elif isinstance(node, FunctionAccessNode):
            pass
        elif isinstance(node, ReturnNode):
            pass
        elif isinstance(node, ProgramNode):
            pass
        return  self.errors.append(InvalidCodeGeneration(node, "Compiler Error Unexpected Parse Result"))


def Generate_Code(ast):
    gen = CodeGenerator()
    gen.generate(ast) # add in genertion function