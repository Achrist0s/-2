Python 3.9.7 (tags/v3.9.7:1016ef3, Aug 30 2021, 20:19:38) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> orders ={
'slave' : 300,
'beef' : 56,
'juice' : 28,
'tee' : 19,
}
>>> sorted_dic= sorted (orders.items(), key=lambda x:[1])
>>> print(sorted_dic) # [('tee'), 19), ('juice', 28), ('beef',56), ('slave',300)]
[('slave', 300), ('beef', 56), ('juice', 28), ('tee', 19)]
>>> a =179
>>> b = 971
>>> c = (a**2+b**2)**0.5
>>> print (c)
987.361129475938
>>> my_list = ["leaf", "cherry", "fish"]
>>> my_list1 = ["D","C","B","A"]
>>> my_list2 = [1,2,3,4,5]
>>> my_list.sort() # ['cherry', 'fish', 'leaf']
>>> my_list1.sort() # ['A', 'B', 'C', 'D']
>>> print(sorted(my_list2, reverse=True)) # [5, 4, 3, 2, 1]
[5, 4, 3, 2, 1]
>>> a=3
>>> b=4
>>> a, b = b, a
>>> print(a, b) # a= 4, b=3
4 3
>>> a= "СЛАВА УКРАЇНІ!!!"
>>> b= "ГЕРОЯМ СЛАВА !!!"
>>> print(a, b)
СЛАВА УКРАЇНІ!!! ГЕРОЯМ СЛАВА !!!
>>> 