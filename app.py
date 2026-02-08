print('Hello Git')
def greet(): return 'Hello'

def add(a, b): return a + b
def subtract(a, b): return a - b
def multiply(a, b): return a * b
def divide(a, b): return a / b
def modulus(a, b): return a % b
def power(a, b): return a ** b
def floor_divide(a, b): return a // b
def square(a): return a * a
def cube(a): return a * a * a
def sqrt(a): return a ** 0.5
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
def is_even(n): return n % 2 == 0
def is_odd(n): return n % 2 != 0
