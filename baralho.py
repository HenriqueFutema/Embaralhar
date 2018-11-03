import random
baralho = ["A♦","A♠","A♥","A♣","2♦","2♠","2♥","2♣","3♦","3♠","3♥","3♣","4♦","4♠","4♥","4♣","5♦","5♠","5♥","5♣","6♦","6♠","6♥","6♣","7♦","7♠","7♥","7♣","8♦","8♠","8♥","8♣","9♦","9♠","9♥","9♣","10♦","10♠","10♥","10♣","B♦","B♠","B♥","B♣","Q♦","Q♠","Q♥","Q♣","K♦","K♠","K♥","K♣"]
print("O baralho tem: {} cartas" .format(baralho.__len__()))
resposta = input("Digite s para embaralhar ou digite n para não embaralhar [s/n]")
num = random.randint(1, 51)

baralhoemb = []
if resposta == "s":
    lista = []
    for i in range(52):

        while (num in lista):
            num = random.randint(0, 51)
        lista.append(num)
    for x in range(52):
        baralhoemb.append(baralho[lista[x]])
    print(baralhoemb)
elif resposta == "n":
    print(baralho)