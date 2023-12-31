class Link():
  ''' This class represents a link between data items only'''
  def __init__ (self, data, next = None):
    self.data = data
    self.next = next

  def __str__(self):
    return str(self.data) + " --> " + str(self.next)



class LinkedList():
  ''' This class implements the operations of a simple linked list'''
  def __init__ (self):
    self.first = None

  def insertFirst (self, data):
    '''inset data at begining of a linked list'''
    newLink = Link(data)
    newLink.next = self.first
    self.first = newLink

  def insertLast (self, data):
    ''' Inset the data at the end of a linked list '''
    newLink = Link(data)
    current = self.first

    if (current == None):
      self.first = newLink
      return
    # find the last and insert it there. 
    while (current.next != None):
      current = current.next

    current.next = newLink

  def findLink(self, data):
    ''' find to which data is the link of a given data inside this linked list'''
    current = self.first
    if (current == None):
      return None

    # searcg and find the position of the given data, the get the link if. 
    while (current.data != data):
      if (current.next == None):
        return None
      else:
        current = current.next

    return current

  def deleteLink(self, data):
    ''' Removes the data from the list if exist and fix the link problems.'''

    current = self.first
    previous = self.first

    if (current == None):
      return None

    while (current.data != data):
      if (current.next == None):
        return None
      else:
        previous = current
    
      current = current.next

    if (current == self.first):
      self.first = self.first.next
    else:
      previous.next = current.next

    return current

  def __str__(self):
    return str(self.first)



class Stack():
    #initializing a linked list and a pointer/link
    def __init__(self):
        self.lst = LinkedList()
        self.link = None
        #using the insert first method to push the data into the list and inititialize the position of the link
    def push(self, data):
        self.lst.insertFirst(data)
        current = self.lst.findLink(data)
        if current.next == None:
            self.link = current
            
      #popping a value from the list/ last value      
    def pop(self):
        current = self.link.next
        if current.next == None:
            return None
        answer = self.lst.deleteLink(self.link)
        self.link = current
        return answer.data
        
    def peak(self):
        return self.list.findLink(self.link).data

