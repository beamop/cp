def main():
    n, m = map(int, input().split())

    for x in range(0, n):
        for y in range(0, m):
            if (x % 2) == 0:
                print("#", end="")
            else:
                print(".", end="")
        print("")


if __name__ == '__main__':
    main()
