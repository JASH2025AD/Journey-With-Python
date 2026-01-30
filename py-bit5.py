#Augmented assignment:list (in-place) vs tuple(rebinding)
lst =[1,2]
t=(1,2)
lst+=[3]
t+=(3,)
print(lst)
print(t)
