from src.transformer import ToDictTransformer
from src.parser import parse


def main() -> None:
    tree = parse('./examples/hello_world.l')
    parse('./examples/all_features.l')

    new_tree = ToDictTransformer().transform(tree)
    for l in new_tree:
        print(l, '\n')


if __name__ == '__main__':
    main()
