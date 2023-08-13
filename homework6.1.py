b = b'r\xc3\xa9sum\xc3\xa9'
str_d = b.decode("utf-8")
print(str_d)
b_new = str_d.encode("Latin1")
print(b_new)
str_d_new = b_new.decode("Latin1")
print(str_d_new)