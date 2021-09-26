from lark import Lark
from lark.tree import Tree


def parse(source: str) -> Tree:
    parser = Lark.open(
        '../lambda.lark',
        parser='lalr',
        start='programm',
        rel_to=__file__
    )

    tree = parser.parse(source)

    return tree
