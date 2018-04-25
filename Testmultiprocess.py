import multiprocessing

def calc_plus(numbers) :
    for n in numbers:
        print('tambah ' + str(n+n))

def calc_square(numbers) :
    for n in numbers:
        print('kali ' + str(n*n))

if __name__ == "__main__" :
    arr = [2,3,6,8]
    p1 = multiprocessing.Process(target=calc_plus, args=(arr,))
    p2 = multiprocessing.Process(target=calc_square, args=(arr,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()




    print("selesai!")