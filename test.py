

f = {'+': lambda x, y: str(float(x) + float(y)),
     '-': lambda x, y: str(float(x) - float(y)),
     '*': lambda x, y: str(float(x) * float(y)),
     '/': lambda x, y: str(float(x) / float(y)),
     'C': lambda x, y: "",
}

"""
x = self.request.get('x')
y = self.request.get('y')
operator = self.request.get('operator')
"""

x=1
y=1
operator= "C"

result = ""

try:
    result = f[operator](x, y)
except ValueError:
    result = "Error: Incorrect Number"
except ZeroDivisionError:
    result = "Error: Division by zero"
except KeyError:
    pass

print result
