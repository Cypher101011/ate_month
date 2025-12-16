def findMajority(arr):
    ele_1 = -1
    ele_2 = -1
    count_1,count_2 = 0
    # count_2 = 0
    majority = len(arr) // 3

    # 1. Find candidates
    for element in arr:

        if element == ele_1:
            count_1 += 1
        elif element == ele_2:
            count_2 += 1
        elif count_1 == 0:
            ele_1 = element
            count_1 = 1
        elif count_2 == 0:
            ele_2 = element
            count_2 = 1
        else:
            count_1 -= 1
            count_2 -= 1

    # 2. Count occurrences
    count_1 = 0
    count_2 = 0

    for ele in arr:
        if ele == ele_1:
            count_1 += 1
        elif ele == ele_2:
            count_2 += 1

    # 3. Prepare result
    result = []
    if count_1 > majority:
        result.append(ele_1)
    if count_2 > majority:
        result.append(ele_2)

    print(result)
