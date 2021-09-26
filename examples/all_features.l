
42 # simple return of value
"hello" # double quoted string
'world' # simple string
\x.x # or function

\x.+ x 1 # prefix operator applying
\x. x + 1 # or infix for operators (literally operators, such as '**')
\x.x `+` 1 # you can also wrap operators with backquotes
\x.x `mod` 3 # but for other variable names it's necessary
\x.(x + \x.1) # with brackets

\x.+ 1 x 2 3 # operator multi-application will be (1 + x + 2 + 3)

(\x.\y.x `mod` y) 7 3 # apply lambda function to arguments

let f x = \x.x ** 2 # create function

let x = 2 + 2 # create variable (also fucntion, but without arguments)

import print # simple import
import math.cos # import part of package
import math.vector.`+` # import operator
import math.f -> func # import rename

a:Int # simple typing
a: Int -> Float # with function types
a :(Float, Decimal) # and Sigma types

a : Int -> (Float, Int) # more complex typing
a : (Int, Float) -> Int # like this
a : (Int -> Int, Int) -> Float # or this

[a, 2, 'hello'] # lists of values
[a, b : A -> B, c: Float] # and also with types
