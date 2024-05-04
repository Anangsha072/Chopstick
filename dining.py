phil = [0, 0, 0, 0, 0]
chopstick = [0, 0, 0, 0, 0]

def signal(z):
    phil[z] = 0
    chopstick[z] = 0
    chopstick[(z + 1) % 5] = 0

def wait(y):
    if chopstick[y] == 0 and chopstick[(y + 1) % 5] == 0:
        phil[y] = 1
        chopstick[y] = 1
        chopstick[(y + 1) % 5] = 1
    elif phil[y] == 1:
        w = int(input(f"Do you want Philosopher {y} to stop eating (1/0): "))
        if w == 1:
            signal(y)
    else:
        print(f"Chopsticks {y} and {(y + 1) % 5} are busy")
        print(f"Philosopher {y} has to wait")

def main():
    for i in range(5):
        phil[i] = 0
        chopstick[i] = 0

    while True:
        for i in range(5):
            if phil[i] == 0:
                print(f"Philosopher {i} is thinking")
                print()
            else:
                print(f"Philosopher {i} is eating")
                print()
        
        s = int(input("Which philosopher is eating: "))
        wait(s)
        
        u = int(input("Do you want to continue (1/0): "))
        if u != 1:
            break

if '__name__' == "_main_":
    main()
        

         
