"""
Description: In this python module we calculate the Greatest Common Divisor between 2 natural numbers.
"""


# def is a python keyword to define a python function
# function name is gcd
# def gcd -> after this we start parenthesis '(' and write the arguments name separated by comma
# here we use num1 and num2 as the arguments name
# num1 and num2 are natural numbers for which we will calculate the gcd
# after giving the arguments, we close the parenthesis ')' and put a colon

def gcd(num1, num2):
    # then we define a variable named as div with initial value as 1, which acts as gcd value
    div = 1
    # in next line we define a variable named as counter with initial value as 1
    # and this will work as a counter
    counter = 1

    # we create a while loop which will run till our counter equals either of the num1 or num2
    while counter <= num1 and counter <= num2:
        # Now an if condition inside while loop, which will calculate modulus or remainder when
        # num1 is divided by counter variable count and num2 is divided by counter variable count
        # and compares there modulus to zero
        if (num1 % counter) == 0 and (num2 % counter) == 0:
            # if the condition satisfy then assign the value of counter to div
            div = counter

            # then print the div
            # there are many syntax-es of print function in python
            # Here, print followed by a parenthesis '(' and then a string as "div=" enclosed in double quotes
            # then a comma, then our variable named div
            print("div= ", div)

        # Now our if conditional block is over and control comes to next statement after the `if` block
        # then we increment our counter
        # but we are still inside the while loop
        counter = counter + 1

        # then we print the counter again, using same syntax as above.
        print("counter=", counter)

        # now control will go back to 1st statement of the while loop and checks again
        # till the while condition isn't met.

    # once the while loop is over then our div variable has the largest gcd between the 2 numbers.
    # and we return from the function that div value
    return div


# Now comes the calling or invocation of the gcd function
# here we will pass our numbers, let's say 16 and 1000
# and store the gcd function results in variable named as res
# Syntax is variable name equals sign and then the function name, start parenthesis, pass 1st value, then 2nd value
# and close the parenthesis
res = gcd(16, 1000)

# Then we print the value of res, using the same above syntax
print("gcd=", res)

# another try for invocation of the gcd function
res = gcd(200, 100)
print("gcd=", res)

# And our code is over now.
