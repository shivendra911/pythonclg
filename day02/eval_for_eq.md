1️⃣ What is eval()?

eval() evaluates a Python expression written as a string and returns the result.

Syntax
eval(expression)

Example
eval("10 + 5")
# Output: 15

2️⃣ Why eval() exists

Because input() always returns a string:

x = input("Enter: ")


If user types:

10+20


Python sees:

"10+20"   # string


eval() converts that string into:

10 + 20   # actual operation

3️⃣ Your case (expression input)
usr = eval(input("Enter an expression: "))


Input:

-10+11


Execution flow:

input() → returns "-10+11"

eval() → computes -10 + 11

Result stored in usr → 1

4️⃣ What eval() can evaluate
✅ Allowed
eval("5")
eval("10+20")
eval("2*3-4")
eval("(10+5)/3")
eval("3**2")

❌ Not statements
eval("x=5")      # ❌ assignment
eval("print(5)") # ❌ statement


Why?
Because eval() only works on expressions, not statements.

5️⃣ Difference between eval() and int() / float()
Function	Accepts expression	Accepts number only
int()	❌	✅
float()	❌	✅
eval()	✅	✅

Example:

float("10+5")   # ❌ error
eval("10+5")    # ✅ 15

6️⃣ eval() is powerful (and dangerous)
⚠️ Example of danger
eval("__import__('os').system('ls')")


This can:

delete files

run system commands

access environment

👉 Never use eval() with untrusted input

7️⃣ How to restrict eval() (important)

You can limit what eval() can access.

Safe math-only eval
usr = eval(input("Enter: "), {"__builtins__": None}, {})


Now:

math works

system calls ❌ blocked

8️⃣ Better alternative (REAL-WORLD)
Use ast.literal_eval() (safe)
import ast
ast.literal_eval("10+5")  # ❌
ast.literal_eval("10")    # ✅


📌 Limitation:
It does NOT evaluate expressions, only literals.

9️⃣ How calculators REALLY work (concept)

Real calculators:

Read input as string

Tokenize (10, +, 5)

Apply operator precedence

Compute result

👉 They do NOT use eval

(You’ll implement this in DSA / compiler subjects)

🔟 When to use eval() (exam answer)

✅ Use eval():

learning

simple expression evaluation

trusted input

❌ Avoid eval():

production apps

user-facing programs

web servers

✅ Final improved version of your program
try:
    usr = eval(input("Enter an expression: "), {"__builtins__": None}, {})

    if usr > 0:
        print("The result is positive.")
    elif usr < 0:
        print("The result is negative.")
    else:
        print("The result is zero.")

except:
    print("Invalid expression")
