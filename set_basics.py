# SET Basics : unordered , unindexed , immutable and no duplicate values allowed
# SET cannot contain mutable elements like lists,sets,dictionaries,etc.

#CREATION -->
# METHOD 1 : with {}
empty_set={}
single_set={1,2,3,4,5,6,7,8,9,10}
# METHOD 2 : Using built-in function "set()"
mixed_set=set([6.7,3,True,'a',"Kashish"])
#Nested Set is not allowed
print("CREATING SET : ",mixed_set)
print()

#Creating tuple with single element is difficult as it is confused with dictionary
single_set={}
print("SINGLED ELEMENT SET TYPE : ",type(single_set))       #type() : Returns the type of data type

#Using set() function :  Avoids type conflict  in singled element set
single_set=set()
print("SINGLED ELEMENT SET TYPE RESOLVED : ",type(single_set))
print()

#CHANGING IN SET: SET are unindexed
#mixed_set[0] --> gives TypeError
print("CHANGING IN SET : ")
#METHOD 1 : Using add() method --> adds an element
single_set.add(11)
print("1 . Adding an element in list : ",single_set)
#METHOD 2 : Using update() method --> adds all elements
single_set.update([11,12,13])
print("2.1 . Adding multiple elements in list : ",single_set)
single_set.update([11,12,13],{1,2,4})
print("2.2 . Adding multiple elements in list : ",single_set)
print()

#SPECIAL FEATURES OF SET or SET COMPREHENSIONS :
print("SET COMPREHENSIONS :")
# 1 . Use of for statement within set brackets
print("1. Use of 'for' statement within set brackets : ",end="")
power={ 2 ** x for x in range(5) }          #prints square of 0 to 4
print(power)

# 2 . Use of for and if statement within set brackets
power1={ 2 ** x for x in range(10) if x>5 }                         #the entire list gets stored in power1
print("2.1 Use of 'for' and 'if' statement within set brackets : ",power1)

multiply={ x for x in range(10) if x%2==0 }
print("2.2 Use of 'for' and 'if' statement within set brackets (even numbers): ",multiply)

concate={ x+y for x in ['a','b'] for y in ['c','d'] }
print("2.3 Use of concatenation of two lists using 'for' statement within set brackets : ",concate)
print()


#DELETING IN SET :
print("DELETING IN SET :")
#METHOD 1 : Using pop() method : Removes and returns an arbitrary element
single_set.pop()
print("1. Deleting an arbitrary element using pop() : ",single_set)

#METHOD 2 : Using clear() method : Removes all elements of list
mixed_set.clear()
print("2. Deleting all elements using clear() : ",mixed_set)

#METHOD 3 : Using remove(value) method : Removes an element of given value , gives KeyError if element is not present
#print(single_set)
single_set.remove(13)
print("3. Deleting element using remove() : ",single_set)

#METHOD 4 : Using discard(value) method : Removes an element of given value ,gives no KeyError if element is not present
single_set.discard(11)
print("4. Deleting element using discard() : ",single_set)