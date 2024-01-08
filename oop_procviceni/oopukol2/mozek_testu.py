from main1 import otazkaslovniodpoved
class MozekTestu:
    def __init__(self,t_list:list) -> None:
        self.cislo_otazky = 0
        self.skore = 0
        self.otazky_list = t_list

    def dalsi_otazka(self):
        aktualni_otazka = self.otazky_list[self.cislo_otazky]
        
        self.cislo_otazky +=1
        odpoved_uzivatele = input(f"Otázka č. {self.cislo_otazky}: {aktualni_otazka.text} A , B , C:")
        self.kontrola_spravnosti(odpoved_uzivatele,aktualni_otazka.odpoved)

    def kontrola_spravnosti(self,odpoved_uzivatele:str,spravna_odpoved:str,):
        if odpoved_uzivatele.lower() == spravna_odpoved.lower():
            print("Správně!")
            self.skore +=1
            print(f"Tvoje skore je: {self.skore}/{self.cislo_otazky}")
        else:
            print(f"Špatně! odpoved je {otazkaslovniodpoved}")
            print(f"Tvoje skore je: {self.skore}/{self.cislo_otazky}")
    def je_otazka(self):
        if self.cislo_otazky < len(self.otazky_list):
            return True
        else:
            return False

