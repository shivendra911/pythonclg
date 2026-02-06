String
## Overview
Strings are sequences of characters used to store text data.

## Creation
```python
# Single quotes
name = 'Python'

# Double quotes
message = "Hello World"

# Triple quotes (multi-line)
text = """This is a
multi-line string"""
```

## Common Methods
- `.upper()` - Convert to uppercase
- `.lower()` - Convert to lowercase
- `.strip()` - Remove leading/trailing whitespace
- `.replace(old, new)` - Replace substring
- `.split(delimiter)` - Split into list
- `.join(list)` - Combine list into string

## Indexing & Slicing
```python
text = "Python"
text[0]      # 'P' (first character)
text[-1]     # 'n' (last character)
text[0:3]    # 'Pyt' (slice from index 0 to 2)
```

## String Formatting
```python
name = "Alice"
age = 25

# f-string (recommended)
f"Name: {name}, Age: {age}"

# format() method
"Name: {}, Age: {}".format(name, age)
```

## Immutability
Strings cannot be modified after creation. Operations return new strings.

## Memory & Size
```python
import sys

text = "Hello World"
sys.getsizeof(text)  # Returns size in bytes

# String size depends on content length and encoding
# Each character typically uses 1-4 bytes (UTF-8)
```