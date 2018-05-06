#function to write temp in f in txt file
temperatures=[10,-20,-289,100]

def writer(temp):
    with open("temps.txt", 'w') as file:
        for temp in temperatures:
            if temp>-273.15:
                f=9/5*temp + 32
                file.write(str(f) + '\n')
writer(temperatures)
