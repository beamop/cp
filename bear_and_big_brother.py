def main():
    lw, bw = map(int, input().split())
    y = 0

    while True:
        y += 1
        lw *= 3
        bw *= 2
        if (lw > bw):
            print(y)
            return 0

if __name__ == '__main__':
    main()