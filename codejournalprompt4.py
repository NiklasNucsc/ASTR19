class Horse:

	def __init__(self, arm_length, leg_length, num_eyes, has_tail, is_furry):
		self.arm_length = arm_length
		self.leg_length = leg_length
		self.num_eyes = num_eyes
		self.has_tail = has_tail
		self.is_furry = is_furry

	def describe(self):
		print("Horse Physical Characteristics:")
		print(f"Length of arms: {self.arm_length} feet")
		print(f"Length of legs: {self.leg_length} feet")
		print(f"Number of eyes: {self.num_eyes}")
		print(f"Has tail? {'Yes' if self.has_tail else 'No'}")
		print(f"Is furry? {'Yes' if self.is_furry else 'No'}")


def main():
	my_horse = Horse(arm_length=3.0, leg_length=4.0, num_eyes=2, has_tail=True, is_furry=True)

	my_horse.describe()


if __name__=="__main__":
	main()