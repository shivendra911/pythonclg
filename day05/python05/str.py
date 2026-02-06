import sys

st = "Hello"
st2 = "Hello"


text = "Hello World"
print(sys.getsizeof(text))

print(f"st = {st}")
print(f"st2 = {st2}")
print(f"id(st) = {id(st)}")
print(f"id(st2) = {id(st2)}")
print(f"st == st2: {st == st2}")
print(f"st is st2: {st is st2}")