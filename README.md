# PyMol
This function is used to identify the pairs of amino acids that are forming disulfide bonds in a chain.
By running this script with the desired chain as the argument, the residue numbers of the amino acids will be printed.

Before use:
- Download the find_dsfpairs.py file to your home directory. (Typing "pwd" in the PyMol command line will show the home directory)

Example:

PyMOL>run find_dsfpairs.py

PyMOL>find_dsfpairs chain A

Residue pairs forming disulfide bonds:[('28', '274'), ('109', '186')]
