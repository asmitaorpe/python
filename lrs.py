import sys
import time

def lrs_dp(user):
    length = len(user)

    arr = [[0]*(length+1)]*(length+1)
    for x in range(1,(length+1)):
        for y in range(1,(length+1)):
            if user[x-1] == user[y-1]and x!=y:
                arr[x][y] = (1+arr[x-1][y-1])
            else:
                arr[x][y] = max(arr[x][y-1],arr[x-1][y])
    print('length', arr[length][length])
    c = ""
    k = length
    l = length
    #print('ji')
    while k>0 and l>0:
        if arr[k][l] == arr[k-1][l-1]+1:
            c += user[k-1]
            k -= 1
            l -= 1
        elif arr[k][l] == arr[k-1][l]:
            k -= 1
        else:
            l -= 1

    print('end while')
    d=c[::-1]
    print('string',d[::])
    print('hi')
    return d
    print('ji')


if __name__ == '__main__':
    user=raw_input("enter")
    #user=sys.argv[1]
    lrs_dp(user)
    print(lrs_dp(user))
