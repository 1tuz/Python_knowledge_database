hash_table = {}

# Insert key-value pairs into the hash table
hash_table['key1'] = 'value1'
hash_table['key2'] = 'value2'
hash_table['key3'] = 'value3'

# Access values in the hash table using keys
print(hash_table['key1']) # Output: 'value1'
print(hash_table['key2']) # Output: 'value2'

# Check if a key is in the hash table
if 'key1' in hash_table:
    print("Key exists in hash table")
else:
    print("Key does not exist in hash table")

# Delete a key-value pair from the hash table
del hash_table['key1']

# Check if the key-value pair was deleted
if 'key1' in hash_table:
    print("Key still exists in hash table")
else:
    print("Key does not exist in hash table")
