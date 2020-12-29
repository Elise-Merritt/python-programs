# Elise Merritt
# Unit 6 Assignment #1
#  Simple implementation of a singly linked list
#

class Node(object):

    def __init__(self, data=None, nextNode=None):
        self.data = data
        self.nextNode = nextNode

class linkedList(object):

    def __init__(self, head=None):
        self.head = head
        self.size = 0

    def insert(self, node):

        if not self.head:
            self.head = node
            self.size += 1
        else:
            # set new nodes pointer to old head
            node.nextNode = self.head
            # reset head to new node
            self.head = node
            self.size +=1

    def getSize(self):
        return self.size

    def printLL(self):
        mynode = self.head
        c = 0
        while mynode:
            c += 1
            print(mynode.data, c)
            mynode = mynode.nextNode

    #Function returns the value at the nth position in a linked list
    def getNum(self, n):
        curr_node=self.head
        #Traverse linked list until right node is reached
        for i in range(1,n):
            curr_node=curr_node.nextNode
        return curr_node.data

            

    

        

 
