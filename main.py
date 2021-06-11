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

print("We gaan lekker galgje spelen")
print("Ben je klaar om de strijd aan te gaan?")

time.sleep(3)

print()
print("Je hebt 5 levens bij elke fout geraden letter gaat er een leven af")

print("Het woord heeft" + str(lengtewoord) + "letters")