[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/ThvOakQ-)


# Black Hole Orbital Trajectory


## Overview
The project aims to explore black hole orbits, focusing on understanding how angular momentum and energy
influences the motion of objects around it. Through theoretical analysis and numerical simulations,the project
delves into topics such as the effective potential and various types of orbits that can exist in the vicinity of a black
hole. As well as the calculation of the trajectory of an object on a given orbit.
More detailed descriptions of the mathematical background and code overview can be found in the final report and the sphinx documentations.

## Final Report
The final report can be found in the `report` directory. Inside the directory you can find the latex file as well as the rendered pdf file.

To build the report from source files in the repo from your local machine follow these steps:

1. `cd report/`
2. `pdflatex finalreport.tex`
3. `open finalreport.pdf`

## Sphinx Documentations
The manual for the classes can be accessed through sphinx. Inside the `docs` directory you can find the files responsible for creating the html and pdf versions of the documentations.

### HTML Manual
You can build and view the manual in html format by following these steps:

1. `cd docs/`
2. `make html`
3. `cd _build/html/`
4. `open index.html`

### PDF Manual
You can build and view the manual in pdf format by following these steps:

1. `cd docs/`
2. `make latexpdf`
3. `cd _build/latex/`
4. `pdflatex blackholeorbitaltrajectory.tex`
5. `open blackholeorbitaltrajectory.pdf`