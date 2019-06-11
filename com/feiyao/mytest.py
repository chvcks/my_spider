
value = ('the answer is: ', 42)
s = str(value)
print(s)

with open('mytestfile', 'w') as f:
    f.write(s)
    print(f.tell())
print(99%100)






