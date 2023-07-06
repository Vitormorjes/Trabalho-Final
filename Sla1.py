import pandas as pd

all_password = pd.read_csv('top200senhas.csv')
#print(all_password) # Verificando se os dados foram importados

timetocrack = all_password[all_password["Time_to_crack_in_seconds"] < 1] #Verificando quantas são as senhas com time to crack menor q 1 segundo
print("O número de senhas com tempo inferior à 1 segundo para hackear é igual a:", len(timetocrack)) # Verificando se os dados foram filtrados
#timetocrack.info() # Verificando se temos dados faltantes
senhas = all_password["Password"] # Criando uma lista com todas as senhas
cn = list(set(senhas)) # Criando uma lista com todas senhas não repetidas

only_alpha = []
only_digit = []
with_digit = []
character_especial = []
for i in cn:
    if(i.isalpha() == True): #Verificando se há somente letras
        only_alpha+= [i]
    elif(i.isdigit() == True): #Verificando se há somente números
        only_digit+= [i]
    elif(i.isalnum() == False):  #Verificando se há somente letras ou números
        character_especial+= [i]
    else:
        with_digit += [i] #Verificando se há caracteres especiais
#print(only_alpha)
#print(only_digit)
#print('a',character_especial)
#print(with_digit)
print("Total de senhas analisadas:", len(all_password))
print("Total de senhas não repetidas:", len(only_alpha)+len(only_digit)+len(with_digit)+len(character_especial))
print("Total de senhas não repetidas contendo apenas letras:", len(only_alpha)) 
print("Total de senhas não repetidas contendo apenas numeros:", len(only_digit))
print("Total de senhas não repetidas contendo caracteres especiais:", len(character_especial))
print("Total de senhas não repetidas contendo apenas letras e numeros:", len(with_digit))
print('\n')

# Australia = all_password[all_password["country"] == "Australia"]
# Austria = all_password[all_password["country"] == "Austria"]
# Belgium = all_password[all_password["country"] == "Belgium"]  
# Brazil = all_password[all_password["country"] == "Brazil"]  
# Canada = all_password[all_password["country"] == "Canada"]
# Chile = all_password[all_password["country"] == "Chile"]
# China = all_password[all_password["country"] == "China"]
# Colombia = all_password[all_password["country"] == "Colombia"]
# Czech = all_password[all_password["country"] == "Czech Republic"]
# Denmark = all_password[all_password["country"] == "Denmark"]
# Estonia = all_password[all_password["country"] == "Estonia"]
# Finland = all_password[all_password["country"] == "Finland"]
# France = all_password[all_password["country"] == "France"]
# Germany = all_password[all_password["country"] == "Germany"]
# Greece = all_password[all_password["country"] == "Greece"]
# Hungary = all_password[all_password["country"] == "Hungary"]
# India = all_password[all_password["country"] == "India"]
# Indonesia = all_password[all_password["country"] == "Indonesia"]
# Ireland = all_password[all_password["country"] == "Ireland"]
# Israel = all_password[all_password["country"] == "Israel"]
# Italy = all_password[all_password["country"] == "Italy"]
# Japan = all_password[all_password["country"] == "Japan"]
# Korea = all_password[all_password["country"] == "Korea"]
# Latvia = all_password[all_password["country"] == "Latvia"]
# Lithuania = all_password[all_password["country"] == "Lithuania"]
# Malaysia = all_password[all_password["country"] == "Malaysia"]
# Mexico = all_password[all_password["country"] == "Mexico"]
# Netherlands = all_password[all_password["country"] == "Netherlands"]
# New_Zealand = all_password[all_password["country"] == "New Zealand"]
# Nigeria = all_password[all_password["country"] == "Nigeria"]
# Norway = all_password[all_password["country"] == "Norway"]
# Phillippines = all_password[all_password["country"] == "Phillippines"]
# Poland = all_password[all_password["country"] == "Poland"]
# Portugal = all_password[all_password["country"] == "Portugal"]
# Romania = all_password[all_password["country"] == "Romania"]
# Russia = all_password[all_password["country"] == "Russia"]
# Saudi_Arabia = all_password[all_password["country"] == "Saudi Arabia"]
# Slovak_Republic = all_password[all_password["country"] == "Slovak Republic"]
# South_Africa = all_password[all_password["country"] == "South Africa"]
# Spain = all_password[all_password["country"] == "Spain"]
# Sweden = all_password[all_password["country"] == "Sweden"]
# Switzerland = all_password[all_password["country"] == "Switzerland"]
# Thailand = all_password[all_password["country"] == "Thailand"]
# Turkey = all_password[all_password["country"] == "Turkey"]
# Ukraine = all_password[all_password["country"] == "Ukraine"]
# United_Arab_Emirates = all_password[all_password["country"] == "United Arab Emirates"]
# United_Kingdom = all_password[all_password["country"] == "United Kingdom"]
# United_States = all_password[all_password["country"] == "United States"]
# Vietnam = all_password[all_password["country"] == "Vietnam"]
# a5 = all_password[all_password["Rank"] == 5]

# paises = [Australia,Austria,Brazil,Belgium,Canada,Chile,China,Colombia,Czech,Denmark,Estonia,Finland,France,Germany,Greece,Hungary,India,Indonesia,Ireland,Israel,Italy,Japan,Korea,Latvia,Lithuania,Malaysia,Mexico,Netherlands,New_Zealand,Nigeria,Norway,Phillippines,Poland,Portugal,Romania,Russia,Saudi_Arabia,Slovak_Republic,South_Africa,Spain,Sweden,Switzerland,Thailand,Turkey,Ukraine,United_Arab_Emirates,United_Kingdom,United_States,Vietnam]
#Lista com todas as senhas de cada um dos países

c = ['0','1','2','3','4','5','6','7','8','9']
h = [0,0,0,0,0,0,0,0,0,0]
max1 = -1
aux1 = -1
for x in range(0,10):       #Esse for é responsavel por verificar individualmente 
    for n in cn:            #a quantidade de vezes que cada algarismo aparece em todas as senhas
        if c[x] in str(n):  #e armazenar em uma lista
            h[x] = h[x] + str(n).count(c[x])
            aux1 = h[x]
            if aux1 > max1:
                max1 = aux1
                num = c[x]
    print("A quantidade total de",c[x],"utilizado em todas as senhas é:",h[x])
print('\n')
print("O algarismo mais utilizado em todas as senhas é o",num,"com",max1,"ocorrências")
print('\n')
z = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
b = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
max0 = -1
aux0 = -1
for x in range(0,26):  #Aqui há um for para cada letra de a até z 
    for n in cn:
        if z[x] in str(n):
            b[x] = b[x] + str(n).count(z[x])
            aux0 = b[x]
            if aux0 > max0:
                max0 = aux0
                letra = z[x]
                
    print("A quantidade total de",z[x],"utilizado em todas as senhas é:",b[x])
print('\n')
print("A letra mais utilizada em todas as senhas é: '",letra,"' com",max0,"ocorrências")

for x in range (1,6):
     print('\n')
     print("O top",x,"de cada pais é: ")
     print(all_password[all_password["Rank"] == x])


