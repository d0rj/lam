

def translate_value(tree_value: dict) -> str:
    value = tree_value['value']
    if 'number' in value:
        return value['number']
    elif 'string' in value:
        return value['string']
    else:
        raise Exception('Wrong value type')


def translate_name(tree_name: dict) -> str:
    return tree_name['name']


def translate_varname(tree_varname: dict) -> str:
    return translate_name(tree_varname['var_name'])


def translate_assign(tree_assign: dict) -> str:
    assign = tree_assign['assign']

    var_name = assign['variable']
    arguments = assign['arguments']
    body = assign['expr'][0]
    return f'({translate_varname(var_name)}, {[translate_name(arg) for arg in arguments]}, {body})'


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


def translate(tree: dict):
    for line in tree:
        obj = line[0]
        if 'value' in obj:
            print(translate_value(obj))
        elif 'lambda' in obj:
            pass
        elif 'assign' in obj:
            print(translate_assign(obj))
        elif 'import' in obj:
            print(translate_import(obj))

        print(line, '\n')
