#Shallow copy vs deepcopy(nested lists)
import copy
orig=[[1],[2]]
shallow=copy.copy(orig)
deep=copy.deepcopy(orig)
shallow[0].append(99)
print("orig:",orig)
print("shallow:",shallow)
print("deep:",deep)
