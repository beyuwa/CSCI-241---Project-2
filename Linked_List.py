class Linked_List:
    
    class __Node:
        
        def __init__(ego, val, index = None, next = None, prev = None):
            ego.val = val
            ego.next = next
            ego.prev = prev
            ego.index = index

    def __init__(ego):
        ego.header = ego.__sent()
        ego.tailer = ego.__sent()
        ego.header.next = ego.tailer
        ego.tailer.prev = ego.header
        ego.size = 0

    def __sent(ego):
        return ego.__Node(None)

    def test_index(ego, index):
        if index > ego.__len__() - 1: # out of bounds
            raise IndexError
    
        if index < 0: # negative
            raise IndexError

    def __len__(ego):
        if ego.header.next is ego.tailer is None: # if there is nothing, or a number was just added, but it doesn't count yet
            return 0
        return ego.size

    def append_element(ego, val):
        new = ego.__Node(val)

        ego.tailer.prev.next = new
        new.prev = ego.tailer.prev
        new.next = ego.tailer
        ego.tailer.prev = new

        new.index = ego.__len__() - 1 #special case, but since it is at the end, it's pretty neat
        ego.size += 1

    def find_at_index(ego, index): #will get the node at the index requested

        cur = ego.header.next # header node

        for _ in range(index):
            cur = cur.next

        return cur
    
    def increment_geq_index(ego, node, inc): # increments indexes after and including the specified node

        while node is not ego.tailer:
            node.index += inc # inc = \pm 1
            node = node.next

    def insert_element_at(ego, val, index): # add new with the provided index
        
        # blocks from psuedo-appending
        ego.test_index(index)

        base = ego.find_at_index(index)
        ego.increment_geq_index(base, 1)
        
        new = ego.__Node(val, index)

        new.prev = base.prev
        base.prev.next = new
        new.next = base
        base.prev = new

        ego.size += 1

    def remove_element_at(ego, index): # remove node at the given index

        ego.test_index(index)
        
        base = ego.find_at_index(index)
        copyval = base.val
        base.prev.next = base.next
        base.next.prev = base.prev

        ego.increment_geq_index(base, -1) # makes indexes including base -1, so if we remove base now all is ok

        base.index = None
        base.val = None
        base.next = None
        base.prev = None

        ego.size += -1

        return copyval

    def get_element_at(ego, index):
        ego.test_index(index)
        return (ego.find_at_index(index).val)

    def rotate_left(ego):

        if ego.__len__() == 0: # if there is an empty list
            return
        
        temp = ego.find_at_index(0).val
        ego.remove_element_at(0)
        ego.increment_geq_index(ego.header.next, -1)
        ego.append_element(temp)
        
    def __str__(ego):

        if ego.header.next is ego.tailer:
            return '[ ]'
        
        stri = '[ '
        cur = ego.header.next

        while cur.next is not ego.tailer:
            stri += (str(cur.val) + ', ')
            cur = cur.next

        stri += str(cur.val)

        stri += ' ]'
        
        return stri

    def __iter__(ego):
        ego.count = 0
        return ego

    def __next__(ego):
        ego.count += 1

        if ego.count <= ego.__len__(): # the "==" case iterates on the last element
            return (ego.find_at_index(ego.count - 1).val) # the index is the count minus 1
        
        raise StopIteration

    def __reversed__(ego):
        novel = Linked_List()
        base = ego.tailer.prev
        counter = 0
        
        while base is not ego.header:
            novel.append_element(base.val)
            base.index = counter
            base = base.prev
            counter += 1

        return novel

if __name__ == '__main__':

    # l = Linked_List()
    # l.append_element(6)
    # l.append_element(4)
    # l.append_element(8)
    # l.insert_element_at(3, 0)
    # print(l.remove_element_at(3))
    # print(l.__str__())
    # print(l.__len__())
    # print(l.__reversed__())

    # k = Linked_List()
    # [k.append_element(i) for i in range(10)]
    # print(k.__str__())
    # k.rotate_left()
    # print(k.__str__())
    # print(k.__reversed__())

    # m = Linked_List()
    # m.append_element(6)
    # m.rotate_left()
    # print(m.__str__())
    # print(m.__len__())
    # print(m.__reversed__())

    # s = Linked_List()
    # print(s.__str__())
    # s.rotate_left()
    # print(s.__len__())
    # print(s.__reversed__())

    # for i in l:
    #     print(i)

    # print(k.__str__())

    # reverse = k.__reversed__()
    # cur = reverse.header.next
    # while cur is not reverse.tailer:
    #     print(cur.val, cur.index)
    #     cur = cur.next

    # for val in reverse:
    #     print(val)

    # p = Linked_List()
    # p.append_element("Data")
    # p.append_element("Big")
    # print(p.__str__())
    # print(p.get_element_at(0))
    # for i in p:
    #     print(i)



    # intential error zone
    #s.insert_element_at(0, 0)
    #print(s.get_element_at(0))
    #print(s.remove_element_at(0))
    #l.insert_element_at(3, -1)
    
    pass

'''


Functions               Complexity      Comments

'__init__'              O(1)            given it is the initialisation class that only declares variables.
'__sent'                O(1)            a class made to define sentinenls
'text_index'            O(1)            merely tests whether or not the specific index is actually valid (if negative or outside the linked list bounds)
'__len__'               O(1)            just calls the size attribute of the Linked_Lists class
'append_element'        O(1)            the function (1) initialises a __node object (constant time) and (2) switches around prev & next attributes for the tailer and new add (also constant time)
'find_at_index'         O(n)            the worst case scenario is where the index is at the end of the list, so the function wlll iterate through every node. This means the function's complexity is linearly dependent of the size of the list.
'increment_geq_index'   O(n)            this function goes through the whole list and increments all indexes by a value "inc". This is function definitely has lienar complexity.
'insert_element_at'     O(n)            this function calls the previous two mentioned, so O(n) + O(n) = O(n) complexity. Initiliasing a node class and messing around with prev/next is done with constant time.
'remove_element_at'     O(n)            this function is the basically the same (calls the same methods) as 'insert_element_at', other than the fact it casts the node in question with None attributes.
'get_element_at'        O(n)            this function tailors 'find_at_index' to suit the project criteria and merely calls it. It necessarily inherits a linear complexity.
'rotate_left'           O(n)            this function calls 'find_at_index', 'remove_element_at', 'increment_geq_index' and 'append_element' individually. Since they all have linear complexity or less, 'rotate_left' will not exceed that time.
'__str__'               O(n)            reads off aliases under a single while loop while constructing a string. It is possible a join list implementation will reduce time complexity, but given I am psuedo-appending, it's probably ok.
'__iter__'              O(1)            just initialises a variable and returns the object... I assume that is done in constant time.
'__next__'              O(n)            either (1) calls 'find_at_index', linear time, or (2) raises an exception, constant time. Thus, the worse case scenario is always linear time.
'__reversed__'          O(n)            basically makes a new list and appends the original list's nodes in reverse. 'append_element' (constant) is called under a while loop (linear), so it this method has linear comeplexity.


'''