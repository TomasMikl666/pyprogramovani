# input: co byste si dal : (espress/latte/cappucino)   , lze zadat report , pokud napíšu report zobrazí se kolik tam je vody , kávy , mléka
# když vyberu třeba espresso tak se odečtou ingredience
#print: vložte minci 1,2,5,10,20,50
#input: kolik 1kč chcete vložit , kolik 2 kč chcete vložit...
#print: celkem jste vložili 50kč
#print cena espressa je 40kč
#print nápoj se připravuje
#print: zde je {zbytek} na zpátek
#po tomhle zkusim napsat report , zda se ingredience odečettli


#NAPIŠ report PRO KONTROLU MNOŽSTVÍ SUROVIN
from machine_dict import MENU
from machine_dict import resources

def odecti_zdroje(typ:str) -> None:
    voda_epresso =MENU[typ]["ingredients"]["water"]
    mleko_epresso =MENU[typ]["ingredients"]["milk"]
    kava_epresso =MENU[typ]["ingredients"]["coffee"]
    
    resources["water"] = resources["water"] - voda_epresso
    resources["milk"] = resources["milk"] - mleko_epresso
    resources["coffee"] = resources["coffee"] - kava_epresso
    if resources["water"] < voda_epresso:
        print("Není voda")
    elif resources["milk"] < mleko_epresso:
        print("Není mléko")
    elif resources["coffee"] < kava_epresso:
        print("Není káva")

def placeni() -> int:
    celkovy_penize = 0
    print("Vložte mince: 1, 2, 5, 10, 20, 50")
    zadej_kolik_jednokorun = int(input("Zadej počet 1: "))
    celkovy_penize += zadej_kolik_jednokorun * 1
    print(celkovy_penize)
    zadej_kolik_dvoukorun = int(input("Zadej počet 2: "))
    celkovy_penize += zadej_kolik_dvoukorun * 2
    print(celkovy_penize)
    zadej_kolik_petikorun = int(input("Zadej počet 5: "))
    celkovy_penize += zadej_kolik_petikorun * 5
    print(celkovy_penize)
    zadej_kolik_desetikorun = int(input("Zadej počet 10: "))
    celkovy_penize += zadej_kolik_desetikorun * 10
    print(celkovy_penize)
    zadej_kolik_dvacek = int(input("Zadej počet 20: "))
    celkovy_penize += zadej_kolik_dvacek * 20
    print(celkovy_penize)
    zadej_kolik_padesatikorun = int(input("Zadej počet 50: "))
    celkovy_penize += zadej_kolik_padesatikorun * 50
    print(f"Celkem jste vložili: {celkovy_penize}") 
    return celkovy_penize

def druh_kavy(typ:str):
    cena_espresso = MENU[typ]["cost"]
    platba = placeni()
    
    if cena_espresso > platba:
        print("Nedostatek peněz kamaráde")
    elif cena_espresso < platba:
        zbytek_vratit = platba - cena_espresso
        print(f"Vracíme: {zbytek_vratit}")
        odecti_zdroje(typ)
        
    else:
        odecti_zdroje(typ)

def kontrola_zdroju():
    voda_resources = resources["water"]
    mleko_resources = resources["milk"]
    kava_resources = resources["coffee"]
    print(f"Voda:{voda_resources}")
    print(f"Mléko:{mleko_resources}")
    print(f"Káva:{kava_resources}")

def doplneni_zdroju() -> None:
    konec = False
    while not konec:
        doplneni = input("Pro doplňěné zadej: 'voda' , 'mleko', 'kava' nebo konec: ")
        max_voda = 400
        max_mleko = 300
        max_kava = 150
        if doplneni == 'voda':
            mnozstvi = int(input("Zadej množství suroviny: "))
            resources["water"] = resources["water"]+mnozstvi
            if resources["water"] > max_voda:
                resources["water"] == 400
                print(f"Maximum vody je 400, aktuální množství je: {max_voda}")
        elif doplneni == 'mleko':
            mnozstvi = int(input("Zadej množství suroviny: "))
            resources["milk"] = resources["milk"]+mnozstvi
            if resources["milk"] > max_mleko:
                resources["milk"] == 300
                print(f"Maximum mleka je 300, aktuální množství je: {max_mleko}")
        elif doplneni == 'kava':
            mnozstvi = int(input("Zadej množství suroviny: "))
            resources["coffee"] = resources["coffee"]+mnozstvi
            if resources["coffee"] > max_kava:
                resources["coffee"] == 150
                print(f"Maximum kavy je 150, aktuální množství je: {max_kava}")
        elif doplneni == "konec":
            konec = True
        else:
            print("error404")


konec = False
while not konec:

    volba = input("Vyberte: espresso , latte , cappucino: ")
    if volba.lower() == "espresso":
        druh_kavy("espresso")
        
    elif volba.lower() == "latte":
        druh_kavy("latte")

    elif volba.lower() == "cappucino":
        druh_kavy("cappucino")
        
    elif volba.lower() == "report":
        kontrola_zdroju()
        doplneni_zdroju()

    else:
        print("object not found")