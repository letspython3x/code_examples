def my_fu(var):
    print(var)
    return "yahooooo"

def my_fu2():
    return False


import ast
tree = ast.parse("print('Hello World')")
exec(compile(tree, filename="<ast>", mode="exec"))

result = None
tree2 = ast.parse("result = my_fu('hello') or my_fu2()")
exec(compile(tree2, filename="<ast>", mode="exec"))

print(result)