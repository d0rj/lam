from lark import Lark


parser = Lark.open('lambda.lark', parser='lalr', start='programm', rel_to=__file__)

programm = '''
42 # simple return of value
\\x.x # or function

\\x.+ x 1 # prefix operator applying
\\x. x + 1 # or infix for operators (literally operators, such as '**')
\\x.x `+` 1 # you can also wrap operators with backquotes
\\x.x `mod` 3 # but for other variable names it's necessary

(\\x.\\y.x `mod` y) 7 3 # apply lambda function to arguments

let f x = \\x.x ** 2 # create function

let x = 2 + 2 # create variable (also fucntion, but without arguments)

'''

tree = parser.parse(programm)

print(tree.pretty())
