def checkMagazine(magazine, note):
    dict = {}
    result = 'Yes'
    for word in magazine:
        if word in dict:
            dict[word] += 1
        else:
            dict[word] = 1

    for word in note:
        if word not in dict:
            result = 'No'
            break
        else:
            dict[word] -= 1
            if dict[word] < 0:
                result = 'No'
                break

    print(result)

def main():
    magazine = ['a', 'sadf', 'a']
    note = ['sadf','sadf']
    checkMagazine(magazine, note)

if __name__=='__main__':
    main()