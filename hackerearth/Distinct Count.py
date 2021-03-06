class TreeNode:
    def __init__(self, data):
        self.data = data
        self.count = 0
        self.left = None
        self.right = None

for _ in range(int(input())):
    [N, X] = [int(s) for s in input().split() if s.isdigit()]
    arr = [int(s) for s in input().split() if s.isdigit()]

    count = 1
    root = TreeNode(arr[0])
    for i in range(1, len(arr)):
        currentNode = root
        previousNode = None

        while currentNode is not None:
            previousNode = currentNode
            if currentNode.data == arr[i]:
                currentNode.count += 1
                break
            elif currentNode.data > arr[i]:
                currentNode = currentNode.left
            elif currentNode.data < arr[i]:
                currentNode = currentNode.right

        if currentNode is None:
            count += 1
            if previousNode.data > arr[i]:
                previousNode.left = TreeNode(arr[i])
            else:
                previousNode.right = TreeNode(arr[i])
    
    if count == X:
        print("Good")
    elif count > X:
        print("Average")
    else: 
        print("Bad")