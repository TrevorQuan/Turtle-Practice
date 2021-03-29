import turtle

# Ask the user how many sides they want for the polygons
# Create the polygon based on the user input
# Error checking make sure the user's input is greater than 3 and less then 10
turtle.shape("turtle")


whileLoop = True
while(whileLoop == True):
  sides = int(input("How many sides do you want?(4-9): "))
  if(sides >= 3 and sides <= 10):
    whileLoop = False
  else:
    print("Error: That is not a number between 4-9.")

for i in range(sides):
  turtle.forward(100)
  turtle.right(360/sides)