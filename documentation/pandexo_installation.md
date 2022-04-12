# How pandexo finally worked.
I did this all form a ubuntu-20.04 WSL shell on windows.

Start with an anaconda environment with python 3.6 (3.6 is important for scipy==1.3.1 which is necessary for pandexo 1.5.3.1)

This version uses pandeia.engine==1.6 therefore you need reference data 1.6 (not 1.5 which is found on the site or 1.7 which is the most up to date version.) (There is also a pandeia.engine==1.7 but pandexo.engine is not yet compatible with this one, therefore 1.6 is used and the wrong set of reference data will result in a code that doesn't work.)

Pandeia reference data 1.6 can be found here https://stsci.app.box.com/v/pandeia-refdata-v1p6

Besides that, https://natashabatalha.github.io/PandExo/installation.html#installation-with-pip-or-git can be followed. 

Using 'echo $pandeia_refdata' and 'echo $PYSYN_CDBS' is a good way to check whether or not the export functions from the link above have been done right.

## Small notes
During the installation I got the import error in this line: 'from astropy.modeling import blackbody as bb' blackbody is not a function in the most up to date version of astropy. But astropy==4.1 or up to 4.2.1 should have this function and still work. I myself used astropy==4.1.

With astropy==4.1 the most up to date version of photutils is no longer compatible. I used photutils==1.0.2.

The anaconda environment I used to set everything up came from the environment.yml file from https://github.com/ers-transit/hackathon-2021-day0. I did change the python version from 3.9 back to 3.6 as mentioned earlier.