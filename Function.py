
# lets first start with the conventional Hello world function

def myfun():
    print("hello coders.")
    print("whats upp..")
    
myfun()
    
def sons(*args):
    print("my obedient son is:",args[2])
    
sons("ram","shyam","hari","vishnu")

def key_func(first,second,third):
    print("my first god name is:" + first)
    
key_func(first = "ram", second = "hari", third = "shyam")

def key_wala(**args):
    print("my fav god name is:" , args["second"])
    
key_wala(first = "ram", second = "hari", third = "shyam")

def my_function(country = "Norway"):
  print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")
