if __name__== '__main__':
    n =int(input())

    arr= list(map(int,input().split()))
    sets=list(set(arr))#set cant be indexed so we have to convert it into list
    print(sets[-2])