#Sort stability (preserves original order for equal keys)
pairs =[['a',2],['b',1],['c',2]]
pairs.sort(key=lambda x:x[1])
print(pairs)