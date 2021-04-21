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
s1 = {0, 2, 4, 6, 8} <br />
s2 = {1, 2, 3, 4, 5} <br />

1. Unions <br />
    s1 | s2 = {0, 1, 2, 3, 4, 5, 6, 8} <br />

2. Intersections <br />
    s1 & s2 = {2, 4} <br />
    
3. Differences <br />
    s1 - s2 = {8, 0, 6} <br />
    
4. Symmetric Differences <br />
    s1 ^ s2 = {0, 1, 3, 5, 6, 8} <br />
    
5. Subsets <br />
    s1 = {1, 2, 3, 4} <br />
    s2 = {1, 2, 3, 4, 5, 6} <br />
    s1 <= s2  - True <br />

6. Supersets <br />
    s1 = {1, 2, 3, 4} <br />
    s2 = {1, 2} <br />
    s1 >= s2 - True <br />
    
7. disjointness <br />
    s1 = {1, 3, 5} <br />
    s2 = {2, 4, 6} <br />
    s1.isdisjoint(s2) <br />
    
## Pickling

__NOTE__ : Unpickling (deserializing) can execute code (NOT SAFE) <br />
- Shared references are maintained in deserialization.
- recursive objects can be pickled.

        class Exploit(object):
            def __reduce__(self):
                return (os.system("cat /etc/password > exploit.txt && curl www.google.com >> exploit.txt")
