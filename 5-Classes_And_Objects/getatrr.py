
"""In order to avoid infinite recursion in this method, 
its implementation should always call the base class method with the same name to access any attributes it needs,
 for example, object.__getattribute__(self, name)."""


class Yeah(object):
    def __init__(self, name):
        self.name = name
    # Gets called when an attribute is accessed
    def __getattribute__(self, item):
        print ('__getattribute__ ', item)
        # Calling the super class to avoid recursion
        return super(Yeah, self).__getattribute__(item)
    # Gets called when the item is not found via __getattribute__
    def __getattr__(self, item):
        print ('__getattr__ ', item)
        return super(Yeah, self).__setattr__(item, 'orphan')


yeah = Yeah('yes')
yeah.name