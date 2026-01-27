"""
While Loop and Entry-Controlled Loop Concepts

A while loop is an entry-controlled loop statement that repeatedly executes a block 
of code as long as a specified condition evaluates to True.

Entry-Controlled Loop:
- The condition is checked BEFORE entering the loop body for the first time
- If the condition is False initially, the loop body never executes
- Examples: while loops, for loops

Syntax:
    while condition:
        # Loop body - code to execute repeatedly
        statement1
        statement2
        # Update condition to avoid infinite loop
        update_variable

Parameters:
    condition: A boolean expression that is evaluated before each iteration
               The loop continues while this condition is True

Key Points:
- The loop body executes only if the condition is True
- After each iteration, the condition is re-evaluated
- Must update variables inside the loop to eventually make condition False
- Infinite loop occurs if condition never becomes False

Example:
    counter = 0
    while counter < 5:
        print(counter)
        counter += 1  # Update to eventually exit loop

Use Cases:
- When the number of iterations is unknown beforehand
- Processing user input until valid input is received
- Reading data until end-of-file
- Game loops and real-time applications
"""