with open('sample.txt','r') as f:
    i=0
    while True:
            line =f.readline()
            if 'python' in line:
                print(f"its in third line{i+1}")
            if not line:
                break
            else:
                i+=1
            