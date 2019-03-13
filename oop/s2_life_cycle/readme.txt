0. Object life cycle
Constructor:
+ __init__, you only implement one of these three: default, parameter or copy constructor
+ You can use this code to implement both default and copy constructor
-----------------------------
class Foo:
    def __init__(self, orig=None):
        if orig is None:
            self.non_copy_constructor()
        else:
            self.copy_constructor(orig)
    def non_copy_constructor(self):
        # do the non-copy constructor stuff
    def copy_constructor(self, orig):
        # do the copy constructor

a=Foo()  # this will call the non-copy constructor
b=Foo(a) # this will call the copy constructor
-----------------------------
+ Import copy for copy object

Destructor:
+ __del__, learn more in III below

Static:
+ Static variables:
----------------------------------------
Example code:
class Example:
    staticVariable = 5 # Access through class

print Example.staticVariable # prints 5

# Access through an instance
instance = Example()
print instance.staticVariable # still 5

# Change within an instance
instance.staticVariable = 6
print instance.staticVariable # 6
print Example.staticVariable # 5

# Change through
class Example.staticVariable = 7
print instance.staticVariable # still 6
print Example.staticVariable # now 7

==> when you change instance.staticVaribale = some_value,
it 'll create an new class variable name static varibale
----------------------------------------
+Static methods: learn more in II below

##################################################
I. __str__() and __repr__() (references: https://www.journaldev.com/22460/python-str-repr-functions)
- Implement for what display in print(obj)
+ __str__ must return string object whereas __repr__ can return any python expression.
+ If __str__ implementation is missing then __repr__ function is used as fallback. There is no fallback if __repr__ function implementation is missing.
+ If __repr__ function is returning String representation of the object, we can skip implementation of __str__ function.

##################################################
II. regular methoid, classmethod, static method (ref:
https://www.youtube.com/watch?v=rq8cL2XMM5M&t=41s)

+ Regular method: with no decorator, get self is the first argument (usually use)
+ Class method: with decorator @classmethod in header, get cls as the first argument
(purpose: calling constructor like __init__() or access class varibales(static variables))
+ Static method: with decorator @staticmethod in header, don't pass the instance (self) or
the class (cls), they are just normal functions which have some logical connection with the class


..learnmore: https://radek.io/2011/07/21/static-variables-and-methods-in-python/
..learnmore: https://www.programiz.com/python-programming/methods/built-in/classmethod

##################################################
III. Using destructor (ref: https://eli.thegreenplace.net/2009/06/12/safely-using-destructors-in-python/)

- Not too important because of python GS (Garbage Collector)

.. learn more: https://pymotw.com/3/weakref/

##################################################
IV. Copy constructor, shallow, deep copy (ref: https://realpython.com/copying-python-objects/)

+ Making a shallow copy of an object won’t clone child objects. Therefore, the copy is not fully independent of the original.
+ A deep copy of an object will recursively clone child objects. The clone is fully independent of the original, but creating a deep copy is slower.
+ You can copy arbitrary objects (including custom classes) with the copy module (copy.deepcopy())

==> child object in the object is the reason why there are two concept shallow and deep copy.

.. learn more: https://stackoverflow.com/questions/1241148/copy-constructor-in-python

