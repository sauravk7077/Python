#import module as namespace
import helpers
helpers.display("It is not a warning")

#import all into current namespace
from helpers import *
display("Not a warning")

#import specific items into current namespace
from helpers import display
display("Not a warning")


import sys

sys.path.append('c:\\Users\\racer\\Documents\\Module')

from some_random_module import do_something_stupid as stupid
stupid(5)
