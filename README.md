# CHEM-3RP3
Code written to fit a quadratic to reaction pathways as part of a project completed for a research course at McMaster University.

This python script includes the necessary code to do reaction fitting and graph drawing. Before using the code you must install miniconda, and python 3 is preferred. Both numpy and matplotlib are required to run this code successfully. Once you have downloaded the "solve_quad.py" file, open your terminal and go to the directory where you saved the file and open your python interpreter. Copy these two lines of code (after replacing "number1" with the energy of the reactant, "number2" with the energy of the transition state, and "number3" with the energy of the product for any particular reaction pathway you are trying to model):
line 1:from solve_quad import solve_and_draw 
line 2:solve_and_draw(number1, number2, number3)
into the interpreter to solve for the quadratic fit to the reaction path, a graph will be returned for the reaction pathway.