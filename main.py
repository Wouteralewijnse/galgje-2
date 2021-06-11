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

 else: 
    print("Nee helaas! Deze letter zit niet in het woord.")
    counter = counter + 1
    if counter == 1:
      print("""  
     |
     |
     |
     |
     |
_____|""")
      print(naam + ", je hebt nog 4 beurten over.")
    
    elif counter == 4:
      print("""  ____
  | \|
     |
     |
     |
     |
_____|""")
      print(naam + ", je hebt nog 3 beurten over.")
    elif counter == 5:
      print("""  ____
  | \|
  0  |
     |
     |
     |
_____|""")
      print(naam + ", je hebt nog 3 beurten over.")
    elif counter == 6:
      print("""  ____
  | \|
  0  |
  |  |
     |
     |
_____|""")
      print(naam + ", je hebt nog 2 beurten over.")
    elif counter == 8:
      print("""  ____
  | \|
  0  |
 /|\ |
     |
     |
_____|""")
      print(naam + ", je hebt nog 1 beurten over.")
    elif counter == 9:
      print("""  ____
  | \|
  0  |
 -|- |
 /   |
     |
_____|""")
      print(naam + ", je hebt nog 0,5 beurt over.")
    elif counter == 10:
      print("""  ____
  | \|
  0  |
 -|- |
 / \ |
     |
_____|""") 
      time.sleep(1)
      print('helaas! Je kon het woord niet vinden binnen de beurten. Speel opnieuw en win!')
      
      time.sleep(1)
      print()
      print("Je hebt het einde van het spel gehaald. Klik op 'Run' om het nog een keer te spelen!")
      break




