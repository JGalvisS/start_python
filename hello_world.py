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

#collection type
#dict {}- key/value it is mutable, use .keys() to get only keys on directory or .values() to get only values. you can call any value using the key ["key"].
my_dir={"name":"jose","age":26}
print(my_dir)
print(my_dir.keys())
print(my_dir.values())
print(my_dir["name"])
#set no mantiene el orden, permite agregar .add () y eliminar elementos .discard(), Elimina los duplicados 
my_set={"elsa","sebatian","mario"}
print(my_set)
#list [] keep insertion order, mutable use  .append() para agregar elemntos, .pop(), convertir en lista vacia .clear(), copiar todos los elemtos de la lista .copy) elimina elemtos con los que haga match .remove("object")
my_list=["mary","alvaro","jose"]
print(my_list)
my_list.append("carlos")
print(my_list)
#tuple () no change, method to count how many that elements appear in the tuple.count("object"), it let get index of element .index("object")
my_tuple= ("margarita", "rosa","girasol", "rosa")
print(my_tuple)
print(my_tuple.count("rosa"))
print(my_tuple.index("girasol"))
