from dependencies import *

NUM_WAVES = 20 # Specifies the number of waves to approximate with
SCALE = 100 # Scale down factor
DESTINATION = "../equations.txt"  # Destination file for equations
LATEX_MODE = False  # True outputs out LaTeX formatting, False outputs Desmos formatting

# Prints your configurations
if LATEX_MODE:
    print("Mode: LATEX")
else:
    print("Mode: DESMOS")

print(f"Scale: {SCALE}")
print(f"Wave Count: {NUM_WAVES}")
print(f"Destination: {DESTINATION}")

# Gets all filenames to get the equation for
filenames = []
while True:
    filename = input("Enter in the next filename (type QUIT to finish): ").strip()

    if filename == "QUIT":
        break

    if file_exists(filename):
        filenames.append(filename)
    else:
        print(f"Error: File {filename} not found!")

ensure_file(DESTINATION) # Ensures the destination file exists
write_all_equations(filenames, DESTINATION, NUM_WAVES, SCALE, LATEX_MODE)

# Prints a message if it succeeds
N = len(filenames)
if N > 0:
    print(f"Wrote all {N} equations to {DESTINATION}.")