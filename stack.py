class Stack (object):

  def __init__ (self):
    self.stack = []

  # add an item to the top of the stack
  def push (self, item):
    self.stack.append(item)

  # remove an item from the top of the stack
  def pop(self):
    if(not self.isEmpty()):
      return self.stack.pop()
    else:
      return None

  # check what item is on top of the stack without removing it
  def peek(self):
    return self.stack[len(self.stack) - 1]

  # check if a stack is empty
  def isEmpty (self):
    return (len(self.stack) == 0)

  # return the number of elements in the stack
  def size(self):
    return (len(self.stack))

  # a string representation of this stack. 
  def __str__(self):
    return str(self.stack)


# # a different implementation of the Stack class
#class Stack (object):
   #def __init__ (self):
     
  #   self.stack =[]

 #  def push (self, item):
#     self.stack.insert(0, item )

#   def pop(self):
#     return self.stack.pop(0)

#   def peek (self):
#     return self.stack[0]

#   def isEmpty (self):
#     return (len(self.stack) == 0)

#   def size (self):
#     return (len(self.stack))


class Queue():
    # 
    def __init__(self):
        self.stack1 = Stack()
        self.stack2 = Stack()
        
        
    def enqueue(self,data):
        return self.stack1.push(data)
        
        
    def dequeue(self):
        while (self.stack1.isEmpty() == False):
            self.stack2.push(self.stack1.pop())
            
        new = self.stack2.pop()   
        while (self.stack2.isEmpty()==False):
            self.stack1.push(self.stack2.pop())
        return new
        def __str__(self):
            return str(self.stack1)
            
        
   
        


###############################
#                             #
#   Example run of a stack    #
#                             #
###############################

my_queue = Queue()
my_queue.enqueue(1)
print(my_queue)
my_queue.enqueue(2)
my_queue.enqueue(3)
my_queue.enqueue(4)
print(my_queue)
#print("scheme",my_queue.dequeue())

