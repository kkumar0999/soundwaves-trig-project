# soundwaves-trig-project
This repository stores the code for my Algebra 2/Trigonometry project!

Now, considering that I made this project in my sophomore year of high school with a deadline, it's no wonder that the actual code is a little messy... But I wanted to publish this because this project was actually the main inspiration for my [audio visualizer project!](https://github.com/kkumar0999/audio-visualizer) So if you'd like to check that out, you can as well.

## Background
One day in class, my teacher assigned our class a project for our trigonometry unit. Specifically, we had to represent something in real life with sinusoidal functions.

While the expectations only called for something along the lines of something that performed circular rotations or revolutions, I had an interesting idea: Could I use code to represent a complex sound wave with purely sinusoidal functions?

So what my partner and I did was we did both! We used a vinyl to get the rotation aspect, and we also recorded a short clip from the vinyl to analyze. This repository focuses on the sound analysis portion of that project.

## Project Findings
The theory, findings, and reflection on the sound analysis portion of the project can be found in the [SoundWaveProjectReflection.pdf](SoundWaveProjectReflection.pdf) file.

## Project Structure
- `src/` - source code files
- `SoundWaveProjectReflection.pdf` - Project reflection and write-up
- `requirements.txt` - Python dependencies
- `LICENSE` - MIT License
- `README.md` - This file

## Getting Started

### Prerequisites
Make sure you have Python installed, then install the required libraries by running:

`pip install -r requirements.txt`

### Running the Project
1. Update the configuration variables in `main.py` as necessary. Specifically:
    - Change `NUM_WAVES` to the number of waves you want the approximation to use.
    - Change `SCALE` to the factor in which you want amplitude values to be scaled down by.
    - Change `DESTINATION` to the desired destination file you want the final approximation to be outputted to.
    - Change `LATEX_MODE` depending on whether you want a LaTeX or Desmos output. `True` corresponds to LaTeX formatting, while `False` corresponds to Desmos formatting.
2. Run `main.py` from within the `src/` directory (or update paths accordingly).

## License
This project is open source and available under the MIT License. For more information, refer to the [LICENSE](LICENSE) file.