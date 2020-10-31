class HashTableEntry:
    """
    Linked List hash table key/value pair
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8



class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity):
        # Your code here
        self.capacity = max(capacity, MIN_CAPACITY)
        self.storage = [None] * capacity


    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        # Your code here
        return len(self.storage)


    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        # Your code here
        pass
        # total load
        load = 0

        # loopover all node
        
        for node in self.storage:

            currNode = node

            while node is not None:
                
                pass
            





    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """

        # Your code here
    #     algorithm fnv-1 is
    #       hash := FNV_offset_basis

    #     for each byte_of_data to be hashed do
    #       hash := hash × FNV_prime
    #       hash := hash XOR byte_of_data
    #     return hash 

        offset_basis = 14695981039346656037
        FNV_prime = 1099511628211

        hashed = offset_basis

        bytes_to_code = key.encode()

        for byte in bytes_to_code:
            hashed = hashed * FNV_prime

            hashed = hashed ^ byte
            
        return hashed

    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        # Your code here
        long_hash = 5381

        for c in key:
            long_hash = (long_hash * 33) + ord(c)
            # long_hash = ((long_hash << 5) + c)
            

        return long_hash


    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        #return self.fnv1(key) % self.capacity
        return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        # Your code here
        # self.storage[self.hash_index(key)] = value

        # create new node
        newNode = HashTableEntry(key,value)

        # get index for storing
        index = self.hash_index(key)

        # get current item
        currNode = self.storage[index]

        # check if storage has node in it
        if isinstance(currNode, HashTableEntry):

            
            # check if currNode.key is same
            if currNode.key == key:
                currNode.value = value


            # if loop until it reaches the end and add node
            while currNode.next is not None:
                
                # update the currNode to the next
                currNode = currNode.next
                
                # if key is the same update value
                if currNode.key == key:
                    currNode.value = value
                    return

            # save the new node to the linked list
            currNode.next = newNode
        # else add the node
        else:
            self.storage[index] = newNode


    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """

        # Your code here
        # self.storage[self.hash_index(key)] = None

        # get hashed index
        index = self.hash_index(key)
        
        # get the node on that index
        currNode = self.storage[index]

        # if the currNode.key matches updated the storage since its the first one
        if currNode.key == key:
            self.storage[index] = currNode.next

        else:
            # while the currNode is not none
            while currNode is not None:
                # update to next node
                prevNode = currNode

                currNode = currNode.next

                # if keys match
                if currNode.key == key:
                    # if there is a next
                    prevNode.next = currNode.next

                    return



    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        # Your code here
        # return self.storage[self.hash_index(key)]
        # get index for hashed key
        index = self.hash_index(key)
        
        # set the current node
        currNode = self.storage[index]
            
        # loop over currNode till you find key or reach the end
        while currNode is not None:

            # if key matches
            if currNode.key == key:
                # return the value
                return currNode.value
            else:
            # else update the currNode to the next node
                currNode = currNode.next   

        return currNode


    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        # Your code here
        pass



if __name__ == "__main__":
    ht = HashTable(8)

    ht.put("line_1", "'Twas brillig, and the slithy toves")
    ht.put("line_2", "Did gyre and gimble in the wabe:")
    ht.put("line_3", "All mimsy were the borogoves,")
    ht.put("line_4", "And the mome raths outgrabe.")
    ht.put("line_5", '"Beware the Jabberwock, my son!')
    ht.put("line_6", "The jaws that bite, the claws that catch!")
    ht.put("line_7", "Beware the Jubjub bird, and shun")
    ht.put("line_8", 'The frumious Bandersnatch!"')
    ht.put("line_9", "He took his vorpal sword in hand;")
    ht.put("line_10", "Long time the manxome foe he sought--")
    ht.put("line_11", "So rested he by the Tumtum tree")
    ht.put("line_12", "And stood awhile in thought.")

    print("")

    # Test storing beyond capacity
    # for i in range(1, 13):
    #     print(ht.get(f"line_{i}"))

    # Test resizing
    old_capacity = ht.get_num_slots()
    # ht.resize(ht.capacity * 2)
    new_capacity = ht.get_num_slots()

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    # for i in range(1, 13):
    #     print(ht.get(f"line_{i}"))

    ht.get_load_factor()
    print("")
