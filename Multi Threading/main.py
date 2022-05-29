import threading
import time


def square(x):
    for i in x:
        time.sleep(2)
        print("Square  : " + str(i * i ))


def cube(x):
    for i in x:
        time.sleep(1)
        print("Cube : " + str(i * i * i))


if __name__ == "__main__":
    arr = [2, 4, 6, 8, 10, 12, 14]
    # square(arr)
    # cube(arr)

    # Creating Threads
    t1 = threading.Thread(target=square, args=(arr,))
    t2 = threading.Thread(target=cube, args=(arr,))

    # Start is used to start the thread
    t1.start()
    # If a thread used join, the main thread will stop executing till the join thread is completed
    t1.join()
    t2.start()
    t2.join()
