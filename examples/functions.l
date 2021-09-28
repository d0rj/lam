\x.x

\x.+ x 1 # like Python's `lambda x: x + 1`
\x. x + 1
\x.x `+` 1

\x.x `mod` 3 # like Python's `lambda x: x % 2`

\x.(x + \x.1) # must be like `lambda x_1: (lambda x_2: x_1 + x_2)`

\x.+ 1 x 2 3 # like `lambda x: 1 + x + 2 + 3`

(\x.\y.x `mod` y) 7 3 # apply lambda function to arguments
