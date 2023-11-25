class Codec:

    def serialize(self, root):
        if root==None:
            return ""
        q=deque([root])
        s=""
        while q:
            node=q.popleft()
            if node:
                s+=str(node.val)+" "
                q.append(node.left)
                q.append(node.right)
            else:
                s+="# "
        return s       

    def deserialize(self, data):
        n=len(data)
        if n==0:
            return None
        data=data.split(" ")
        t=root=TreeNode(data[0])
        data.pop()
        q=deque([root])
        i=1
        while q:
            node=q.popleft()
            s=data[i]
            if s!='#':
                node.left=TreeNode(s)
                q.append(node.left)
            else:
                node.left=None
            i+=1
            s=data[i]
            if s!='#':
                node.right=TreeNode(s)
                q.append(node.right)
            else:
                node.right=None  
            i+=1
        return t