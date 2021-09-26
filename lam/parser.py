from lark import Lark
from lark.tree import Tree


def parse(file_name: str) -> Tree:
    parser = Lark.open(
        '../lambda.lark',
        parser='lalr',
        start='programm',
        rel_to=__file__
    )

    with open(file_name, 'r') as file:
        programm = file.read()
    tree = parser.parse(programm)

    return tree
