# Homework 26 by Polskoi Yuri

class Calc:
    def add(self, x, y):
        try:
            result = x + y
        except Exception as e:
            return f"Error: {e}"
        return result

    def sub(self, x, y):
        try:
            result = x - y
        except Exception as e:
            return f"Error: {e}"
        return result

    def mult(self, x, y):
        try:
            result = x * y
        except Exception as e:
            return f"Error: {e}"
        return result

    def div(self, x, y):
        try:
            if y == 0:
                raise ZeroDivisionError("Не можна ділити на 0")
            result = x / y
        except ZeroDivisionError as e:
            return e
        except Exception as e:
            return f"Error: {e}"

    def pow(self, x, y):
        try:
            if y < 0 or not y.is_integer():
                raise ValueError("Не можна обчислити дробний або від'ємний ступінь числа")
            result = x ** y
        except ValueError as e:
            return e
        except Exception as e:
            return f"Error: {e}"
        return result

    def sqrt(self, x):
        try:
            if x < 0:
                raise ValueError("Не можна обчислити корінь від'ємного числа")
            result = x ** 0.5
        except ValueError as e:
            return e
        except Exception as e:
            return f"Error: {e}"
        return result


calc = Calc()
print("x + y =", calc.add(5, 3))
print("x - y =", calc.sub(5, 3))
print("x * y =", calc.mult(2, -8))
print("x / y =", calc.div(5, 0))
print("x ** y =", calc.pow(5, -2))
print("Квадратний корінь x =", calc.sqrt(-45))

