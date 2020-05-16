class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, head):
        head = Node(head)
        self.head = head
        self.head.next = self.head

    #this function starts from the head and goes through the list until it finds the last element
    #the last element is the one that has his next value pointing to the head, because we have a circular list
    def insertInList(self, value):
        currNode = self.head
        while currNode.next is not self.head:
            currNode = currNode.next
        currNode.next = Node(value)
        currNode.next.next = self.head

    def printList(self):
        n = self.head
        while n.next is not self.head:
            print(n.value)
            n = n.next
        print(n.value)

    #I made this method because in some cases I need to know what is the previous node
    #One of this cases is when you remove a node
    def previousNode(self, value):
        node = self.head
        #first we check if the node is the head
        if value == node.value:
            while node.next != self.head:
                node = node.next
            return node

        # if the node is not the head, we just check for him
        while node.next != self.head:
            if node.next.value == value:
                return node
            node = node.next

    #I made this method because it may be usefull later
    def checkForElement(self, value):
        node = self.head
        while node.next != self.head:
            if node.value is value:
                return True
            node = node.next

        #the while goes until the last element but stops there so here I checked for the last element
        if node.value is value:
            return True

        return False



    def remove(self,value):
        n = self.head

        #First we check for the head
        #The method previousNode came in handy for this part
        if n.value == value:
            self.previousNode(n.value).next = n.next
            self.head = n.next

        else:
            check = 0
            #the while below is not checking for the last element so I made the check variable to check for the last element
            # ONLY if an element wasn't succesfully removed, because my remove method is removing only one element.
            #Without the check variable for the list 3,5,3,5 it would remove the first five then will go into the second if where it would remove
            #the last five also.
            while n.next is not self.head:
                if n.value is value:
                    self.previousNode(n.value).next = n.next
                    check = 1
                    break
                n = n.next
            if n.next is self.head and check is not 1:
                self.previousNode(n.value).next = self.head

    def listThirdElementFromTheGivenOne(self, value):
        if self.checkForElement(value):
            node = self.head
            while node.value != value:
                node = node.next
            return node.next.next.next.value



# Now going to the actual Josepheus problem:
#The first step is to create a linkedList

l = LinkedList(1)

#adding values into list
l.insertInList(2)
l.insertInList(3)
l.insertInList(4)
l.insertInList(5)
l.insertInList(6)
l.insertInList(7)
l.insertInList(8)
l.insertInList(9)
l.insertInList(10)

steps = int((input("The number of steps: ")))
count = 1
node = l.head
while node.next is not node:
    node = node.next
    count += 1
    if count is steps:
        count = 1
        l.remove(node.value)
        node = node.next
print("the last node is: ")
l.printList()