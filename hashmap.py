class HashMap:

	def __init__(self, array_size):
		self.array_size = array_size
		self.array = [None] * self.array_size

	def hash(self, key):
		key_bytes = key.encode()
		hash_code = sum(key_bytes)
		return hash_code

	def compress(self, hashcode):
		return hashcode % self.array_size

	def assign(self, key, value):
		index = self.compress(self.hash(key))
		self.array[index] = value

	def retrieve(self, key):
		index = self.compress(self.hash(key))
		return self.array[index]

if __name__ == "__main__":
	hash_map = HashMap(20)
	hash_map.assign('color', 'red')
	print(hash_map.retrieve('color'))