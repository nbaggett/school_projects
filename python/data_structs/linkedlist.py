import copy
class LinkedList:
    
    # The __Node class is used internally by the LinkedList class. It is 
    # invisible from outside this class due to the two underscores
    # that precede the class name. Python mangles names so that they
    # are not recognizable outside the class when two underscores
    # precede a name but aren't followed by two underscores at the
    # end of the name (i.e. an operator name). 
    class __Node:
        def __init__(self,item,next=None):
            self.item = item
            self.next = next
            
        def getItem(self):
            return self.item
        
        def getNext(self):
            return self.next
        
        def setItem(self, item):
            self.item = item
            
        def setNext(self,next):
            self.next = next
        
        def __repr__(self):
            return self.item
            
    def __init__(self,contents=[]):
        # Here we keep a reference to the first node in the linked list
        # and the last item in the linked list. The both point to a 
        # dummy node to begin with. This dummy node will always be in
        # the first position in the list and will never contain an item. 
        # Its purpose is to eliminate special cases in the code below. 
        self.first = LinkedList.__Node(None,None)
        self.last = self.first
        self.numItems = 0

        for e in contents:
            self.append(e)
          
    def __getitem__(self,index):
        if index >= 0 and index < self.numItems:
            cursor = self.first.getNext()
            for i in range(index):
                cursor = cursor.getNext()
                
            return cursor.getItem()
        
        raise IndexError("LinkedList index out of range")
    
    def __setitem__(self,index,val):
        if index >= 0 and index < self.numItems:
            cursor = self.first.getNext()
            for i in range(index):
                cursor = cursor.getNext()
                
            cursor.setItem(val)
            return 
        
        raise IndexError("LinkedList assignment index out of range")
    
    def insert(self,index,item):
        cursor = self.first
        
        if index < self.numItems: 
            for i in range(index):
                cursor = cursor.getNext()
                
            node = LinkedList.__Node(item, cursor.getNext())
            cursor.setNext(node)
            self.numItems += 1
        else:
            self.append(item)
            
            
    def __add__(self,other):
        if type(self) != type(other):
            raise TypeError("Concatenate undefined for " + \
                str(type(self)) + " + " + str(type(other)))

        result = LinkedList()
        
        cursor = self.first.getNext()
        
        while cursor != None:
            result.append(cursor.getItem())
            cursor = cursor.getNext()
            
        cursor = other.first.getNext()
                    
        while cursor != None:
            result.append(cursor.getItem())
            cursor = cursor.getNext()
        
        result.numItems = self.numItems + other.numItems
        return result
    
    
    def __contains__(self,item):
        # This is left as an exercise for the reader.
        cursor = self.first
        for i in range(len(self)):
            if cursor.getItem() == item:
                return True
            cursor = cursor.getNext()
        return False
        #pass
 
    def __delitem__(self,index):
        # This is left as an exercise for the reader. 
        cursor = self.first
        if index == 1:
            cursor = self.first.getNext()
        else:
            for i in range(index):
                cursor = cursor.getNext()
        deletion = cursor.getNext()
        afterDeletion = deletion.getNext()
        cursor.setNext(afterDeletion)
        #pass 
            
    def __eq__(self,other):
        if type(other) != type(self):
            return False
        
        if self.numItems != other.numItems:
            return False
        
        cursor1 = self.first.getNext()
        cursor2 = other.first.getNext()
        while cursor1 != None:
            if cursor1.getItem() != cursor2.getItem():
                return False
            cursor1 = cursor1.getNext()
            cursor2 = cursor2.getNext()
            
        return True
    
    def __iter__(self):
        # This is left as an exercise for the reader.
        current = self.first
        
        while current is not None:
            yield current
            current = current.next
        #pass
            
    def __len__(self):
        # This is left as an exercise for the reader.
        cursor = self.first
        
        len  = 0
        while cursor.getNext() != None:
            len += 1
            cursor = cursor.getNext()
        
        return len
        
        #pass

    def append(self,item):
        node = LinkedList.__Node(item)
        self.last.setNext(node)
        self.last = node
        self.numItems += 1
        
    def reverse(self):
        newlist = LinkedList()
        dex = len(self)-1
        while dex >= 0:
            if self[dex] is not None:
                newlist.append(self[dex])
            dex -= 1
        return newlist

        
    def __str__(self):
        # This is left as an exercise for the reader.
        cursor = self.first.next
        result = ''
        if cursor != None:
            result += str(cursor.getItem())
            cursor = cursor.next
            while cursor:
                result += ', ' + str(cursor.getItem())
                cursor = cursor.next
        return result
        
        #pass
    
    def __repr__(self):
        # This is left as an exercise for the reader.
        cursor = self.first.getNext()
        while cursor is not None:
            yield cursor.getItem()
            cursor = cursor.next

        #pass              
                
def main():
    lst = LinkedList()
    
    for i in range(100):
        lst.append(i)
    
    lst2 = copy.deepcopy(lst)
    
    
    if lst == lst2:
        print("Test 1 Equality Passed")
    else:
        print("Test 1 Equality Failed")
    
    lst3 = lst + lst2
    
    if len(lst3) == len(lst) + len(lst2):
        print("Test 2 Len Passed")
    else:
        print("Test 2 Len Failed")
        
    
    if 1 in lst3:
        print("Test 3 Membership Passed")
    else:
        print("Test 3 Membership Failed")        
    
    if 2 in lst3:
        print("Test 4 Membership Passed")
    else:
        print("Test 4 Membership Failed")        
    
    del lst[1]
    
    if 1 in lst:
        print("Test 5 Delete Failed")
    else:
        print("Test 5 Delete Passed")        
    
    if len(lst) == 99:
        print("Test 6 Len Delete Passed")
    else:
        print("Test 6 Len Delete Failed")        
        
    if lst == lst2:
        print("Test 7 Equality Failed")
    else:
        print("Test 7 Equality Passed")      
        
    del lst2[2]
    
    if lst == lst2:
        print("Test 8 Delete Failed")
    else:
        print("Test 8 Delete Passed")  
        
    
    lst4 = copy.deepcopy(lst)
    lst.insert(0,100)
    lst4 = LinkedList([100]) + lst4

    
    if lst == lst4:
        print("Test 9 Insert Passed")
    else:
        print("Test 9 Insert Failed")
    
        
    lst.insert(1000,333)
    lst4.append(333)

    if lst == lst4:
        print("Test 10 Append Passed")
    else:
        print("Test 10 Append Failed")  
        
if __name__ == "__main__":
    main()
                
            
            
        
            