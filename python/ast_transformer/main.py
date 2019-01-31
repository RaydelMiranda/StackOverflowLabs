#!/usr/bin/env python
import ast
import os
from ast_transformer import AnalyserNodeTransformer

# instrument_node need to be in the namespace.
from ast_transformer import instrument_node

if __name__ == "__main__":

    target_path = os.path.join(os.path.dirname(__file__), 'target/target.py')

    with open(target_path, 'r') as program:
        # Read and parse the target script.
        tree = ast.parse(program.read())
        # Make transformations.
        tree = AnalyserNodeTransformer().visit(tree)
        # Fix locations.
        ast.fix_missing_locations(tree)
        # Compile and execute.
        compiled = compile(tree, filename='target.py', mode='exec')
        exec(compiled)