class coin_calculator:
	def __init__(self, coins, price):
		self.coins = coins
		self.comparable_coins = len(self.coins)
		assert price <= 10000
		self.price = price

	"""
	Definition
		Convert the list to a string

	Parameters
	----------
	list : list
		The list to be converted

	Return
	------
	value : string
		The converted list
	"""
	def list_to_string(self, list):
		s = "["
		m = ", ".join(map(str, list))
		return s + m + "]"

	"""
	Definition
		Print the solutions
	
	"""
	def print_solutions(self):
		A = self.dynamicOptions()
		amount_of_ways = A[ self.comparable_coins-1 ][self.price]

		print("---------")
		print( "{:6} | {:1000}".format( "coins", "Matrix" ) )
		print( "--------")
		for i in range(self.comparable_coins):
			if A[i] == A[i-1]:
				break

			print( "{:6} | {:1000}".format(
				str(self.coins[i]),
				self.list_to_string(A[i])
				)
			)
		print("---------")
		print("Amount of ways: ", amount_of_ways)
		print("---------")

	"""
	Definition
		Print according to the Greedy algorithm

	Return
	------
	s : int
		The size of the node, including the children
	"""
	def printSolutionNumberGreedy(self):
		return self.getSolutionsNumber(self.comparable_coins, self.price)

	"""
	Definition
		Calculate according to the Greedy Algorithm
	
	Parameters
	----------
	comparable_coins : list
		The coins you can compare with
	price : int
		The price.

	Return
	------
	value : int
		Amount of ways to pay according to the Greedy Algorithm
	"""
	def getSolutionsNumberGreedy(self, comparable_coins, price):
		global coins

		if price < 0:
			return 0

		if price == 0:
			return 1

		if comparable_coins <= 0:
			return 0

		return self.getSolutionsNumberGreedy(comparable_coins - 1, price) + self.getSolutionsNumberGreedy(comparable_coins, price - self.coins[comparable_coins - 1])

	def dynamicOptions(self):
		A = [ ([0] * (self.price + 1) ) for _ in range(self.comparable_coins) ]

		for i in range(self.comparable_coins):
			A[i][0] = 1

		for j in range(self.price + 1):
			A[0][j] = 1

		for i in range(self.comparable_coins):
			for j in range(self.price + 1):
				if j >= self.coins[i]:
					A[i][j] = A[ i - 1 ][j] + A [i][ j - self.coins[i] ]
				elif j < self.coins[i]:
					A[i][j] = A[ i - 1 ][j]

		return A


coins = [1,2,5,10,20,50,100,200,500,1000,2000,5000,10000]
calc = coin_calculator(coins, 100)

calc.print_solutions()

