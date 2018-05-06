temperatures=[10,-20,-289,100]
def c_to_f(c):
    if c>-273.15:
        f=9/5 * c + 32
        with open('c_to_f.txt', 'a+') as file:
            file.write(str(f) + '\n')
        return f
    else:
        return "that doesn't make  sense"


for temp in temperatures:
    print(c_to_f(temp))
