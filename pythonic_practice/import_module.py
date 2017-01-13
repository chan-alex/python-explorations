
import module_demo.module1   # this is an example of absolut import


o1 = module_demo.module1.m1()


from module_demo.module1 import m1  # this is another way to import

o2 = m1()


from module_demo.module1 import global_var  

print(global_var)
