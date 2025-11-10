import cirq
import numpy

# Gets the input and converts it into its ascii characters
message = input("Enter message")
ascii_values = [ord(char) for char in message]

# Defines the qubit and the list of circuits
qubit = cirq.NamedQubit("myqubit")
circuits = []
for value in ascii_values:
  circuits.append(cirq.Circuit())

# Gets the digit of all the ascii values
first_digit = [num // 100 for num in ascii_values]
second_digit = [(num % 100) // 10 for num in ascii_values]
third_digit = [num % 10 for num in ascii_values]

# Assigns gates based on the first digit
index = 0

for digit in first_digit:
  radian = np.pi/6 if digit == 0 else -(np.pi/6)
  circuits[index].append(cirq.Rx(rads=radian).on(qubit))
  index += 1

# Assigns gates based on the second digit
index = 0

for digit in second_digit:
  if digit == 0: circuits[index].append(cirq.I(qubit))
  elif digit == 1: circuits[index].append(cirq.X(qubit))
  elif digit == 2: circuits[index].append(cirq.Y(qubit))
  elif digit == 9: circuits[index].append(cirq.Z(qubit))
  index += 1

# Assigns gates based on the third digit
index = 0

for digit in third_digit:
  radian = digit * (np.pi / 12)
  circuits[index].append(cirq.Ry(rads=radian).on(qubit))
  index += 1

# Prints all the circuits
for i in range(len(circuits)):
  print(circuits[i])

# Gives the amplitudes for each letter
simulator = cirq.Simulator()
results = []
for circuit in circuits:
  results.append(simulator.simulate(circuit))

for i in range(len(results)):
  print(f"Result for letter " + message[i])
  print(results[i])
  print(" ")
  print("---------------")
  print(" ")
