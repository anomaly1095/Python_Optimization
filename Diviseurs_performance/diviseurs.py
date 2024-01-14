def trouver_diviseurs(x: int, liste_de_diviseurs: list)->list:
    print("starting search")
    for i in range(1, x):
        if x % i == 0:
            liste_de_diviseurs.append(i)
    return liste_de_diviseurs

def main():
    liste_de_diviseurs1 = []
    liste_de_diviseurs2 = []
    liste_de_diviseurs3 = []
    liste_de_diviseurs4 = []
    
    liste_de_diviseurs1 = trouver_diviseurs(x= 10000000 , liste_de_diviseurs = liste_de_diviseurs1)
    liste_de_diviseurs2 = trouver_diviseurs(x= 10000000 , liste_de_diviseurs = liste_de_diviseurs2)
    liste_de_diviseurs3 = trouver_diviseurs(x= 10000000 , liste_de_diviseurs = liste_de_diviseurs3)
    liste_de_diviseurs4 = trouver_diviseurs(x= 10000000 , liste_de_diviseurs = liste_de_diviseurs4)
    
    print(f"{liste_de_diviseurs1}\n{liste_de_diviseurs2}\n{liste_de_diviseurs3}\n{liste_de_diviseurs4}") 

if __name__ == "__main__":
    main()