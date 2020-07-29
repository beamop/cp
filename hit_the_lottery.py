def main():
    n = int(input())
    j = 0
    k = -1

    while(n):
        k += 1
        if (j + 100 <= n):
            j += 100
        elif (j + 20 <= n):
            j += 20
        elif (j + 10 <= n):
            j += 10
        elif (j + 5 <= n):
            j += 5
        elif (j + 1 <= n):
            j += 1
        else: 
            print(k)
            return 0

if __name__ == '__main__':
    main()