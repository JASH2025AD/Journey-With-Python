def gen():
    total=0
    while True :
       x=yield total    
       if x is None:
           return total
       total +=x
g = gen()
print(next(g))    #start:yields 0
print(g.send(5))  #send 5 -->total =5,yield 5
print(g.send(3))  #total =8 ,yield 8
try:
    print(g.send(None))  #tells generator to return total
except StopIteration as e:
    print("Returned:",e.value)           
        