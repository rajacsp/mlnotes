---
title: Abstract-With-Ast
date: 2024-12-07
author: Your Name
cell_count: 7
score: 5
---

```python
!python --version
```

    Python 3.12.4



```python
import ast
```


```python
# Python code as a string
code = """
def greet(name):
    return f"Hello, {name}!"
    
x = 10
y = x + 20
print(greet("Python"))
"""
```


```python
# Parse the code into an AST
tree = ast.parse(code)
```


```python
# Define a visitor class to analyze nodes
class CodeAnalyzer(ast.NodeVisitor):
    def visit_FunctionDef(self, node):
        print(f"Function found: {node.name}")
        self.generic_visit(node)
    
    def visit_Assign(self, node):
        targets = [t.id for t in node.targets if isinstance(t, ast.Name)]
        print(f"Assignment to: {targets}")
        self.generic_visit(node)
    
    def visit_Call(self, node):
        if isinstance(node.func, ast.Name):
            print(f"Function call: {node.func.id}")
        self.generic_visit(node)
```


```python
# Create an analyzer instance and visit nodes
analyzer = CodeAnalyzer()
analyzer.visit(tree)
```

    Function found: greet
    Assignment to: ['x']
    Assignment to: ['y']
    Function call: print
    Function call: greet



```python

```


---
**Score: 5**