import csv
import sys

"""
Definition
	Function to write to a csv file

Parameters
----------
dict : dictionary
	The dictionary containing the words as keys, and the count as values.

"""
def csv_writer(dict):
	with open("E:/School/2017-2018/blok_2/Algorithms and Datastructures/assignments/Week 3/opdracht_4.csv", "w") as dest:
		file = csv.writer(dest, sys.stdout, delimiter=',', lineterminator='\n')
		for key, value in dict.items():
			file.writerow( (key, value) )
	dest.close()

class method1:
	def writeToFile(self, dict):
		with open("E:/School/2017-2018/blok_2/Algorithms and Datastructures/assignments/Week 3/opdracht_4.csv", "w") as csvfile:
			file = csv.writer(csvfile, sys.stdout, delimiter=',', lineterminator='\n')
			for key, value in dict.items():
				file.writerow( (key, value) )
		csvfile.close()

	def countWords(self):
		words_dict = {}
		with open("E:/School/2017-2018/blok_2/Algorithms and Datastructures/assignments/Week 3/opdracht_4.txt", "r") as file:
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

	def insert(self, word):
		self.d[word] = TrieNode()

class Trie:
	def __init__(self):
		self.root = TrieNode()

	def insert(self, word):
		current = self.root

		if self.contains(word):
			if word in current.n:
				current.n[word] = (current.n.get(word) + 1)
			else:
				current.n.update({word: 2})
			return

		for i in range(len(word)):
			if word[i] in current.d:
				current = current.d[word[i]]
			else:
				# Complete word
				while i < len(word):
					current.insert(word[i])
					current = current.d[word[i]]
					i += 1
		current.w = word

	def find_words(self, begin_char):
		found_words = []

		top_node = self.root
		for char in begin_char:
			if char in top_node.d:
				top_node = top_node.d[char]
			else:
				return found_words

		if top_node == self.root:
			queue = [TrieNode for key, TrieNode in top_node.d.items()]
		else:
			queue = [top_node]

		while queue:
			current = queue.pop()
			if current.w != None:
				found_words.append(current.w)

			queue = [TrieNode for key, TrieNode in current.d.items()] + queue

		return found_words


	def contains(self, word):
		current = self.root
		for char in word:
			if char in current.d:
				current = current.d[char]
			else:
				return False

		return True

	def return_duplicates(self):
		return self.root.n


class method2:

	def run(self):
		trie = Trie()

		with open("E:/School/2017-2018/blok_2/Algorithms and Datastructures/assignments/Week 3/opdracht_4.txt", "r") as file:
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