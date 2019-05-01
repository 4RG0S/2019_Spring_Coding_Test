# solution
if __name__ == '__main__':
   # f = open("input.txt", "r")
     
    for test_case in range(1, 11):
        n = input().strip()
        flag = 0
        for i in range(int(n)):
            tmp = input().strip().split(' ')
 
            if flag != 1:
                if len(tmp) == 4:
                    if tmp[1].isnumeric() is True:
                        flag = 1
                    if tmp[2].isnumeric() is False and tmp[3].isnumeric() is False:
                        flag = 1
 
                elif len(tmp) == 3:
                    if tmp[1].isnumeric() is True:
                        flag = 1
                    if tmp[2].isnumeric() is False:
                        flag = 1
 
                elif len(tmp) == 2:
                    if tmp[1].isnumeric() is False:
                        flag = 1
 
        if flag == 1:
            print("#"+str(test_case)+" 0")
        else:
            print("#"+str(test_case)+" 1")
