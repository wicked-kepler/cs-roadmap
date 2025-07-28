# Lecture 8 - Functions as Objects

> **Topic Overview:** environments, scope, functions as objects

### return
- Return only has meaning inside a function
- Only one return is executed inside a function
- Code inside the function after the return statement is not executed
- Has a value associated with it

### Scope
- When a function is called it creates a new environment with every function call
- This environment disappears after it return a value
- Global environments are where the user interacts with the Python interpreter and where the program starts out
- Formal parameters get bound to the value of input parameters
- Scope is a mapping of names to objects
  - Defines the context in which the body is evaluated
  - Values of variables given by bindings of names
- A function can access a variable defined outside
- A function cannot modify a variable defined outside

### Objects
- Objects in Python have a type
- Objects can be used as an argument or returned from a function