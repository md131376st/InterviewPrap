# Definition

object-oriented Programming (OOPs) is a programming paradigm that uses objects and classes in programming. It aims to
implement real-world entities like inheritance, polymorphisms, encapsulation

# concepts

- class
    - blueprints or the prototype from which the objects are being created.
- object
    - The object is an entity that has a state and behavior associated with it
    - consist:
        - State
        - Behavior
        - Identity
- Polymorphism
    - simply means having many forms
    - this can be used by overriding
- Encapsulation
    - f wrapping data and the methods that work on data within one unit
- Inheritance
    - is the capability of one class to derive or inherit the properties from another class
    - Type
        - single
        - Multilevel
        - Hierarchical
        - Multiple
- Data Abstraction
    - use abstract classes

# Important tips

- __ is used for private valuebles in classes
- use meaningful names
- static => bound to class level not object level
    - readable
    - save memory

# Diagrams

- Use Case Diagram
- Activity Diagram
- Class Diagram
- Schema Design
- API Design

# Important key words
- Caching
- Load Balancer
- Scalability
- Reliability
- Error Handling
# reduce Memory
- Using built-in Dictionaries
- using tuples
- class
-  recordclass (out side tool)
  - ```python
    import sys 
    from recordclass import recordclass 
    
    Point = recordclass('Point', ('x', 'y', 'z')) 
    
    Coordinates = Point(3, 0, 1) 
    print(sys.getsizeof(Coordinates))
    
    ```
- make data classes
  ```python
    import sys 
    from recordclass import make_dataclass 
    
    Position = make_dataclass('Position', ('x', 'y', 'z')) 
    Coordinates = Position(3, 0, 1) 
    
    print(sys.getsizeof(Coordinates)) 
    
    ```
  



