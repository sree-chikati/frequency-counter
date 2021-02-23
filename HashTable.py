from LinkedList import LinkedList

class HashTable:

  def __init__(self, size):
    self.size = size
    self.arr = self.create_arr(size)


  # 1️⃣ TODO: Complete the create_arr method.

  # Each element of the hash table (arr) is a linked list.

  def create_arr(self, size):
    """ Creates an array (list) of a given size 
    and populates each of its elements with a LinkedList object """
    array = []
    
    for i in range(size): 
      new_ll = LinkedList()
      array.append(new_ll)
    
    return array




  # 2️⃣ TODO: Create your own hash function.

  # Hash functions are a function that turns each of these keys into an word_len value that we can use to decide where in our list each key:value pair should be stored. 

  def hash_func(self, key):

    # 1. Get the first char
    # 2. Calculate its distance from 'a'
    # 3. Mod so we are in range

    first_char = key[0].lower()
    dist_a = ord(first_char) - ord('a')
    index = dist_a % self.size

    return index


  # 3️⃣ TODO: Complete the insert method.

  # Should insert a key value pair into the hash table, where the key is the word and the value is a counter for the number of times the word appeared. When inserting a new word in the hash table, be sure to check if there is a Node with the same key in the table already.

  def insert(self, key, value):

    # 1. Find which index to insert key + value
    # 2. Go through ll and search key
    # 3. But, if same key exists... increase value by 1
    # 4. Create tuple according to find_update
    # 4. If the key is not found, then append

    hash_key = self.hash_func(key)
    new_ll = self.arr[hash_key].find_update(key)

    item = (key, value)
    
    if new_ll == -1:
      self.arr[hash_key].append(item)




  # 4️⃣ TODO: Complete the print_key_values method.

  # Traverse through the every Linked List in the table and print the key value pairs.

  # For example: 
  # a: 1
  # again: 1
  # and: 1
  # blooms: 1
  # erase: 2

  def print_key_values(self):
    for ll in self.arr: 
      ll.print_nodes()
    
    print('DONE')



