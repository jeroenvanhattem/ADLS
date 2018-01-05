import csv
import sys

class method1:
	def writeToFile(self, dict):
		with open("opdracht_4.csv", "w") as csvfile:
			file = csv.writer(csvfile, sys.stdout, delimiter=',', lineterminator='\n')
			for key, value in dict.items():
				file.writerow( (key, value) )
		csvfile.close()

	def countWords(self):
		words_dict = {}
		with open("opdracht_4.txt", "r") as file:
			lines = file.read().splitlines()
			for line in lines:
				if not line == "":
					words = line.split()
					for word in words:
						if word in words_dict:
							words_dict[word] = words_dict.get(word) + 1
						else:
							words_dict.update({ word: 1 })
			file.close()
		self.writeToFile(words_dict)

class TrieNode:

	def __init__(self):
		self.w = None
		self.d = {}
		self.n = {}

	def insert(self, woord):
		self.d[woord] = TrieNode()

class Trie:
	def __init__(self):
		self.root = TrieNode()

	def insert(self, woord):
		current = self.root

		if self.contains(word):
			if woord in current.n:
				current.n[woord] = (current.n.get(woord) + 1)
			else:
				current.n.update({woord: 2})
			return

		for i in range(len(woord)):
			if woord[i] in current.d:
				current = current.d[woord[i]]
			else:
				# woord is hier volledig
				while i < len(woord):
					current.insert(woord[i])
					current = current.d[woord[i]]
					i += 1
		current.w = woord

	def find_words(self, begin_kar):
		gevonden_worden = []

		bovenste_node = self.root
		for kar in begin_kar:
			if kar in bovenste_node.d:
				bovenste_node = bovenste_node.d[kar]
			else:
				return gevonden_worden

		if bovenste_node == self.root:
			queue = [TrieNode for key, TrieNode in bovenste_node.d.items()]
		else:
			queue = [bovenste_node]

		while queue:
			current = queue.pop()
			if current.w != None:
				gevonden_worden.append(current.w)

			queue = [TrieNode for key, TrieNode in current.d.items()] + queue

		return gevonden_worden


	def contains(self, woord):
		current = self.root
		for kar in woord:
			if kar in current.d:
				current = current.d[kar]
			else:
				return False

		return True

	def return_duplicates(self):
		return self.root.n


class method2:

	def run(self):
		trie = Trie()

		with open("opdracht_4.txt", "r") as file:
			lines = file.read().splitlines()
			for line in lines:
				if not line == "":
					words = line.split()
					for word in words:
						trie.insert(word)

			file.close()

		alphabet = list(trie.root.d.keys())
		dict_trie = {}
		duplicaties = trie.return_duplicates()

		for letter in alphabet:
			words = trie.find_words(letter)
			for word in words:
				if word in duplicaties:
					dict_trie.update({word: duplicaties.get(word)})
				else:
					dict_trie.update({word: 1})

		csv_writer(dict_trie)



counter1 = method1()
counter1.countWords()

counter2 = method2()
counter2.run()