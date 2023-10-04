# Homework 24 by Polskoi Yuri

class String(str):
    def __add__(self, other):
        return String(str(self) + str(other))

    def __sub__(self, other):
        a = str(self)
        b = str(other)
        index = a.find(b)
        result = a[0:index] + a[index+len(b):]
        return String(result) if index > -1 else self


print(String('New') + String(890))
print(String(1234) + 5678)
print(String('New') + 'castle')
print(String('New') + 77)
print(String('New') + True)
print(String('New') + ['s', ' ', 23])
print(String('New') + None)

print('-' * 100)

print(String('New bala7nce') - 7)
print(String('New balance') - 'bal')
print(String('New balance') - 'Bal')
print(String('pineapple apple pine') - 'apple')
print(String('New balance') - 'apple')
print(String('NoneType') - None)
print(String(55678345672) - 7)
print(String('New balance') - 'New ')
