from inspect import isfunction, signature
from types import BuiltinFunctionType

from src.transformer import ToDictTransformer
from src.parser import parse
from src.translater import translate


def main() -> None:
    tree = parse('./examples/hello_world.l')

    new_tree = ToDictTransformer().transform(tree)

    for line in translate(new_tree):
        print(line)


if __name__ == '__main__':
    main()
