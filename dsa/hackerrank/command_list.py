if __name__=='__main__':
    N = int(input())
    arr=[]

    for _ in range(N):
        command = input().split()
        cmd=command[0]
        args=command[1:]

        if cmd== 'insert':
            i,e =map(int,args)
            arr.insert(i,e)

        elif cmd =='print':
            e= int(args[0])
            arr.remove(e)
        
        elif cmd =='append':
            e =int(args[0])
            add.remove(e)

        elif cmd == 'sort':
            arr.sort()
            
        elif cmd == 'pop':
            arr.pop()
        
        elif cmd =='reverse':
            arr.reverse()
