
#Execute a function with a argument twice
def do_twice(funct, arg):
    funct(arg)
    funct(arg)

def print_spam(t):
    print(t)


def print_2_times(arg):
    print(arg)
    print(arg)



#Execute a function four times using "do_twice"
def do_four(funct, arg):
    do_twice(funct, arg)
    do_twice(funct, arg)


