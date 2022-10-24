# try- except statements is for handling cases when incorrect arguments are passed to a function
# catch exceptions with try clause
# except do something about the error
def sqrt(x):
    '''catch TypeErrors and let other errors pass thru'''
    try:
        return x ** 0.5
    except TypeError:
        print('x must be an int or float')
sqrt('b')