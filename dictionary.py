# Re-implementation of Python's dict... only better. Honest.

class Dict:

	def __init__(self):
	# We need the below guys to point to two different places in memory.
		self.n = 8
		self.rows = [ [] for i in range(self.n) ]
		self.desks = [ [] for i in range(self.n) ]
		
	def __setitem__(self, key, value):
		"Implements d[key] = value"
		# Dunder methods don't really need a doc string but let's leave it.
		row_id = hash(key) % self.n
		row = self.rows[row_id]
		desk = self.desks[row_id]
		row.append(key)
		desk.append(value)
	
	def __getitem__(self, key):
		"Implements d[key]"
		row_id = hash(key) % self.n
		row = self.rows[row_id]
		desk = self.desks[row_id]
		position = row.index(key)
		value = desk[position]
		return value
		