#Generator exhaustion(one-use iterator)
gen=(x for x in range(3))
print(list(gen))
print(set(gen))
print(tuple(gen))

gen = (x for x in range(3))
data = list(gen)

print(data)        # [0, 1, 2]
print(set(data))   # {0, 1, 2}
print(tuple(data)) # (0, 1, 2)
