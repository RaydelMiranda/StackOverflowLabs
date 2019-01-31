#!/usr/bin/env python
import ast
from ast_transformer import AnalyserNodeTransformer

# instrument_node need to be in the namespace.
from ast_transformer import instrument_node

if __name__ == "__main__":
    with open('target/target.py', 'r') as program:
        # Read and parse the target script.
        tree = ast.parse(program.read())
        # Make transformations.
        tree = AnalyserNodeTransformer().visit(tree)
        # Fix locations.
        ast.fix_missing_locations(tree)
        # Compile and execute.
        compiled = compile(tree, filename='target/target.py', mode='exec')
        exec(compiled)