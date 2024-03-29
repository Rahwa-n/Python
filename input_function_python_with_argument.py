The input() function with an argument
The input() function can do something else: it can prompt the user without any help from print().

We've modified our example a bit, look at the code:

anything = input("Tell me anything...")
print("Hmm...", anything, "...Really?")


Note:

the input() function is invoked with one argument - it's a string containing a message;
the message will be displayed on the console before the user is given an opportunity to enter anything;
input() will then do its job.
This variant of the input() invocation simplifies the code and makes it clearer.

The result of the input() function
We've said it already, but it must be unambiguously stated once again: the result of the input() function is a string.

A string containing all the characters the user enters from the keyboard. It is not an integer or a float.

This means that you mustn't use it as an argument of any arithmetic operation, e.g., you can't use this data to square it, divide it by anything, or divide anything by it.

anything = input("Enter a number: ")
something = anything ** 2.0
print(anything, "to the power of 2 is", something)


Prev Next