import numpy as np 
import matplotlib.pyplot as plt

def main():

	n = 1000
	x_values = np.linspace(0, 2 * np.pi, n)
	y_values = np.sin(x_values)

	print(f"{'x (radians)' :>15} {'sin(x)' :>15}")
	print("-" * 30)

	for x, y in zip(x_values, y_values):
		print(f"{x:15.8} {y:15.8}")

	plt.plot(x_values, y_values, label="sin(x)", color="blue", linewidth=2)
	plt.xlabel("x (radians)")
	plt.ylabel("sin(x)")
	plt.grid(True)
	plt.legend()

	plt.show()


if __name__ == "__main__":
	main()