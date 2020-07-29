import sys

def main():
    n = int(input())
    i = 1
    j = 1

    for x in range(n):
        if (j > 2):
            j = 1
        if (j == 1):
            if (x != n - 1):
                sys.stdout.write("I hate")
                j += 1
            else:
                sys.stdout.write("I hate it")
                j += 1
            if (x < n - 1):
                sys.stdout.write(" that ")
        else:
            if (x == n - 1):
                sys.stdout.write("I love it")
                j += 1
            else:
                sys.stdout.write("I love")
                j += 1
            if (x < n - 1):
                sys.stdout.write(" that ")

if __name__ == '__main__':
    main()
