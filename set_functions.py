# SET METHODS illustration :
print("SET METHODS illustration :")
set1={1,2,34,67,89,23,1,99}
my_set1={1,4,9,0,65,78,8,4,4,5,7,8}
my_set2={1,2,3,7,9,0,7,45,6}

#add() : Adds an element to the set
print("1. add() method")
set1.add(12)
print("Adding an element in list : ",set1)
print()

#update() : Updates the set with the union of itself and others
set1.update([11,12,13])
print("2. update() method")
print("Adding multiple elements in list : ",set1)
set1.update([11,12,13],{1,2,4})
print("Adding multiple elements in list : ",set1)
print()

#copy()	: Returns a copy of the set
print("3. copy() method : ")
a={}
a=my_set2.copy()
print("Copying one set in another using copy() my_set2 copied in new set 'a' : ",a)
my_set2=set1.copy()                 #now my_set2 has only the values of set1
print("Copying one set in another using copy() set1 copied in my_set2: ",my_set2)
print()

#union() : Returns the union of sets in a new set
print("4. union() method : ",my_set2.union(my_set1))
print()

#intersection()	: Returns the intersection of two sets as a new set
print("5. intersection() method : ",my_set2.intersection(my_set1))
print()

#intersection_update() : Updates the set with the intersection of itself and another
my_set2.intersection_update(my_set1)
print("6. intersection_update() method : ",my_set2)
print()

# print(set1)
# print(my_set1)
# print(my_set2)

#difference() : Returns the difference of two or more sets as a new set
print("7. difference() method : ",set1.difference(my_set1))
print()

#difference_update() : Removes all elements of another set from this set
set1.difference_update(my_set1)
print("8. difference_update() method : ",set1)
print()

#symmetric_difference()	: Returns the symmetric difference of two sets as a new set
print("9. symmetric_difference() method : ",my_set2.symmetric_difference(my_set1))
print()

#symmetric_difference_update() : Updates a set with the symmetric difference of itself and another
my_set2.symmetric_difference_update(my_set1)
print("10. symmetric_difference_update() method : ",my_set2)
print()

#isdisjoint() : Returns True if two sets have a null intersection
print("11. isdisjoint() method : ")
print("Check if both the sets are disjoint or not ?: ",my_set2.isdisjoint(my_set1))
print()

#issubset()	: Returns True if another set contains this set
print("12. issubset() method : ")
print("Check if my_set2 is superset of my_set1  or not ? : ",my_set2.issubset(my_set1))
print()

#issuperset() : Returns True if this set contains another set
print("13. issuperset() method : ")
print("Check if my_set2 is superset of my_set1  or not ? : ",my_set2.issuperset(my_set1))
print()

#pop() : Removes and returns an arbitrary set element. Raises KeyError if the set is empty
print("14. pop() method : ")
set1.pop()
print("Deleting an arbitrary element using pop() : ",set1)
print()

#remove() : Removes an element from the set. If the element is not a member, raises a KeyError
print("15. remove() method : ")
my_set2.remove(65)
print("Deleting element using remove() : ",my_set2)
print()

#discard() : Removes an element from the set if it is a member. (Do nothing if the element is not in set)
print("16. discard() method : ")
my_set2.discard(4)
print("Deleting element using discard() : ",my_set2)
print()

#clear() : Removes all elements from the set
print("17. clear() method : ")
set1.clear()
print("Deleting all elements using clear() : ",set1)
print()

# SET BUILT-IN FUNCTIONS illustration :
print("SET BUILT-IN FUNCTIONS illustration :")
set1={1,2,34,67,89,23,1,99,0}
my_set1={1,4,9,0,65,78,8,4,4,5,7,8}
my_set2={1,2,3,7,9,0,7,45,6}

# all() : Returns True if all elements of the set are true (or if the set is empty).
print("1. all() function : ")
print("Using all() in my_set1 is  : ",all(my_set1))    #False since my_set1 has 0
print()

# any() : Returns True if any element of the set is true. If the set is empty, returns False.
print("2. any() function : ")
print("Using any() in my_set1 is  : ",any(my_set1))     #True since my_set1 has at least one value True
print()

# enumerate() : Returns an enumerate object. It contains the index and value for all the items of the set as a pair.
print("3. enumerate() function : ")
enumerate_set=enumerate(my_set1)
print("Enumerating in my_set1 is  : ",set(enumerate_set))
print()

# len() : Returns the length (the number of items) in the set.
print("4. len() function : ")
print("Length of set1 is  : ",len(set1))
print()

# max() : Returns the largest item in the set.
print("5. max() function : ")
print("Largest item in set1 is  : ",max(set1))
print()

# min() : Returns the smallest item in the set.
print("6. min() function : ")
print("Smallest item in set1 is  : ",min(set1))
print()

# sorted() : Returns a new sorted list from elements in the set(does not sort the set itself).
print("7. sorted() function : ")
print("Sorting in set1 is  : ",sorted(set1))
print()

# sum() : Returns the sum of all elements in the set.
print("8. sum() function : ")
print("Sum of items in set1 is  : ",sum(set1))
print()

