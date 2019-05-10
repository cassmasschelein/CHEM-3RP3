# CHEM-3RP3
Code written to fit a quadratic to reaction pathways as part of a project completed for a research course at McMaster University.

This python script includes the necessary code to do reaction fitting and graph drawing. Before using the code you must install miniconda, and python 3 is preferred. Both numpy and matplotlib are required to run this code successfully. Download both the "solve_quad.py" file and the "solve_and_draw.py" file. First customize "solve_and_draw.py" such that you replace "number1" with the energy of the reactant, replace "number2" with the energy of the transition state, and replace "number3" with the energy of the product for any particular reaction pathway you are trying to model. Then, open your terminal and go to the directory where you saved the files and open your python interpreter. Copy this line of code:

"from solve_quad import solve_and_draw"

into the interpreter to solve for the quadratic fit to the reaction path, a graph will be returned for the reaction pathway.