def foo(x) -> int: # 'annotation' another called 'comment'.
    return x * 2

y = foo(32)
print(y) # если передаваемый переменный будет не y а х
         # тогда будет NameError



# DuckTyping
def foo(x: str, y: int) -> str:
    result = x
    for i in range(y - 1):
        result += x
    return result

t = foo("ma", 2)
print(t)
