
# 前序
def forward_order(cur):
    res = []
    stack = []
    while cur or stack:
        while cur:
            stack.append(cur)
            res.append(cur.val)
            cur = cur.left
        cur = stack.pop()
        cur = cur.right
    return res

# 中序
def inward_order(cur):
    res = []
    stack = []
    while cur or stack:
        while cur:
            stack.append(cur)
            cur = cur.left
        cur = stack.pop()
        res.append(cur.val)
        cur = cur.right
    return res


#后序遍历，非递归
def backward_order(cur):
    res,stack = [],[]
    pre = None
    while stack or cur:
        while cur:
            stack.append(cur)
            cur = cur.left
        cur = stack.pop()
        if not cur.right or cur.right == pre:
            res.append(cur.val)
            pre = cur
            cur = None
        else:
            stack.append(cur)
            cur = cur.right

    return res


def mergeSort(arr,l,r):
    if l==r: return
    mid = l+(r-l)//2
    mergeSort(arr, l, mid)
    mergeSort(arr,mid+1,r)
    merge(arr,l,r,mid)

def merge(arr,l,r,mid):
    helper = [0]*(r-l+1)
    p1,p2 = l,mid+1
    i = 0
    while p1<=mid and p2<=r:
        if arr[p1]<arr[p2]:
            helper[i] = arr[p1]
            p1+=1
        else:
            helper[i] = arr[p2]
            p2+=1
        i+=1
    if p2<=r:
        helper[i:] = arr[p2:r+1]
    else:
        helper[i:] = arr[p1:mid+1]
    arr[l:r+1] = helper

