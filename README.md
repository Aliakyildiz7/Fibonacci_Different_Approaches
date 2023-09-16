# Fibonacci_Different_Approaches
This code calculates the nth term of Fibonacci Series with 4 different methods.

The first method is iterative method which gradually adds to the list.
The  second method is recursive method which returns the Fibonacci Series of the previous term.
The third method is memoization with a cache dictionary to prevent recalculating of values.
The forth method is again memoization, buy with a built in decorator in Python.

It shows that recursive method with memoization (either with dictionary or decorator) is much faster than iterative method. 
For recursion without memoization, while it has comparable results in low n numbers, it gets proggresively slower to the point of being useless.
For this recursion without memoization is commented out in the code.
