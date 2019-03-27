
if __name__ == '__main__':
    sum = 0             # 전망 좋은 아파트 세대 수

    for i in range (10) :
        number = input().strip()                # 테스트 케이스 길이
        tmp = input().strip()

        building = tmp.split()                  # 빌딩 split

        for j in range (len(building)) :            #숫자로
            building[j] = int(building[j])

        for k in range(len(building)) :
            if building[k] == 0:
                continue
            else :
                max_prev = max(building[k-2], building[k-1])
                max_next = max(building[k+1], building[k+2])

                Max = int(max(max_prev, max_next))                  #-2 ~ +2 사이 내 가장 큰 빌딩

                if building[k] - Max > 0 :
                    sum += building[k] - Max
                    #print(building[k], building[k]-Max)

        print("#"+ str(i+1) + " " + str(sum))
        sum = 0

def max (a, b) :
    if a > b :
        return a

    return b
