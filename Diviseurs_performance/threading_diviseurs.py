from threading import *

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
    
    thread1 = Thread(target=trouver_diviseurs, args= (10000000, liste_de_diviseurs1))
    thread2 = Thread(target=trouver_diviseurs, args= (10000000, liste_de_diviseurs2))
    thread3 = Thread(target=trouver_diviseurs, args= (10000000, liste_de_diviseurs3))
    thread4 = Thread(target=trouver_diviseurs, args= (10000000, liste_de_diviseurs4))
    
    thread1.start()
    thread2.start()
    thread3.start()
    thread4.start()
    
    thread1.join()
    thread2.join()
    thread3.join()
    thread4.join()
    
    print(f"{liste_de_diviseurs1}\n{liste_de_diviseurs2}\n{liste_de_diviseurs3}\n{liste_de_diviseurs4}") 

if __name__ == "__main__":
    main()

