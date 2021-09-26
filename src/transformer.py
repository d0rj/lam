from lark import Transformer

from src.utils import flatten


class ToDictTransformer(Transformer):
    def programm(self, s):
        return s

    def expr(self, s):
        return s

    def infix(self, s):
        return {'infix': {'operation': s[1], 'arguments': [s[0], s[2]]}}

    def infix_operator(self, s):
        return s[0]

    def OPERATOR(self, s):
        return {'operator': str(s)}

    def bracket_expr(self, s):
        return s[0]

    def lambd(self, s):
        return {'lambda': {'arguments': s[0], 'body': s[1]}}

    def body(self, s):
        return s[0]

    def assign(self, s):
        return {'assign': {'variable': s[0], 'arguments': s[1], 'expr': s[2]}}

    def arguments(self, s):
        return list(s)

    def NAME(self, s):
        return {'name': str(s)}

    def TYPE_NAME(self, s):
        return {'type_name': str(s)}

    def type(self, s):
        return {'type': s[0]}

    def typed_var(self, s):
        return {'typed_var': {'var': s[0], 'with_type': s[1]}}

    def imp_type(self, s):
        return {'imp_type': {'left': s[0], 'right': s[1]}}

    def tupled_type(self, s):
        return {'tupled_type': s[0]}

    def list_like(self, s):
        return s

    def tuple(self, s):
        return {'tuple': s}

    def list(self, s):
        return {'list': flatten(s[0])}

    def var_name(self, s):
        return {'var_name': s[0]}

    def number(self, s):
        return {'number': float(str(s[0]))}

    def string(self, s):
        return {'string': str(s[0])}

    def value(self, s):
        return {'value': s[0]}

    def strict_varname(self, s):
        return s[0]

    def dotted_varname(self, s):
        if len(s) == 1:
            return {'dotted_varname': [s[0]]}
        return {'dotted_varname': [s[0]] + s[1]['dotted_varname']}

    def import_(self, s):
        if len(s) == 1:
            return {'import': s[0]}
        else:
            return {'import': s[0], 'as': s[1]}
