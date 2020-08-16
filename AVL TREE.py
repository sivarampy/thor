import time
st = time.time()

class node:
    def __init__(self,data):
        self.data = data
        self.height = 1
        self.left = None
        self.right = None
class tree:
    def __init__(self):
        self.root = None
        
    def getheight(self,node):
        if not node:
            return 0
        return node.height

    def getdiff(self,node):
        if not node:
            return 0
        return self.getheight(node.left) - self.getheight(node.right)

    def rightrotate(self,z):
        y = z.left
        n2 = y.right

        # rotation
        y.right = z
        z.left = n2

        # update heights
        z.height = 1 + max(self.getheight(z.left),self.getheight(z.right))
        y.height = 1 + max(self.getheight(y.left),self.getheight(y.right))

        return y

    def leftrotate(self,z):
        y = z.right
        n2 = y.left

        y.left = z
        z.right = n2

        z.height = 1 + max(self.getheight(z.left),self.getheight(z.right))
        y.height = 1 + max(self.getheight(y.left),self.getheight(y.right))

        return y
    
    def additem(self,data):
        def add(cur_node,data):
            # step 1 - normal bts insertion
            if cur_node == None:
                return node(data)
            if data < cur_node.data:
                cur_node.left = add(cur_node.left,data)
            else:
                cur_node.right = add(cur_node.right,data)

            # step 2 - update the height of the ancestor node
            cur_node.height = 1 + max(self.getheight(cur_node.left),self.getheight(cur_node.right))

            # step 3 - get the difference
            diff = self.getdiff(cur_node)
            # step 4 - if its not balanced try one of the cases
            ## case 1 - left left
            if diff > 1 and data < cur_node.left.data:
                return self.rightrotate(cur_node)
            ## case 2 - left right
            if diff > 1 and data > cur_node.left.data:
                cur_node.left = self.leftrotate(cur_node.left)
                return self.rightrotate(cur_node)
            ## case 3 - right right
            if diff < -1 and data > cur_node.right.data:
                return self.leftrotate(cur_node)
            ## case 4 - right left
            if diff < -1 and data < cur_node.right.data:
                cur_node.right = self.rightrotate(cur_node.right)
                return self.leftrotate(cur_node)

            return cur_node
        
        self.root = add(self.root,data)

    def getsuccessor(self,node):
        cur_node = node.right
        while cur_node:
            if cur_node.left == None:
                break
            cur_node = cur_node.left
        return cur_node

    def deleteitem(self,data):
        def delete(cur_node,data):
            if cur_node == None:
                return cur_node
            elif cur_node.data < data:
                cur_node.right = delete(cur_node.right,data)
            elif cur_node.data > data:
                cur_node.left = delete(cur_node.left,data)
            else:
                if cur_node.left == None:
                    temp = cur_node.right
                    cur_node = None
                    return temp
                if cur_node.right == None:
                    temp = cur_node.left
                    cur_node = None
                    return temp
                temp = self.getsuccessor(cur_node)
                cur_node.data = temp.data
                cur_node.right = delete(cur_node.right,temp.data)

            cur_node.height = 1 + max(self.getheight(cur_node.left),self.getheight(cur_node.right))

            diff = self.getdiff(cur_node)

            if diff > 1 and self.getdiff(cur_node.left) >= 0:
                return self.rightrotate(cur_node)
            if diff > 1 and self.getdiff(cur_node.left) < 0:
                cur_node.left = self.leftrotate(cur_node.left)
                return self.rightrotate(cur_node)
            if diff < -1 and self.getdiff(cur_node.right) <= 0:
                return self.leftrotate(cur_node)
            if diff < -1 and self.getdiff(cur_node.right) > 0:
                cur_node.right = self.rightrotate(cur_node.right)
                return self.leftrotate(cur_node)
            
            return cur_node
        
        self.root = delete(self.root,data)

    def inorder(self):
        def pre(cur_node):       
            if cur_node.left:
                pre(cur_node.left)
            print(cur_node.data,end=' ')
            if cur_node.right:
                pre(cur_node.right)
        if not self.root:
            return None
        else:
            pre(self.root)

t = tree()


for i in range(20):
    t.additem(i)
t.deleteitem(15)    
t.inorder()
print(time.time()-st)
