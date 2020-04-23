def f():
    # Local scope
    s = "Me too."
    print(s)

# Global scope
s = "It is great."

print(f())
print(s)