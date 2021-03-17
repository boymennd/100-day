from flask import Flask
import time

app = Flask(__name__)


def speed_calc_decorator(function):
    def wrapper_fun():
        start_time = time.time()
        function()
        end_time = time.time()
        print(f"{function.__name__} run speed: {end_time - start_time}")

    return wrapper_fun


@speed_calc_decorator
def function_1():
    for i in range(100000):
        i + i


@speed_calc_decorator
def function_2():
    for i in range(1000000000):
        i + i


function_1()
function_2()
