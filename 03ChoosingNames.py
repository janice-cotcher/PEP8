# not recommended
x = input("What is your name? ")
print("Hello, " + x + "!")

# recommended
name = input("What is your name? ")
print("Hello, " + name + "!")

# not recommended
def ar():
  """Calculates area of a rectangle"""
  l = float(input("What is the length of the side of the rectangle? "))
  w = float(input("What is the width of the side of the rectangle? "))
  A = l * w
  print("The area of the rectangle is " + str(A) + "cm^2")

ar()

# recommended
def area_rect():
  """Calculates the area of a rectangle"""
  length = float(input("What is the length of the side of the rectangle? "))
  width = float(input("What is the width of the side of the rectangle? "))
  Area = length * width
  print("The area of the rectangle is " + str(Area) + "cm^2")


area_rect()