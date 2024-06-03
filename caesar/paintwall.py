print(f"1 can of paint can cover 5 square meters of wall, given a random height and width of wall, calculate hom many can of paint can can be used to paint the wall")

test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))

coverage = 5
paint = (test_h * test_w) / coverage
paint =round(paint)
print(f"You will need {paint} cans of paint.")