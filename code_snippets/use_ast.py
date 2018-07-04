import ast
ast.parse('"hi" or None')
#<_ast.Module object at 0x7f97af125110>
 
k = ast.parse('6+8')
print(k)
#<_ast.Module object at 0x7f97af137510>
print(eval(compile(k,'', mode="eval")))


