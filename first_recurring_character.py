def main():
    s = str(input())
    arr = s.split()
    seen = []
    
    for x in arr:
        if (x in seen):
            print('duplicate is %s' %(x))
            exit(1)
        seen.append(x)
        

if __name__ == '__main__':
    main()
