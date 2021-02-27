from cs50 import get_int

while True:
    # Prompt the user for height
    height = get_int("Enter a number between 1 and 8: ")
    if height > 0 and height < 9:

        for i in range(0, height):
            for j in range(0, height):
                # Adjust the position of pyramid
                if (j < height - i-1):
                    print(" ", end="")
            print("#"*(i+1), end="")
            print("  ", end="")
            # Right pyramid
            print("#"*(i+1))
        break