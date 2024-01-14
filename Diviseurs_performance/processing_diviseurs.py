import multiprocessing

def trouver_diviseurs(x: int, process_queue: multiprocessing.Queue)-> None:
    print("starting search")
    liste_de_diviseurs = []
    for i in range(1, x):
        if x % i == 0:
            liste_de_diviseurs.append(i)
    process_queue.put(liste_de_diviseurs)
    
def main():
    result_queue1 = multiprocessing.Queue()
    result_queue2 = multiprocessing.Queue()
    result_queue3 = multiprocessing.Queue()
    result_queue4 = multiprocessing.Queue()
    
    process1 = multiprocessing.Process(target= trouver_diviseurs, args=(10000000, result_queue1))
    process2 = multiprocessing.Process(target= trouver_diviseurs, args=(10000000, result_queue2))
    process3 = multiprocessing.Process(target= trouver_diviseurs, args=(10000000, result_queue3))
    process4 = multiprocessing.Process(target= trouver_diviseurs, args=(10000000, result_queue4))
    
    process1.start()
    process2.start()
    process3.start()
    process4.start()
    
    process1.join()
    process2.join()
    process3.join()
    process4.join()
    
    print(f"{result_queue1.get()}\n{result_queue2.get()}\n{result_queue3.get()}\n{result_queue4.get()}")

if __name__ == "__main__":
    main()