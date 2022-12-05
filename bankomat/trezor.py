
slovnik = {}
max_c = 0

automat = int(input("Zadejte Vaši částku, prosím : "))

with open("trezor.txt", "r") as t:
    for hodnoty in t.readlines():
        hodnoty = hodnoty.strip()
        hodnoty = hodnoty.split()
        slovnik.update({int(hodnoty[0]) : int(hodnoty[1])})

for key in slovnik.keys():
    max_c += slovnik[key] * key

if automat > max_c:
    print("V tomto zařízení se nenachází zadaná hodnota peněz.")
    exit()

for key in slovnik.keys():
    if automat // key != 0:
        pocet = automat // key
        if pocet <= slovnik[key]:
            automat -= pocet * key
            slovnik.update({key : slovnik[key] - pocet})
            print("Výběr částky: ", key,"Kč ", pocet, " krát")
        else:
            pocet = slovnik[key]
            automat -= pocet * key
            slovnik.update({key : slovnik[key] - slovnik[key]})
            print("Výběr částky: ", key,"Kč ", pocet, " krát")

with open("trezor.txt", "w") as t:
    for key,value in slovnik.items():  
        t.write(f"{key}   {slovnik[key]}\n")