from lark import Lark, Transformer


class ToDictTransformer(Transformer):
    def infix(self, s):
        return { 'infix': s[1], 'arguments': [s[0], s[2]] }

    def infix_operator(self, s):
        return str(s[0])

    def OPERATOR(self, s):
        return str(s)

    def bracket_expr(self, s):
        return s[0]

    def lambd(self, s):
        return {'lambda': {'arguments': s[0], 'body': s[1]}}

    def arguments(self, s):
        return list(s)

    def NAME(self, s):
        return {'name': str(s)}

    def var_name(self, s):
        return {'var_name': s[0]}

    def number(self, s):
        return {'number': float(str(s[0]))}

    def value(self, s):
        return {'value': s[0]}


def main() -> None:
    parser = Lark.open('lambda.lark', parser='lalr', start='programm', rel_to=__file__)

    with open('programm.l', 'r') as file:
        programm = file.read()

    tree = parser.parse(programm)

    print(tree.pretty())
    print('---')
    print(ToDictTransformer().transform(tree).pretty())


if __name__ == '__main__':
    main()
