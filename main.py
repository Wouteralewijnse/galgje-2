import random
import time



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

gok = (input(": "))
match = re.search(gok,woordkeuze)

