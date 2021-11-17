# %%
3 % 5

# %%
6 %6

# %%
print(i in range(2,6))

# %%
for i in range(2,6):
    print(i)

# %%
print(*range(1,2))

# %%
print(*range(1,10))

# %%
*range(1,10)

# %%
def hi(name="yasoob"):
    def greet():
        return "now you are in the greet() function"
 
    def welcome():
        return "now you are in the welcome() function"
 
    if name == "yasoob":
        return greet
    else:
        return welcome
 
a = hi()


