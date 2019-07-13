# PyMathProblemGenerator

PyMathProblemGenerator is a problem generator coded in python using PyQt5 as a user interface and Wolfram Mathematica to render and compute mathematical problems.

## Building from source
Make sure you have all the dependencies before proceeding. Open a terminal window then run ```pyinstaller PyMathProblemGenerator.spec``` in the same folder that the source code is located. The build should now appear in dist.

## Installation

Run the executable after extracting the files from the download. For Windows users, run the file PyMathProblemGenerator.exe as is.

For macOSX users, place repo.mx and definitions.mx inside the users/<your name here> directory then run the app.

Instructions for Linux users TBD.

## Usage

For Windows and macOS X users:
By running PyMathProblemGenerator, the app will appear. The topic can be changed in settings in addition to the difficulty.

For Linux Users:
By running main.py, the user interface will appear. This requires Wolfram Mathematica to be functional. By running maindesign.py, the problem designer (not finished yet) will open, and problems can be designed and imported (not implemented yet). Instructions on this will be published soon.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## Goals
Finishing the Problem designer, and making it accessible to more people who aren't familiar with the wolfram language. 

Implement a better repository storage mechanism rather than store from a local file.

## License
[MIT](https://choosealicense.com/licenses/mit/)
