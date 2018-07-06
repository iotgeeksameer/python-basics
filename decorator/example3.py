def my_decorator(some_function):

    def wrapper():

        num = 10

        if num == 10:
            print("Yes!")
        else:
            print("No!")

        some_function()

        print("Something is happening after some_function() is called.")

    return wrapper


if __name__ == "__main__":
    my_decorator()




from decorator07 import my_decorator


@my_decorator
def just_some_function():
    print("Wheee!")

just_some_function()



'''result 
Yes!
Wheee!
Something is happening after some_function() is called'''
# @my_decorator is just an easier way of saying just_some_function = my_decorator(just_some_function).
# It’s how you apply a decorator to a function.

