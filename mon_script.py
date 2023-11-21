x = input()
PIN = "0339"
nbressai = 1

while ((x != PIN) & (nbressai < 3)):
    
    print("code incorrect, recommencez")
    
    x = input()
    
    nbressai = nbressai + 1

if x != PIN:
    
    print("carte avalée, contactez votre conseiller")
    
else:
    
    print("code bon")