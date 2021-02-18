# 二分查找的一些基本题template

# 在从小到大的数组里找数字，任意位置

def findNumbers(arrayIn,target):
    l,r = 0, len(arrayIn)-1
    while l<=r:
        mid = (l+r) >> 1
        if arrayIn[mid] == target:
            return mid
        elif arrayIn[mid] < target:
            l = mid + 1
        else:
            r = mid - 1
    return -1

# 还是找数字，但是输出最左的值
def findNumLeft(arrayIn,target):
    l,r = 0, len(arrayIn)-1
    while l<=r:
        mid = (l+r)>>1
        if arrayIn[mid]==target:
            r = mid - 1
        elif arrayIn[mid] < target:
            l = mid + 1
        else:
            r = mid - 1
    if l>=len(arrayIn) or arrayIn[l]!=target: return -1
    return l

def findNumRotate(arrayIn,target):
    l,r = 0, len(arrayIn)-1
    while l<=r:
        mid = l + (r - l) // 2
        if arrayIn[mid] == arrayIn[l]:
            if arrayIn[l] != target:
                l +=1
            else:
                r = mid -1
        elif arrayIn[mid] > arrayIn[l]: # order [l,mid]
            if arrayIn[l] <= target <= arrayIn[mid]:
                r = mid -1
            else:
                l = mid +1
        elif arrayIn[mid] < arrayIn[l]: # order [mid,r]
            if arrayIn[mid] >= target or arrayIn[l] <= target:
                r = mid -1
            else:
                l = mid + 1
    if l>=len(arrayIn) or arrayIn[l]!=target: return -1
    return l


if __name__ == '__main__':
    # print(findNumbers([1,3,4,6,7,8,10,13,14],4))
    print(findNumRotate([4,4,4,6,1,1,3,3,4],4))