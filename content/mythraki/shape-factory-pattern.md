---
title: Shape-Factory-Pattern
date: 2025-01-03
author: Your Name
cell_count: 12
score: 10
---

```python

```


```python
import pyutil as pyu
pyu.get_local_pyinfo()
```




    'conda env: ml311; pyv: 3.11.10 (main, Oct  3 2024, 07:29:13) [GCC 11.2.0]'




```python
print(pyu.ps2("haystack-ai ollama-haystack python-dotenv"))
```

    haystack-ai==2.8.0
    ollama-haystack is not installed in the current environment.
    python-dotenv==0.21.0
    



```python

```


```python
from abc import ABC, abstractmethod

# Step 1: Define an abstract base class (interface)
class Shape(ABC):
    @abstractmethod
    def draw(self):
        pass

# Step 2: Create concrete implementations of the Shape interface
class Circle(Shape):
    def draw(self):
        return "Drawing a Circle"

class Square(Shape):
    def draw(self):
        return "Drawing a Square"

class Rectangle(Shape):
    def draw(self):
        return "Drawing a Rectangle"

# Step 3: Create a Factory class to generate objects
class ShapeFactory:
    @staticmethod
    def get_shape(shape_type):
        if shape_type == "circle":
            return Circle()
        elif shape_type == "square":
            return Square()
        elif shape_type == "rectangle":
            return Rectangle()
        else:
            raise ValueError(f"Unknown shape type: {shape_type}")

# Client Code
if __name__ == "__main__":
    # Use the factory to create shapes
    factory = ShapeFactory()
    
    shape1 = factory.get_shape("circle")
    print(shape1.draw())  # Output: Drawing a Circle
    
    shape2 = factory.get_shape("square")
    print(shape2.draw())  # Output: Drawing a Square
    
    shape3 = factory.get_shape("rectangle")
    print(shape3.draw())  # Output: Drawing a Rectangle
```

    Drawing a Circle
    Drawing a Square
    Drawing a Rectangle



```python

```


```python
# Singleton + Factory

from abc import ABC, abstractmethod

# Abstract Base Class
class Shape(ABC):
    @abstractmethod
    def draw(self):
        pass

# Concrete Implementation: Circle
class Circle(Shape):
    _instance = None  # Class-level variable to store the singleton instance

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        if not hasattr(self, "initialized"):  # To prevent reinitialization
            print("Initializing Circle...")
            self.initialized = True

    def draw(self):
        return "Drawing a Circle"

# Concrete Implementation: Square
class Square(Shape):
    _instance = None  # Class-level variable to store the singleton instance

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        if not hasattr(self, "initialized"):  # To prevent reinitialization
            print("Initializing Square...")
            self.initialized = True

    def draw(self):
        return "Drawing a Square"

# Factory Class
class ShapeFactory:
    @staticmethod
    def get_shape(shape_type):
        if shape_type == "circle":
            return Circle()  # Singleton behavior for Circle
        elif shape_type == "square":
            return Square()
        else:
            raise ValueError(f"Unknown shape type: {shape_type}")

# Client Code
if __name__ == "__main__":
    factory = ShapeFactory()

    # First time creating Circle
    shape1 = factory.get_shape("circle")
    print(shape1.draw())  # Output: Drawing a Circle

    # Reusing the same Circle instance
    shape2 = factory.get_shape("circle")
    print(shape2.draw())  # Output: Drawing a Circle

    # Reusing the same Circle instance
    shape2 = factory.get_shape("square")
    print(shape2.draw())  # Output: Drawing a Circle

    # Reusing the same Circle instance
    shape2 = factory.get_shape("square")
    print(shape2.draw())  # Output: Drawing a Circle

    # Verifying both instances are the same
    print(shape1 is shape2)  # Output: True
```

    Initializing Circle...
    Drawing a Circle
    Drawing a Circle
    Initializing Square...
    Drawing a Square
    Drawing a Square
    False



```python

```


```python

```

## Decorator


```python
import time
from abc import ABC, abstractmethod

# Step 1: Define an abstract base class (interface)
class Shape(ABC):
    @abstractmethod
    def draw(self):
        pass

# Step 2: Create concrete implementations of the Shape interface
class Circle(Shape):
    def draw(self):
        return "Drawing a Circle"

class Square(Shape):
    def draw(self):
        return "Drawing a Square"

class Rectangle(Shape):
    def draw(self):
        return "Drawing a Rectangle"

# Decorator for measuring execution time
def execution_time_wrapper(original_method):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = original_method(*args, **kwargs)
        end_time = time.time()

        execution_time = end_time - start_time
        formatted_execution_time = f"{execution_time:.6f}"
        print(f"{original_method.__name__} executed in {formatted_execution_time} seconds")
        return result, formatted_execution_time
        
    return wrapper

# Step 3: Create a Factory class to generate objects
class ShapeFactory:
    @staticmethod
    def get_shape(shape_type):
        if shape_type == "circle":
            shape = Circle()
        elif shape_type == "square":
            shape = Square()
        elif shape_type == "rectangle":
            shape = Rectangle()
        else:
            raise ValueError(f"Unknown shape type: {shape_type}")
        
        # Dynamically wrap the draw method
        shape.draw = execution_time_wrapper(shape.draw)
        return shape

# Client Code
if __name__ == "__main__":
    # Use the factory to create shapes
    factory = ShapeFactory()
    
    shape1 = factory.get_shape("circle")
    print(shape1.draw())  # Output: Drawing a Circle with execution time
    
    shape2 = factory.get_shape("square")
    print(shape2.draw())  # Output: Drawing a Square with execution time
    
    shape3 = factory.get_shape("rectangle")
    print(shape3.draw())  # Output: Drawing a Rectangle with execution time
```

    draw executed in 0.000000 seconds
    ('Drawing a Circle', '0.000000')
    draw executed in 0.000000 seconds
    ('Drawing a Square', '0.000000')
    draw executed in 0.000000 seconds
    ('Drawing a Rectangle', '0.000000')



```python

```


---
**Score: 10**