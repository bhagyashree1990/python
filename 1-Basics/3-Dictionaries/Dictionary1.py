myDictionary = {"firstName":"John","lastName": "Doe","address":"Mumbai"}
keys = myDictionary.keys()
print(keys)
myDictionary["contactNumber"] = "91234567890"
print(keys)
del myDictionary['address']
print(keys)
