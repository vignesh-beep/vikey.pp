nums1 = int(input())
if nums1 > 1:
    for i in range(2, nums1):
        if (nums1 % i) == 0:
            print("yes")
            break
    else:
        print("no")
