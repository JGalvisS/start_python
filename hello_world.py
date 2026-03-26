print("hello world")

#Variables
y=20
x=52
print(x)

# if basic
if x > y:
    print("y is greater than x")
    
#Casting
#Use type to know what kind of varible it is 
type_x = type(x) 
print(type_x)
#Use str to casting to string or .format
str_y= str(y)
type_y= type(str_y) 
print(type_y)
new_string= "this is a number {}"
print(new_string.format(x))

#tipos de colecciociones
#dict {}- clave/valor es mutable
my_dirct={"name":"jose","age":26}
print(my_dirct)
#list [] mantiene el orden de insercion, es mutable con append(), pop()
my_list=["mary","alvaro","jose"]
print(my_list)
my_list.append("carlos")
print(my_list)
#tupla () no se puede modificar 
my_tupla= ("margarita", "rosa","girasol")
print(my_tupla)
#set no mantiene el orden, permite agregar y eliminar elemtos, Elimina los duplicados 
my_set={"elsa","sebatian","mario"}
print(my_set)
