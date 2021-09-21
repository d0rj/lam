from src.transformer import ToDictTransformer
from src.parser import parse


def main() -> None:
    tree = parse('programm.l')

    new_tree = ToDictTransformer().transform(tree)
    [print(t, '\n') for t in new_tree]

    print('\n', new_tree[5])


if __name__ == '__main__':
    main()
