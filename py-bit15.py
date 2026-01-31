def sub():
    yield 1
    return "subdone"
def  main():
    val =yield from sub()
    yield val
g=main()
print(next (g))
print(next (g))    
    