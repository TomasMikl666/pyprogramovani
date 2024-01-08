from data import test_data

from test_model import Test
from mozek_testu import MozekTestu

test_list = []


for jednaotazka in test_data:
    otazkatext = jednaotazka["text"]
    otazkaodpoved = jednaotazka["odpoved"]
    otazkaslovniodpoved = jednaotazka["slovniodpoved"]
    nova_otazka = Test(otazkatext,otazkaodpoved)
    test_list.append(nova_otazka)

test = MozekTestu(test_list)
while test.je_otazka() == True:
    test.dalsi_otazka()
    
print("Kone testu!")
print(F"Tvoje skore je {test.skore} / {test.cislo_otazky}")