#mutating a dict while iterating-->error
d={1:'a',2:'b'}
for k in d:
    if k==1:
        del d[k]
        