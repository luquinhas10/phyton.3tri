numero = 29  
primo = True
i = 2
if numero < 2:
    primo = False
else:
    while i * i <= numero:
        if numero % i == 0:
            primo = False
            break
        i += 1
print(primo)
