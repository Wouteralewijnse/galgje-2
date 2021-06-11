import random
import time



print("Voer uw naam in alstublieft:")
name = input()
print("Hallo " + name + "!")

counter = 0
woordenlijst = ["informatica", "informatiekunde", "spelletje", "aardigheidje", "scholier", "fotografie", "waardebepaling", "specialiteit", "verzekering", "universiteit", "heesterperk" ]

hetwoord = random.choice(woordenlijst)
lengtewoord = len(hetwoord)
temp = "." * lengtewoord

print("We gaan vandaag galgje spelen")

time.sleep(2)

print("Ben je klaar om de strijd aan te gaan?")

time.sleep(3)

print()
print("Je hebt 5 levens bij elke fout geraden letter gaat er een leven af")

time.sleep(1)

print('Zijn je 5 levens op zonder het woord te raden dan heb je verloren')