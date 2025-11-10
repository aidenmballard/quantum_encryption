import cirq
import numpy

# List of possible real amplitudes
real_list = {
    "a1" : 0.588,
    "a2" : 0.766,
    "b1" : 0.483,
    "b2" : 0.837,
    "c1" : 0.370,
    "c2" : 0.892,
    "d1" : 0.966,
    "d2" : 0,
    "e1" : 0.958,
    "e2" : 0.126,
    "f1" : 0.933,
    "f2" : 0.250,
    "g1" : 0.892,
    "g2" : 0.370
}

# List of possible imaginary amplitudes
imag_list = {
    "a1" : -0.205,
    "a2" : 0.158,
    "b1" : -0.224,
    "b2" : 0.129,
    "c1" : -0.239,
    "c2" : 0.099,
    "d1" : 0,
    "d2" : 0.259,
    "e1" : -0.034,
    "e2" : 0.257,
    "f1" : -0.067,
    "f2" : 0.250,
    "g1" : -0.099,
    "g2" : 0.239
}

# List of inputs
real_amplitudes = []
imag_amplitudes = []

# Gets input amplitudes
for i in range(len(message)):
  real_amplitudes.append(float(input("Input the first real number")))
  real_amplitudes.append(float(input("Input the second real number")))

  imag_amplitudes.append(float(input("Input the first imag number")))
  imag_amplitudes.append(float(input("Input the second imag number")))

# Gets the list of dictionary keys and defines variables
key_list = list(real_list.keys())
matching_keys = []
decrypted_word = ""

# Checks if a key matches an input
for i in range(len(real_amplitudes)):
  for j in range(len(key_list)):
    if real_amplitudes[i] == real_list[key_list[j]]:
      matching_keys.append(key_list[j])

# Checks if there are two matching inputs
for i in range(len(matching_keys) - 1):
  temp = matching_keys[i]
  temp2 = matching_keys[i + 1]

  # Adds the letter to the decrypted word
  if (temp[:1] == temp2[:1]):
    decrypted_word = decrypted_word + temp[:1]

# Prints the final word
print(decrypted_word)
