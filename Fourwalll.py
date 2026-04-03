l=float(input("Enter the length of the room:"))
b=float(input("Enter the breadth of the room:"))
h=float(input("Enter the height of the room:"))
AOW=2*h*(l+b)
print("Area of the walls is:",AOW)

#function
def AOW():
  l=float(input("Enter the length of the room:"))
  b=float(input("Enter the breadth of the room:"))
  h=float(input("Enter the height of the room:"))
  AOW=2*h*(l+b)
  return f"Area of the walls:{AOW}"
print(AOW())
