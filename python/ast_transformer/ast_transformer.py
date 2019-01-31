import ast
import parser

def instrument_node(value):
    VarType = type(value)
    class AnalyserHelper(VarType):
        def __init__(self, *args, **kwargs):
            self.hidden_field = (0, 0)
            super(AnalyserHelper, self).__init__(*args, **kwargs)
    return AnalyserHelper(value)


class AnalyserNodeTransformer(ast.NodeTransformer):
    """Wraps all dicts in a call to instrument_node()"""
    def visit_Dict(self, node):
        return ast.Call(func=ast.Name(id='instrument_node', ctx=ast.Load()),
                        args=[node], keywords=[])
        return node


