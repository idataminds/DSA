class HashTable:
    def __init__(self, size):
        self.size = size  # Initialize the size of the hash table
        self.table = [None] * size  # Create a table of the given size, initialized with None

    def _hash(self, key):
        """Compute the hash for a given key."""
        return hash(key) % self.size  # Compute the index using the hash of the key and the size of the table

    def insert(self, key, value):
        """Insert a key-value pair into the hash table."""
        index = self._hash(key)  # Calculate the index for the key
        self.table[index] = value  # Store the value at the computed index

    def search(self, key):
        """Search for a value by key."""
        index = self._hash(key)  # Calculate the index for the key
        return self.table[index]  # Return the value stored at the index

