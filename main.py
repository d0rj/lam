from lam.transformer import ToDictTransformer
from lam.parser import parse


def main() -> None:
    with open('./examples/hello_world.l') as file:
        programm = file.read()
    tree = parse(programm)

    new_tree = ToDictTransformer().transform(tree)
    for l in new_tree:
        print(l, '\n')


if __name__ == '__main__':
    main()
