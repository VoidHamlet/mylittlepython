"Re-implementation of Python's dict.... only better."

class Dict:

    def __init__(self):
        self.n = 8
        self.rows = [ [] for i in range(self.n) ]
        self.desks = [ [] for i in range(self.n) ]

    def __setitem__(self, key, value):
        "Implements d[key] = value"
        row_id = hash(key) % self.n
        row = self.rows[row_id]
        desk = self.desks[row_id]
        if key not in row:
            row.append(key)
            desk.append(value)
        else:
            position = row.index(key)
            desk[position] = value

    def __getitem__(self, key):
        "Implements d[key]"
        row_id = hash(key) % self.n
        row = self.rows[row_id]
        desk = self.desks[row_id]
        try:
            position = row.index(key)
        except ValueError:
            raise KeyError(key)
        value = desk[position]
        return value

    def __delitem__(self, key):
        "Implements del d[key]"
        row_id = hash(key) % self.n
        row = self.rows[row_id]
        desk = self.desks[row_id]
        try:
            position = row.index(key)
        except ValueError:
            raise KeyError(key)
        del row[position]
        del desk[position]

    def __iter__(self):
        for row in self.rows:
            for key in row:
                yield key

    def keys(self):
		# We already have an iterable!
        return list(self)

