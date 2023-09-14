# Challenge: Python Stack Trace Interpretation

See the "Python Stack Traces" attachment which lists several python stack traces. Your task is to examine the stack traces and provide a brief response for each one that summarizes what the problem or likely problem is, and the first line of code you would jump to in your code editor given the trace.

## Problem number 1:

### Input:

```python

Traceback (most recent call last):
  File "stack_traces.py", line 36, in run_trace
    f()
  File "stack_traces.py", line 45, in <lambda>
    run_trace(1, lambda: perform_calculation(add, '1', 3))
  File "stack_traces.py", line 8, in perform_calculation
    calc(x, y)
  File "stack_traces.py", line 12, in add
    return x + y
TypeError: can only concatenate str (not "int") to str
```

### Root cause:

The problem is a TypeError due to attempting to concatenate a string and an integer.

### First Line to check:

Go to line 12 in the perform_calculation function, where add(x, y) is called.

### Possible solution:

Convert the string to a integer before addition. We can use int() to do this: int(x) + int(y) if numbers are integers. If numbers are floating point numbers, then we can use float() to do this: float(x) + float(y).

## Problem number 2:

### Input:

```python
Traceback (most recent call last):
File "stack_traces.py", line 36, in run_trace
f()
File "stack_traces.py", line 46, in <lambda>
run_trace(2, lambda: perform_calculation(add, 7, '3'))
File "stack_traces.py", line 8, in perform_calculation
calc(x, y)
File "stack_traces.py", line 12, in add
return x + y
TypeError: unsupported operand type(s) for +: 'int' and 'str'
```

### Root cause:

The problem is a TypeError due to attempting to add an integer and a string.

### First Line to check:

Navigate to line 12 in the perform_calculation function, where add(x, y) is called.

### Possible solution:

Convert the string to integer or floats.

Problem number 3:

Input:

```python
Traceback (most recent call last):
File "stack_traces.py", line 36, in run_trace
f()
File "stack_traces.py", line 47, in <lambda>
run_trace(3, lambda: perform_calculation(mult, '3', '3'))
File "stack_traces.py", line 8, in perform_calculation
calc(x, y)
File "stack_traces.py", line 15, in mult
return x \* y
TypeError: can't multiply sequence by non-int of type 'str'
```

### Root cause:

The problem is a TypeError caused by trying to multiply two strings, which is not supported.

### First Line to check:

Look at line 15 in the mult function, where x \* y is calculated.

### Possible solution:

To fix this, convert the strings to integers/floats before multiplication: int(x) \* int(y).

## Problem number 4:

### Input:

```python
Traceback (most recent call last):
File "stack_traces.py", line 36, in run_trace
f()
File "stack_traces.py", line 48, in <lambda>
run_trace(4, lambda: perform_calculation(mult, [4], [3]))
File "stack_traces.py", line 8, in perform_calculation
calc(x, y)
File "stack_traces.py", line 15, in mult
return x \* y
TypeError: can't multiply sequence by non-int of type 'list'
```

### Root cause:

The error is a TypeError due to attempting to multiply a list by a non-integer.

### First Line to check:

Investigate line 15 in the mult function, where x \* y is computed.

### Possible solution:

Ensure that you are multiplying elements within the lists, not the entire lists themselves.

# Problem number 5:

### Input:

```python
Traceback (most recent call last):
File "stack_traces.py", line 36, in run_trace
f()
File "stack_traces.py", line 49, in <lambda>
run_trace(5, lambda: perform_calculation(innoc, '1', 3))
File "stack_traces.py", line 8, in perform_calculation
calc(x, y)
File "stack_traces.py", line 22, in innoc
spelunk()
File "stack_traces.py", line 21, in spelunk
raise ValueError('Invalid')
ValueError: Invalid
```

### Root cause:

The problem is a ValueError raised with the message "Invalid," indicating an issue within the spelunk function.

### First Line to check:

Go to line 21 in the spelunk function, where the ValueError is raised.

### Possible solution:

Inspect the spelunk function to identify the specific issue that led to the ValueError and handle it appropriately.

## Problem number 6:

### Input:

```python
Traceback (most recent call last):
File "stack_traces.py", line 36, in run_trace
f()
File "stack_traces.py", line 50, in <lambda>
run_trace(6, lambda: comp_calc([1, 2, 3], 1, add))
File "stack_traces.py", line 30, in comp_calc
return [perform_calculation(calc, x_i, y_i) for x_i, y_i in zip(x, y)]
TypeError: zip argument #2 must support iteration
```

### Root cause:

This TypeError arises from trying to use zip with an argument that doesn't support iteration.

### First Line to check:

Check line 30 in the comp_calc function, where the list comprehension uses zip.

### Possible solution:

Ensure that both x and y in the comp_calc function are iterable (e.g., lists or tuples) before using zip.

## Problem number 7:

### Input:

```python
Traceback (most recent call last):
File "stack_traces.py", line 36, in run_trace
f()
File "stack_traces.py", line 51, in <lambda>
run_trace(7, lambda: comp_calc([1, 2, [3]], [4, 5, 6], add))
File "stack_traces.py", line 30, in comp_calc
return [perform_calculation(calc, x_i, y_i) for x_i, y_i in zip(x, y)]
File "stack_traces.py", line 30, in <listcomp>
return [perform_calculation(calc, x_i, y_i) for x_i, y_i in zip(x, y)]
File "stack_traces.py", line 8, in perform_calculation
calc(x, y)
File "stack_traces.py", line 12, in add
return x + y
TypeError: can only concatenate list (not "int") to list
```

### Root cause:

A TypeError occurs because the code is trying to concatenate a list and an integer.

### First Line to check:

Go to line 12 in the add function, where x + y is calculated.

### Possible solution:

Modify the code to perform a valid operation on the list elements, depending on your intention.

## Problem number 8:

### Input:

```python
Traceback (most recent call last):
File "stack_traces.py", line 36, in run_trace
f()
File "stack_traces.py", line 52, in <lambda>
run_trace(8, lambda: calc_dict({'one': 1, 'two': '2'}, 'one', 'two', add))
File "stack_traces.py", line 26, in calc_dict
return perform_calculation(calc, d[k1], d[k2])
File "stack_traces.py", line 8, in perform_calculation
calc(x, y)
File "stack_traces.py", line 12, in add
return x + y
TypeError: unsupported operand type(s) for +: 'int' and 'str'
```

### Root cause:

A TypeError is raised when trying to add an integer and a string while processing a dictionary.

### First Line to check:

Examine line 12 in the add function, where x + y is executed.

### Possible solution:

Ensure that the values retrieved from the dictionary are of integers or floats. If not then, first convert them into integers or floats based on the requirement.

## Problem number 9:

### Input:

```python
Traceback (most recent call last):
File "stack_traces.py", line 36, in run_trace
f()
File "stack_traces.py", line 53, in <lambda>
run_trace(9, lambda: calc_dict({}, 'one', 'two', add))
File "stack_traces.py", line 26, in calc_dict
return perform_calculation(calc, d[k1], d[k2])
KeyError: 'one'
```

### Root cause:

The problem is a KeyError occurring because the code tries to access dictionary keys that don't exist.

### First Line to check:

Go to line 26 in the calc_dict function, where d[k1] and d[k2] are accessed.

### Possible solution:

Check if the keys 'one' and 'two' exist in the dictionary before accessing them, and handle the case when they are not present.
