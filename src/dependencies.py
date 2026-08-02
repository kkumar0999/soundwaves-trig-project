from scipy.io import wavfile
import numpy as np

def write_all_equations(filenames, destination, num_waves, scale, latex_mode):
    for filename in filenames:
        write_equations(filename, destination, num_waves, scale, latex_mode)

# audio file, destination file
def write_equations(filename, destination, num_waves, scale, latex_mode):
    # Fs, x[n]
    rate, data = wavfile.read(filename)

    # Converts to mono if needed by averaging the columns
    if data.ndim == 2:
        data = data.mean(axis=1)

    # X
    transform = np.fft.fft(data)

    # with /len(transform), it makes the amplitudes actually useful amp values
    amps = np.abs(transform) / len(transform)
    phases = np.angle(transform)
    freqs = np.fft.fftfreq(len(data), 1/rate)

    N = len(transform)
    
    # Cut out negatives
    amps = amps[:N//2]
    freqs = freqs[:N//2]
    phases = phases[:N//2]

    # Get top indices
    top_indices = np.argsort(amps)[-num_waves:]
    top_indices = sorted(top_indices, key=lambda i: freqs[i])

    #Scaled down amplitudes, writes the equation
    with open(destination, 'a') as file:
        file.write(f"{filename}\n")
        for j in range(num_waves-1):
            i = top_indices[j] # Gets index from top indices
            write_equation(file, amps[i]/scale, freqs[i], phases[i], False, latex_mode)
        write_equation(file, amps[num_waves-1]/scale, freqs[num_waves-1], phases[num_waves-1], True, latex_mode)

        if not latex_mode:
            file.write("\\left\\{0\\le x\\le " + f"{N/rate:.3f}" + "\\right\\}\n")

def write_equation(file, amp, freq, phase, is_end, is_latex):
    if is_latex:
        file.write(f"{amp:.3f}\\cos(2\\pi {freq:.3f} x")
        # Handles negatives
        if phase > 0:
            file.write(f" + {phase:.3f})")
        else:
            file.write(f" - {abs(phase):.3f})")
        
        # Handles spacing (prints out each equation line by line)
        if not is_end:
            file.write(" +\n")
    else:
        file.write(f"{amp:.3f}cos(2\\pi{freq:.3f}x")

        # Handles negatives
        if phase > 0:
            file.write(f" + {phase:.3f})")
        else:
            file.write(f" - {abs(phase):.3f})")

        # Handles spacing (prints all equations on one line)
        if is_end:
            file.write("\n")
        else:
            file.write(" + ")

# Ensures that the file exists and is blank
def ensure_file(filename):
    with open(filename, 'w'):
        pass

# Returns whether a file exists
def file_exists(filename):
    try:
        with open(filename, 'r'):
            return True
    except FileNotFoundError:
        return False