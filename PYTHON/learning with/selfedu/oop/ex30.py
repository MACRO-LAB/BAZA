"""#30. Распространение исключений (propagation exceptions) | ООП Python
"""

def func2():
    return 1/0

def func1():
    try:
        func2()
    except ZeroDivisionError:
        print("asdfs")

print("random")

func1()

print("random2")
print("randome")