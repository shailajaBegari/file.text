f=open("abc.text")
content=f.read(20)
print("1:",content)
content=f.read(10)
print("2:",content)
f.close()
