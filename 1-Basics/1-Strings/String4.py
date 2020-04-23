# Default order 
String4="{} {} {}".format("Geeks","For","Life")
print(String4)
# Positional Formatting
String4="{1} {0} {2}".format("Geeks","For","Life")
print(String4)
# Keywords Formatting
String4="{c} {b} {a}".format(a="Geeks",b="For",c="Life")
print(String4)

# Integers - Binary Representation
String4 = "{0:b}".format(4)
print(String4)
# Float - Exponential Representation
String4 = "{0:e}".format(165.6458)
print(String4)
# Round Off
String4 = "{0:.2f}".format(1/6)
print(String4)