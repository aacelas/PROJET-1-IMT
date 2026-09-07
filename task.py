import argparse

parser = argparse.ArgumentParser()

parser.add_argument("file", type=str, help="Nom ficher")
parser.add_argument("option", type=str, help="Option a faire a ficher")
parser.add_argument("content", nargs="*", help="Afficher le contenu du ficher")
#subparsers = parser.add_subparsers(dest="content",required=False) #TODO fix the subparsers

args = parser.parse_args()

try:
    file = open(args.file, "r")
except FileNotFoundError:
    file = open(args.file, "w")
    file.write("Id. Description.\n")
    file.close()

if args.option == "show":
    file = open(args.file, "r")
    print(file.read())
    file.close()
elif args.option == "add":
    with open(args.file, "r", encoding="utf-8") as file:
        lignes = file.readlines()
    if len(lignes) == 1:
        id = 1
    else:
        derniere_ligne = lignes[-1].strip()
        premier_caractere = derniere_ligne[0]
        id = int(premier_caractere) + 1

    with open(args.file, "a", encoding="utf-8") as file:
        file.write(str(id) + " " + " ".join(args.content) + "\n")

#elif args.option == "rm": TODO remove the line from the file
    #idRm = args.content[0]
    #with open("lestaches.txt", "r", encoding="utf-8") as file:
        #for linea in file:
            #if linea and linea[0] == idRm: 
#elif args.option == "modify": TODO edit the line from the file
else:
    print("Option invalide. Veuillez choisir 'show', 'add', 'rm' ou 'modify'.") 