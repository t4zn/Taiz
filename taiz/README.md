# Taiz Language

Taiz is a custom, minimalist programming language designed for simplicity and ease of use. This language is built to run on a custom interpreter and is suited for educational purposes, scripting, and learning programming concepts. The language syntax is simple, and it supports basic operations, loops, functions, and more.

## Features

- **Minimalist Syntax**: Focus on clarity and simplicity.
- **Custom Interpreter**: The Taiz language runs using a custom interpreter written in Python.
- **Support for Variables, Functions, and Loops**: Basic constructs to write executable programs.
- **Integration with VS Code**: Easily write and execute Taiz scripts directly from VS Code.

## Keywords


### **1. `cash` (Variable Assignment)**

Assign a value to a variable.

```
cash x = 10
cash y = x + 5
emit y
```

---

### **2. `kiss` (AND Operator)**

Used to combine conditions with AND.

```
cash a = 5
cash b = 10
emit a > 0 kiss b < 15
```

---

### **3. `aka` (OR Operator)**

Used to combine conditions with OR.

```
cash a = -1
cash b = 10
emit a > 0 aka b > 5
```

---

### **4. `cap` (NOT Operator)**

Negates a condition.

```
cash a = 5
emit cap a > 10
```

---

### **5. `bet` (If Statement)**

Defines a basic if statement.

```
bet x < 10 boom
emit "x is less than 10"
destroy
```

---

### **6. `maybe` (Elif Statement)**

Used as an elif in an if block.

```
bet x < 5 boom
emit "x is less than 5"
maybe x < 10 boom
emit "x is less than 10"
bruh
emit "x is 10 or greater"
destroy
```

---

### **7. `bruh` (Else Statement)**

Defines the else statement.

```
bet x < 5 boom
emit "x is less than 5"
bruh
emit "x is greater than or equal to 5"
destroy
```

---

### **8. `cycle` (For Loop)**

Defines a for loop.

```
cycle i = 0 to 5
emit i
boom
```

---

### **9. `to` (Used in For Loop)**

Used to define the range of a for loop.

```
cycle i = 0 to 3
emit i
boom
```

---

### **10. `jump` (Step in For Loop)**

Defines the step in a for loop.

```
cycle i = 0 to 10 jump 2
emit i
boom
```

---

### **11. `until` (While Loop)**

Defines a while loop.

```
cash x = 0
until x == 5 boom
emit x
cash x = x + 1
```

---

### **12. `ignite` (Function Definition)**

Defines a function.

```
ignite add_numbers a, b
cash result = a + b
emit result
```

add_numbers 5, 10

---

### **13. `boom` (End of Block)**

Marks the end of a block (e.g., if, loop, or function).

```
bet x < 5 boom
emit "x is less than 5"
destroy
```

---

### **14. `destroy` (End Block or Function)**

Ends a block or function definition.

```
bet x < 5 boom
emit "x is less than 5"
destroy
```

---

### **15. `emit` (Return or Print)**

Used to print or return a value.

```
emit "Hello, World!"
```

---

### **16. `skip` (Continue in Loop)**

Skips the current iteration of a loop.

```
cycle i = 0 to 5
skip if i == 2
emit i
boom
```

---

### **17. `pause` (Break in Loop)**

Stops the execution of a loop.

```
cycle i = 0 to 5
pause if i == 3
emit i
boom
```

---

### **18. `hole` (Null Value)**

Represents a null value.

```
cash value = hole
emit value
```

---

### **19. `L` (False)**

Represents a boolean False.

```
emit L
```

---

### **20. `W` (True)**

Represents a boolean True.

```
emit W
```

---

### **21. `pie` (Math.PI)**

Represents the mathematical constant Pi.

```
emit pie
```

---

### **22. `shout` (Print Function)**

Prints a string to the output.

```
shout "This is a shout!"
```

---

### **23. `show` (Print and Return)**

Prints and returns a value.

```
show "This is shown!"
```

---

### **24. `ask` (Input String)**

Asks for user input as a string.

```
cash name = ask "What is your name?"
emit name
```

---

### **25. `askin` (Input Integer)**

Asks for user input as an integer.

```
cash age = askin "What is your age?"
emit age
```

---

### **26. `wipe` (Clear Screen)**

Clears the console output.

```
wipe
```

---

### **27. `is_num` (Check if Number)**

Checks if a value is a number.

```
cash x = 10
emit is_num x
```

---

### **28. `is_str` (Check if String)**

Checks if a value is a string.

```
cash name = "John"
emit is_str name
```

---

### **29. `is_list` (Check if List)**

Checks if a value is a list.

```
cash items = [1, 2, 3]
emit is_list items
```

---

### **30. `is_func` (Check if Function)**

Checks if a value is a function.

```
ignite greet
emit "Hello!"emit is_func greet
```


---

### **31. `add` (Append to List)**

Appends an item to a list.

```
cash numbers = [1, 2, 3]
add numbers 4
emit numbers
```

---

### **32. `drop` (Pop from List)**

Removes an item from the list.

```
cash numbers = [1, 2, 3]
drop numbers
emit numbers
```

---

### **33. `merge` (Extend List)**

Adds elements from one list to another.

```
cash list1 = [1, 2]
cash list2 = [3, 4]
merge list1 list2
emit list1
```

---

### **34. `size` (Get Length)**

Gets the length of a list.

```
cash items = [1, 2, 3]
emit size items
```

---

### **35. `go` (Run Script)**

Executes a script.

```
go "path/to/script.tz"
```
