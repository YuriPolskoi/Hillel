# Homework 16 by Polskoi Yuri

line = b'r\xc3\xa9sum\xc3\xa9'

line_utf8 = line.decode()

print(line_utf8)

line_b_latin1 = line_utf8.encode("latin1")

print(line_b_latin1)

line_latin1 = line_b_latin1.decode("latin1")

print(line_latin1)
