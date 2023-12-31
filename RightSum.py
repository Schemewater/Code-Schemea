#  File: RightSum.py

#  Description: Get the right sum of the BST

#  Student Name:

#  Student UT EID:

#  Course Name: CS 313E

#  Unique Number: 86610

import sys

class Queue(object):
    def __init__(self):
        self.queue = []

    # add an item to the end of the queue
    def enqueue(self, item):
        self.queue.append(item)

    # remove an item from the beginning of the queue
    def dequeue(self):
        return (self.queue.pop(0))

    # check if the queue is empty
    def is_empty(self):
        return (len(self.queue) == 0)

    # return the size of the queue
    def size(self):
        return (len(self.queue))

class Node (object):
  def __init__ (self, data):
    self.data = data
    self.lchild = None
    self.rchild = None

class Tree (object):
  def __init__ (self):
    self.root = None

  # insert data into the tree
  def insert (self, data):
    new_node = Node (data)

    if (self.root == None):
      self.root = new_node
      return
    else:
      current = self.root
      parent = self.root
      while (current != None):
        parent = current
        if (data < current.data):
          current = current.lchild
        else:
          current = current.rchild

      # found location now insert node
      if (data < parent.data):
        parent.lchild = new_node
      else:
        parent.rchild = new_node

  # ***There is no reason to change anything above this line***

  # Returns an integer of the right sum of the BST
  def get_right_sum(self):
      make_queue = [[self.root,0]]
      final_list = []
      while make_queue:
          nodes = make_queue.pop(0)
          final_list.append(nodes)
          #final_list.reverse()
          if nodes[0].lchild:
              make_queue.append([nodes[0].lchild , nodes[1] + 1])
          #if nodes[0].rchild:
              #make_queue.append([nodes[0].rchild , nodes[1] + 1])
          
# =============================================================================
         
      sum = 0
      while final_list:
          i = -1
          sum += final_list[-1][0].data
          while (len(final_list)>=-i) and (final_list[i][1]==final_list[-1][1]):
              i-=1
          final_list = final_list[:i+1]
           
           
           
 
 
      return sum
# =============================================================================


# ***There is no reason to change anything below this line***

def main():
    # Create tree
    line = sys.stdin.readline()
    line = line.strip()
    line = line.split()
    tree_input = list (map (int, line))    # converts elements into ints

    tree = Tree()
    for i in tree_input:
      tree.insert(i)

    print(tree.get_right_sum())

if __name__ == "__main__":
  main()
