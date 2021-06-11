import random
import time
import re


print("Voer uw naam in alstublieft:")
name = input()
print("Hallo " + name + "!")

counter = 0
woordenlijst = ["informatica", "informatiekunde", "spelletje", "aardigheidje", "scholier", "fotografie", "waardebepaling", "specialiteit", "verzekering", "universiteit", "heesterperk" ]

woordkeuze = random.choice(woordenlijst)
lengtewoord = len(woordkeuze)
temp = "." * lengtewoord

print("We gaan vandaag galgje spelen")

time.sleep(2)

print("Ben je klaar om de strijd aan te gaan?")

time.sleep(2)

print()
print("Je hebt 5 levens bij elke fout geraden letter gaat er een leven af")

time.sleep(2)

print('Zijn je 5 levens op zonder het woord te raden dan heb je verloren')

time.sleep(2)

print("Het woord heeft " + str(lengtewoord) + " letters")

while True:
  gokje = (input(": "))
  match = re.search(gokje, woordkeuze)
  if gokje == woordkeuze: 
    print('Goed gedaan! Je heb het woord ' + '"' + woordkeuze + '"' + " geraden")
    print("Dit is het einde van het spel. Klik op 'Run' om het spel nogmaals te spelen!")
    break

 elif match: 
    print("Goed gedaan! raad verder.")
    for i in range(0, lengtewoord):
      if gokje == woordkeuze[i]:
        temp = temp[:i] + gokje +temp[i+1:]
    print(temp)




