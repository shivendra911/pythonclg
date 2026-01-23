relational operator
A relational operator is used in programming to compare two values. The result of a relational operation is always either True or False. In Python, the main relational operators are:

## Relational Operators in Python

| Operator | Description              | Example      | Result   |
|----------|--------------------------|--------------|----------|
| ==       | Equal to                 | 5 == 3       | False    |
| !=       | Not equal to             | 5 != 3       | True     |
| >        | Greater than             | 5 > 3        | True     |
| <        | Less than                | 5 < 3        | False    |
| >=       | Greater than or equal to | 5 >= 5       | True     |
| <=       | Less than or equal to    | 3 <= 5       | True     |

**Example in code:**

a = 10
b = 20
print(a > b)   # False
print(a < b)   # True


not vs !=

!= : Relational operator that checks if two values are not equal
not : Logical operator that negates (inverts) a boolean value# != compares two values
Key Differences:

Operator	Type	                    Use Case	            Example
!=	        Relational	                Compare two values	    5 != 3 → True
not        	Logical	Negate a boolean	not                     True → False


a = 10
b = 20
print(a != b)   # True (10 is not equal to 20)

# not negates a boolean
x = True
print(not x)    # False (negates True)

print(not (a == b))  # True (not False)
print(a != b)        # True (same result, different approach)

# not can be used with conditions
if not a == b:
    print("a is not equal to b")  # This prints

# Equivalent to:
if a != b:
    print("a is not equal to b")  # This also prints