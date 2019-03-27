
if __name__ == '__main__':
    for n in range(10):
        array = [0*100 for j in range(100)]
        number = input().strip()
        number = int(number)

        for i in range(100):
            array[i] = input().strip().split()

        for i in range(100):
            if array[0][i] == "0":
                continue
            else:
                X = 0
                Y = i
                flag = 2                    # 0 : move to left / 1 : move to right / 2 : move to bottom

                while X < 100:
                    if flag == 0:          # move to left
                        if Y == 0:
                            X += 1
                            flag = 2
                            continue
                        else:
                            if array[X][Y-1] == "1":
                                Y -= 1
                                continue
                            else:
                                X += 1
                                flag = 2

                    elif flag == 1:     # move to right
                        if Y == 99:
                            X += 1
                            flag = 2
                            continue
                        else:
                            if array[X][Y+1] == "1":
                                Y += 1
                                continue
                            else:
                                X += 1
                                flag = 2

                    else:                           #move to bottom
                        if Y == 99:
                            if array[X][Y-1] == "1":                #move left
                                Y -= 1
                                flag = 0
                                continue
                        elif Y == 0:
                            if array[X][Y+1] == "1":                #move right
                                Y += 1
                                flag = 1
                                continue
                        else:
                            if array[X][Y-1] == "1":
                                Y -= 1
                                flag = 0
                                continue
                            elif array[X][Y+1] == "1":
                                Y += 1
                                flag = 1
                                continue
                        X += 1

                if array[X-1][Y] == "2":
                    print("#"+str(number)+" "+str(i))
                    break;
