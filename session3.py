'''
Write a Python program that defines a function f(x) that returns x**3 + 8. In the main function of the program, call f(x) with x = 9 and print the result.  Use an if statement that executes if the result is larger than 27 and prints “YAY!”.
'''
def f(x):
    return x**3 + 8

def main():
    result = f(9)
    print(result)
    print("YAY!") if result > 27 else None

main()