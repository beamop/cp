s = input()

lowerCount = sum(map(str.islower, s))
upperCount = sum(map(str.isupper, s))

if (lowerCount > upperCount or lowerCount >= upperCount):
    print(s.lower())
else: 
    print(s.upper())