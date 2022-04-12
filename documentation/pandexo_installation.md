# How pandexo finally worked.
I did this all form a ubuntu-20.04 WSL shell on windows.

Start with an anaconda environment with python 3.6 (3.6 is important for scipy==1.3.1 which is necessary for pandexo 1.5.3.1)

This version uses pandeia.engine==1.6 therefore you need reference data 1.6 (not 1.5 which is found on the site or 1.7 which is the most up to date version.) (There is also a pandeia.engine==1.7 but pandexo.engine is not yet compatible with this one, therefore 1.6 is used and the wrong set of reference data will result in a code that doesn't work.)

Pandeia reference data 1.6 can be found here https://stsci.app.box.com/v/pandeia-refdata-v1p6

Besides that, https://natashabatalha.github.io/PandExo/installation.html#installation-with-pip-or-git can be followed. 

Using 'echo $pandeia_refdata' and 'echo $PYSYN_CDBS' is a good way to check whether or not the export functions from the link above have been done right.

