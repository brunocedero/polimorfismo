class Number:
	value = 0

	def __init__(self, value):
		self.value = value

	def compare(self, number):
		if numero.value > self.value:
			return numero.value
		return self.value


class String:
	value = ""

	def __init__(self, value):
		self.value = value

	def compare(self, string_compare):
		words = [self.value, string_compare.value]
		words.sort()
		return words[0]


class List:
	value = []

	def __init__(self, value):
		self.value = value

	def compare(self, list_compare):
		if len(self.value) > len(list_compare.value):
			return self.value
		return list_compare.value


def returnTheBigger(a,b):
	a.compare(b)


#testing methods:
number_one = Number(10)
number_two = Number(13)


string_one = String("hello")
string_two = String("bye")


list_one = List([1,2])
list_two = List([1,2,3])


print(returnTheBigger(string_one,string_two))