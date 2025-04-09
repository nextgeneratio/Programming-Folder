def fun1(x):
  
    # This is the outer function that takes an argument 'x'
    def fun2(y):
      
        # This is the inner function that takes an argument 'y'
        return x + y  # 'x' is captured from the outer function
    
    return fun2  # Returning the inner function as a closure

# Create a closure by calling outer_function
closure = fun1(20)

# Now, we can use the closure, which "remembers" the value of 'x' as 10
print(closure(5)) 
D:\Downloades\Programming Folder\test folder\python\general test\test.py