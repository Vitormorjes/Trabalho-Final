import pandas as pd
import matplotlib.pyplot as plt

all_password = pd.read_csv('top200senhas.csv')
#print(all_password) # Verificando se os dados foram importados

timetocrack = all_password[all_password["Time_to_crack_in_seconds"] < 1] #Verificando quantas são as senhas com senha para se hackear menor que 1 segundo
print("O número de senhas com tempo inferior à 1 segundo para hackear é igual a:", len(timetocrack), "senhas") #Mostrando o número de senhas com time to crack menor q 1 segundo
senhas = all_password["Password"] # Criando uma lista com todas as senhas
unique_passwords = list(set(senhas)) # Criando uma lista com todas senhas não repetidas

only_alpha = []
only_digit = []
with_digit = []
character_especial = []
for i in unique_passwords: #Um for para que i seje todas as senhas não repetidas
    if(i.isalpha() == True): #Verificando quais palavras há somente letras
        only_alpha+= [i]
    elif(i.isdigit() == True): #Verificando quais palavras há somente números
        only_digit+= [i]
    elif(i.isalnum() == False):  #Verificando quais palavras há contém caracteres especiais
        character_especial+= [i]
    else:
        with_digit += [i] #Verificando quais palavras há letras e números

print("Total de senhas analisadas:", len(all_password)) #Mostrando o total de senhas analisadas
print("Total de senhas não repetidas:", len(only_alpha)+len(only_digit)+len(with_digit)+len(character_especial)) #Mostrando o total de senhas não repetidas
print("Total de senhas não repetidas contendo apenas letras:", len(only_alpha))   #Mostrando o total de senhas não repetidas contendo apenas letras
print("Total de senhas não repetidas contendo apenas numeros:", len(only_digit))  #Mostrando o total de senhas não repetidas contendo apenas numeros
print("Total de senhas não repetidas contendo caracteres especiais:", len(character_especial)) #Mostrando o total de senhas não repetidas contendo caracteres especiais
print("Total de senhas não repetidas contendo apenas letras e numeros:", len(with_digit)) #Mostrando o total de senhas não repetidas contendo apenas letras e numeros
print('\n')

c = ['0','1','2','3','4','5','6','7','8','9'] #Lista com todos os algarismos
h = [0,0,0,0,0,0,0,0,0,0] #Lista para armazenar a quantidade de vezes que cada algarismo aparece em todas as senhas
max1 = -1
aux1 = -1
for x in range(0,10):                  #Esse for é responsavel por verificar individualmente 
    for n in unique_passwords:         #a quantidade de vezes que cada algarismo aparece em todas as senhas,
        if c[x] in str(n):             # ver qual o algarismo mais utilizado, quantas vezes ele aparece
            h[x] = h[x] + str(n).count(c[x])    #e armazenar esses dados em uma lista
            aux1 = h[x]
            if aux1 > max1:      #Esse if é responsavel por verificar qual o algarismo mais utilizado
                max1 = aux1
                num = c[x]
    print("A quantidade total de",c[x],"utilizado em todas as senhas é:",h[x]) #Mostrando a quantidade de vezes que cada algarismo aparece em todas as senhas
print('\n')
print("O algarismo mais utilizado em todas as senhas é o",num,"com",max1,"ocorrências") #Mostrando qual o algarismo mais utilizado em todas as senhas
print('\n')
z = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'] #Lista com todas as letras do alfabeto
b = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] #Lista para armazenar a quantidade de vezes que cada letra aparece em todas as senhas
max0 = -1
aux0 = -1
for x in range(0,26):           #Um for para verificar a quantidade de vezes que cada letra aparece em todas as senhas,
    for n in unique_passwords:  #e armazenar em uma lista
        if z[x] in str(n):
            b[x] = b[x] + str(n).count(z[x])
            aux0 = b[x]
            if aux0 > max0:   #Esse if é responsavel por verificar qual a letra mais utilizada
                max0 = aux0
                letra = z[x]
                
    print("A quantidade total de",z[x],"utilizado em todas as senhas é:",b[x]) #Mostrando a quantidade de vezes que cada letra aparece em todas as senhas
print('\n')
print("A letra mais utilizada em todas as senhas é:",letra,"com",max0,"ocorrências") #Mostrando qual a letra mais utilizada em todas as senhas

for x in range (1,6): #Um for para mostrar os o "top x" primeiros de cada país (nesse caso top 5)
     print('\n')      
     print("O top",x,"de cada pais é: ") 
     print(all_password[all_password["Rank"] == x])  #Mostrando o "top x" de cada país

plt.bar(c,h,color="red") #Criando um gráfico de barras com os algarismos e a quantidade de vezes que eles aparecem
plt.xticks(c) #Definindo os algarismos como os valores do eixo x
plt.xlabel("Algarismos") #Definindo o nome do eixo x
plt.ylabel("Quantidade de vezes que aparece") #Definindo o nome do eixo y
plt.title("Quantidade de vezes que cada algarismo aparece em todas as senhas") #Definindo o título do gráfico
plt.show() #Mostrando o gráfico

plt.bar(z,b,color="blue") #Criando um gráfico de barras com as letras e a quantidade de vezes que elas aparecem
plt.xticks(z) #Definindo as letras como os valores do eixo x
plt.xlabel("Letras") #Definindo o nome do eixo x
plt.ylabel("Quantidade de vezes que aparece") #Definindo o nome do eixo y
plt.title("Quantidade de vezes que cada letra aparece em todas as senhas") #Definindo o título do gráfico
plt.show() #Mostrando o gráfico