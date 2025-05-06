from logic import *     # Se importa la libreria logig.py

# Se definen los simbolos / tarjetas
mustard = Symbol("ColMustard")
plum = Symbol("ProfPlum")
scarlet = Symbol("MsScarlet")

ballroom = Symbol("ballroom")
kitchen = Symbol("kitchen")
library = Symbol("library")

knife = Symbol("knife")
revolver = Symbol("revolver")
wrench = Symbol("wrench")

simbolos = [
    mustard, plum, scarlet, 
    ballroom, kitchen, library, 
    knife, revolver, wrench
    ]
# Acumula todo lo que se sabe
conocimiento = And(
    Or(mustard, plum, scarlet), 
    Or(ballroom, kitchen, library), 
    Or(knife, revolver, wrench))
# Iniciales
conocimiento.add(And(Not(scarlet), Not(ballroom), Not(knife)))
# Al menos una de ellas es falsa
conocimiento.add(Or(Not(mustard), Not(library), Not(wrench)))
# Se sabe con certeca que no fué
conocimiento.add(Not(plum))
# Se sabe que no fué en...
conocimiento.add(Not(kitchen))


for simbolo in simbolos:
    if model_check(conocimiento,simbolo):
        print(f"{simbolo}: VERDADERO")
    elif model_check(conocimiento, Not(simbolo)):
        print(f"{simbolo}: FALSO")
