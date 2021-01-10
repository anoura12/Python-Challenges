
def nearest_square(num):
    element = 0 # placeholder for containing the square.
    square = 0 # stores the square of the numbers till the given number.

    if(num < 0): # condition for negative numbers.
        return(0)

    for x in range(num):
        square = x ** 2 # finds square of the number.
        
        if(square <= num): #checks whether square is less than the number.
            if(square > element):
                element = square #holds the square of the current number until a new square is generated.

        else:
            return(element) #returns nearest square.
            break

