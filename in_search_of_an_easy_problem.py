import sys

def main():
    x = 0
    k = 0
    n = 0

    for line in sys.stdin:
        x += 1
        if (x == 1):
            k = line
        elif (x == 2):
            n = line
            if ('1' in n.split()):
                print("HARD")
                return 0
            else:
                print("EASY")
                return 0

if __name__ == "__main__":
    main()