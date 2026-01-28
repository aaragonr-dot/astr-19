class animal:

	def __init__(self, name, type):
		self.name = name 
		self.type = type
my_animal = animal("Manatee", "aquatic mammal")

print(f"My favorite animal is {my_animal.name} and the breed is {my_animal.type}.")


class animal:

	def __int__(self, arm_length: float, has_leg: bool, number_of_eyes: int, has_tail: bool, is_furry: bool):

		self.arm_length = arm_length
		self.has_leg = has_leg
		self.number_of_eyes = number_of_eyes
		self.has_tail = has_tail
		self.is_furry = is_furry

	my_animal = animal(arm_length=18.9, has_leg = False, number_of_eyes = 2, has_tail = True, is_furry = False)

	def display_characteristics(self):
		
		print(f"Arm length: {my_animal.arm_length} inches")
		print(f"Has leg? {my_animal.has_leg}.")
		print(f"Number of eyes:{my_animal.has_trail}.")
		print(f"Has a tail {my_animal.has_tail}.")
		print(f"Is it furry?{my_animal.is_furry}.")

