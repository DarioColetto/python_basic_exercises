def print_vector(x, y, z):
    print (x, y, z)


vec_list = [1, 2, 3]  
vec_tuple = (1, 2, 3)
vec_dict = {'x': 1, 'y': 2, 'z': 3} 

# #a la vieja escuela
# print_vector(vec_list[0], vec_list[1], vec_list[2])

# #usando el * refiere a todos los valores
# print_vector(*vec_tuple)
# print_vector(*vec_list)


print_vector(*vec_dict) #devuelve solo las Keys 'x' 'y' 'z'
print_vector(**vec_dict) #devuelve los valores de las Keys

# Conclusions#
# *args and **kwargs can help us write more flexible interfaces for our modules and functions.
# *args collects extra positional arguments as a tuple while **kwargs collects extra keyword arguments as dictionary.
# Actual syntax is * and **. Calling them args and kwargs is just a convention.
# * and ** can be used to unpack function arguments from sequences and dictionaries.