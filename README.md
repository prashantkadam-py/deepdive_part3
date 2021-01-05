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
    
        
