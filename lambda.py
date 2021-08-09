from lark import Lark


def main() -> None:
    parser = Lark.open('lambda.lark', parser='lalr', start='programm', rel_to=__file__)

    with open('programm.l', 'r') as file:
        programm = file.read()

    tree = parser.parse(programm)

    print(tree.pretty())


if __name__ == '__main__':
    main()
