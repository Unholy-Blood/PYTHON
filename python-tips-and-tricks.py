### sets in python
# all elements in a set are unique
# no duplicate elements
my_set = {1,2,3,4,5,1,5,7,'alpha'}
# print(my_set)


### Dictionary in python
# stores data in a key value pair
my_dict = {'key':'value', 'hello':{'dict in dict':None}}
# print(my_dict)


### Assigning mor than one variable at once
x, y, z = 'first val', 'second val', ['any data type']
# print(x,y)


### Interchanging values of two variables
y,x = x,y
# print(x,y)


### Multiline strings
multiline_string = '''LINE ONE
LINE TWO
LINE THREE'''
# print(multiline_string)


### using {f_strings} to print() a variable inside a string
num = 99
# print(f'this is the number without using a comma "," {num}')


### print() without defalt /n at end
# print('xyz', end=' hello ')


### defining type of variable in a def func()
def func(a:str, b:int, c:float, d:list):
    pass


### Changing Data Types
num = 999
# print(f'hello {str(num)}')


### No return value of a func
def func() -> None: # using -> None will not return any value
    return print('blue'), print('why') # CAN still return a value


### the PASS keyword
# used as a space filler
# when no node is required to run without returning an error
def func():
    pass
#func()


### Classes and Objects
class Planet:
    def __init__(self, planet_name:str, universe_number:int=None) -> None:
        self.planet_name = planet_name
        self.universe_number = universe_number
    
    def info(self):
        print(F'THE NAME OF YOUR PLANET IS : {self.planet_name}')
        print(F'AND UNIVERSE NUMBER : {self.universe_number}')

jupiter = Planet('Jupiter')
# jupiter.info()


### SubClass
class Earth(Planet):
    def  __init__(self, universe_number: int = 1) -> None:
        self.universe_number = universe_number
        planet_name = "EARTH"
        super().__init__(planet_name, universe_number)
        # super enters the PARENT CLASS

earth = Earth('55')
# earth.info()