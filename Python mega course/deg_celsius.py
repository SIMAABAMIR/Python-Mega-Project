def cel_farh(celsius):
    if celsius>-273.15:
        far = 9/5*celsius +32
        return far
    else:
        return "Physical temp can't reach this value !! "

temperatures=[10,-20,-289,100]

for temp in temperatures:
    print("Temp in F: ", cel_farh(temp))
