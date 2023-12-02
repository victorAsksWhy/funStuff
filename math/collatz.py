# A Collatz sequence generator.
# In case you don't know whta that is, it basically is a rule that says if a number is even,  it.half
# If it is odd, multiply it by three and add one.
# For whatever reason, it keeps looping 4, 2, 1, 4, 2, 1...
# The program stops when this happens
# This doesn't do anything bt default, it's just a function

def collatz(n):
    output = []
    while n != 1:
        if n % 2 == 0: # If even
            n = n/2
            output.append(n)
        else: # If odd
            n = 3 * n + 1
            output.append(n)
    return output

print(collatz(2763))