# A simple generator function
def my_gen():
    n = 1
    print('This is printed first')
    # Generator function contains yield statements
    yield n

    n += 1
    print('This is printed second')
    yield n

    n += 1
    print('This is printed at last')
    yield n

a = my_gen()
next(a) 
next(a)
next(a)
next(a)
next(a)




'''results
This is printed first
1
 # Once the function yields, the function is paused and the control is transferred to the caller.
 # Local variables and theirs states are remembered between successive calls.
This is printed second
2

This is printed at last
3

 # Finally, when the function terminates, StopIteration is raised automatically on further calls.

Traceback (most recent call last):
...
StopIteration
Traceback (most recent call last):
...
StopIteration'''
