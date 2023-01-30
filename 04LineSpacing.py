# not recommended
# program to calculate the area of a rectangle
def area_rect():
  """Calculates the area of a rectangle"""
  length = float(input("What is the length of the side of the rectangle? "))
  width = float(input("What is the width of the side of the rectangle? "))
  Area = length * width
  print("The area of the rectangle is " + str(Area) + "cm^2")
area_rect()


# recommended
# program to calculate the area of a rectangle


def area_rect():
  """Calculates the area of a rectangle"""
  length = float(input("What is the length of the side of the rectangle? "))
  width = float(input("What is the width of the side of the rectangle? "))
  Area = length * width
  print("The area of the rectangle is " + str(Area) + "cm^2")


area_rect()
