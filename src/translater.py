

def flatten(S: list):
    if S == []:
        return S
    if isinstance(S[0], list):
        return flatten(S[0]) + flatten(S[1:])
    return S[:1] + flatten(S[1:])


def translate_value(tree_value: dict) -> str:
    value = tree_value['value']
    if 'number' in value:
        return str(value['number'])
    elif 'string' in value:
        return str(value['string'])
    else:
        raise Exception('Wrong value type')


def translate_name(tree_name: dict) -> str:
    return tree_name['name']


def translate_operator(tree_operator: dict) -> str:
    return tree_operator['operator']


def translate_varname(tree_varname: dict) -> str:
    if 'name' in tree_varname['var_name']:
        return translate_name(tree_varname['var_name'])
    elif 'operator' in tree_varname['var_name']:
        return translate_operator(tree_varname['var_name'])
    else:
        raise Exception('Wrong variable name format')


def translate_assign(tree_assign: dict) -> str:
    assign = tree_assign['assign']

    var_name = assign['variable']
    arguments = assign['arguments']
    body = assign['expr'][0]

    var_name = translate_varname(var_name)
    arguments = [translate_name(arg) for arg in arguments]
    body = translate_expr(body)

    outer_lambdas = [f'lambda {argument}:' for argument in arguments]
    res = f"{var_name} = {''.join(outer_lambdas)} {body}"
    return res


def translate_dotted_varname(tree_dotted_varname: dict) -> str:
    names = []
    for var_name_obj in tree_dotted_varname:
        if 'var_name' in var_name_obj:
            names.append(translate_varname(var_name_obj))
        elif 'operator' in var_name_obj:
            names.append(var_name_obj['operator'])
        else:
            raise Exception(f'Wrong dotted varname object: {var_name_obj}')

    return '.'.join(names)


def translate_import(tree_import: dict) -> str:
    res = f"import {translate_dotted_varname(tree_import['import']['dotted_varname'])}"
    if 'as' in tree_import:
        res += f" as {tree_import['as']['var_name']['name']}"
    return res


def translate_lambda(tree_lambda: dict) -> str:
    lambda_ = tree_lambda['lambda']

    arguments = lambda_['arguments']
    body = lambda_['body']

    arguments = [translate_name(arg) for arg in arguments]
    outer_lambdas = [f'lambda {argument}:' for argument in arguments]
    body = translate_expr(body)

    return f"({''.join(outer_lambdas)} {body})"


def translate_infix(tree_infix: dict) -> str:
    infix = tree_infix['infix']
    operation = infix['operation']
    arguments = infix['arguments']

    arguments = [translate_expr(arg) for arg in arguments]

    if 'operator' in operation:
        operator = translate_operator(operation)
        return f'({arguments[0]}) {operator} ({arguments[1]})'
    if 'var_name' in operation and (not 'operator' in operation['var_name']):
        bracked_arguments = [f'({argument})' for argument in arguments]
        return f"{translate_varname(operation)}{''.join(bracked_arguments)}"
    else:
        operator = translate_operator(operation['var_name'])
        return f"({arguments[0]}) {operator} ({arguments[1]})"


def translate_applying(tree_app: dict) -> str:
    elements = flatten(tree_app)

    if 'var_name' in elements[0] and 'operator' in elements[0]['var_name']:
        elements = [translate_expr(element) for element in elements]
        return f"{f' {elements[0]} '.join(elements[1:])}"

    elements = [translate_expr(element) for element in elements]
    bracked_elements = [f'({element})' for element in elements]
    return ''.join(bracked_elements)


def translate_expr(tree_expr: dict) -> str:
    if type(tree_expr) is list:
        if len(tree_expr) == 1:
            tree_expr = tree_expr[0]
            return translate_expr(tree_expr)
        elif len(tree_expr) == 0:
            return ''
        else:
            return translate_applying(tree_expr)

    if 'value' in tree_expr:
        return translate_value(tree_expr)
    elif 'assign' in tree_expr:
        return translate_assign(tree_expr)
    elif 'import' in tree_expr:
        return translate_import(tree_expr)
    elif 'lambda' in tree_expr:
        return translate_lambda(tree_expr)
    elif 'var_name' in tree_expr:
        return translate_varname(tree_expr)
    elif 'infix' in tree_expr:
        return translate_infix(tree_expr)

    return str(tree_expr)


def translate(tree: dict):
    for line in tree:
        print(translate_expr(line))
