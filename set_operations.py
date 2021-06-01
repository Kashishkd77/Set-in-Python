# Basic SET Operations illustration :

seta={1,1,2,3,4,2}
setb={8,9,5,2,3,1,8,9}

# "|" union operator -->
print("UNION OPERATION : ")
print("1. Using union operator ",seta|setb)
# Using union() method --> Returns union of sets in new set
seta.union(setb)
print("Using union() method : ",seta.union(setb))
#print(setb.union(seta))
print()

# "&" intersection operator -->
print("INTERSECTION OPERATION : ")
print("1. Using intersection operator ",seta&setb)
# Using intersection() method --> Returns intersection of two sets in new set
print("2. Using intersection() method : ",seta.intersection(setb))
print()

# "-" difference operator -->
print("DEFFERENCE OPERATION :")
print("1.1 Using difference operator SET_A-SET_B : ",seta-setb)
print("1.2 Using difference operator SET_B-SET_A : ",setb-seta)
# Using difference() method --> Returns difference of two sets in new set
print("2. Using difference() method SET_A-SET_B : ",seta.difference(setb))
print()

# "^" symmetric difference operator -->
print("SYMMETRIC DEFFERENCE OPERATION :")
print("1.1 Using symmetric difference operator SET_A and SET_B : ",seta^setb)
print("1.2 Using symmetric difference operator SET_B and SET_A : ",setb^seta)
# Using symmetric_difference() method --> Returns symmetric difference of two sets in new set
print("2. Using symmetric_difference() method SET_B-SET_A: ",setb.symmetric_difference(seta))
print()


# Other SET Operations illustration :

set1=(-11,56.8,True,'a','b','c',67,33,1,True,)

#OPERATION 1 -> Using "in" and "not in" keyword : Returns True/False
print("OPERATION 1 : Using 'in' and 'not in' keyword")
#"in" keyword
print("Is 'Kashish' present in set? : ",'Kashish' in set1)
print("Is 'True' present in set? : ",True in set1)
#"not in" keyword
print("Is 'Kashish' not present in set? : ",'Kashish' not in set1)
print("Is 'True' not present in set? : ",True not in set1)
print()

#OPERATION 2 -> Iterating through a set
print("OPERATION 2 : Iterating through a set using for loop")
#accessing the elements of set by value and not index , using for loop to iterate through set
print("Example 1 : ")
for i in set1:
    print(i)
print("Example 2 : ")
for i in {7,89,'d'}:
    print(i)