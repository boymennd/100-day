import time


def delay_fun(function):
    def wrapper_fun():
        time.sleep(2)
        function()
        function()
    return wrapper_fun


# @delay_fun
def hello():
    print("hello world")


@delay_fun
def bye():
    print("bye world")


@delay_fun
def cong():
    print("anh cong dep trai")


# hello()
# bye()
# cong()
hello_fun = delay_fun(hello)
hello_fun()