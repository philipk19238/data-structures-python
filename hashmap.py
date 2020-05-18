class HashMap:

	def __init__(self, array_size):
		self.array_size = array_size
		self.array = [None] * self.array_size

	def hash(self, key, num_collisions=0):
		key_bytes = key.encode()
		hash_code = sum(key_bytes)

		#shifting hash
		return hash_code + num_collisions

	def compress(self, hashcode):
		return hashcode % self.array_size

	def assign(self, key, value):
		index = self.compress(self.hash(key))

		curr_value = self.array[index]
		if not curr_value:
			self.array[index] = [key, value]

		#overwriting if key is the same
		elif curr_value[0] == key:
			self.array[index] == [key, value]

		#rehashing if hash collision occured
		else:
			number_collisions = 1

			while current_array_value[0] != key:
				new_hash = self.hash(key, number_collisions)
				new_index = self.compress(new_hash)

				current_array_value = self.array[new_index]
				
				if not current_array_value:
					self.array[new_index] = [key, value]
				#overwriting if keys are the same
				if current_array_value[0] == key:
					self.array[new_index] = [key, value]

				#incrementing if array index data has different key
				number_collisions += 1


	def retrieve(self, key):
		index = self.compress(self.hash(key))

		return_value = self.array[index]

		#checking for hash collisions
		if return_value:
			if return_value[0] == key:
				return return_value[1]

			else:
				#incrementing search if hash collision occurs
				retrieval_collisions = 1
				while return_value[0] != key:
					new_array_index = self.compress(self.hash(key, retrieval_collisions))

					return_value = self.array[new_array_index]

					if not return_value:
						return None

					if return_value[0] == key:
						return return_value[1]

					retrieval_collisions += 1

		return None

if __name__ == "__main__":
	hash_map = HashMap(20)
	hash_map.assign('color', 'red')
	print(hash_map.retrieve('color'))