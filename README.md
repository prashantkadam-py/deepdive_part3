# Deep Dive Part 3 : Hash Maps

## Hashable Objects in Python
- All the immutable objects in python are hashable.
    Examples : 
    - int, float, complex, binary, Decimal, Fraction, strings, functions 
    - frozenset, tuples (elements are required to be hashable) 
    - custom classes and custom objects (maybe)
 
## Requirements to make the object or class hashable :
  - If an object is hashable :
        - the hash of the object must be an integer.
        - if two objects equal (==), the hashes must also be equal.
  - Important :
        - two objects that do not compare equal may still have the same hash. (Hash Collisions)
        - more hash collisions slower dictionaries.
       
## Custom Class : 
    - __eq__ : implement equal to method to compare object.
    - __hash__ : If we define __eq__ and not __hash__ then its value is None which indicates class is not hashable.

## Sets Operations
s1 = {0, 2, 4, 6, 8}
s2 = {1, 2, 3, 4, 5}

1. Unions    
    s1 | s2 = {0, 1, 2, 3, 4, 5, 6, 8}

2. Intersections
    s1 & s2 = {2, 4}
    
3. Differences
    s1 - s2 = {8, 0, 6}
    
4. Symmetric Differences
    s1 ^ s2 = {0, 1, 3, 5, 6, 8}
    
5. Subsets
    s1 = {1, 2, 3, 4}
    s2 = {1, 2, 3, 4, 5, 6}
    s1 <= s2  - True

6. Supersets
    s1 = {1, 2, 3, 4}
    s2 = {1, 2}
    s1 >= s2 - True
    
7. disjointness
    s1 = {1, 3, 5}
    s2 = {2, 4, 6}
    s1.isdisjoint(s2)
