from src.transformer import ToDictTransformer
from src.parser import parse
from src.translater import translate


def main() -> None:
    tree = parse('programm.l')

    new_tree = ToDictTransformer().transform(tree)
    translate(new_tree)


if __name__ == '__main__':
    main()
