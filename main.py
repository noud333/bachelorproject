import warnings
warnings.filterwarnings('ignore')
import pandexo.engine.justdoit as jdi # THIS IS THE HOLY GRAIL OF PANDEXO
import numpy as np
import os

exo_dict = jdi.load_exo_dict()
print(jdi.print_instruments())

exo_dict['observation']['sat_level'] = 80    #saturation level in percent of full well
exo_dict['observation']['sat_unit'] = '%'
exo_dict['observation']['noccultations'] = 2 #number of transits
exo_dict['observation']['R'] = None          #fixed binning. I usually suggest ZERO binning.. you can always bin later
                                             #without having to redo the calcualtion
exo_dict['observation']['baseline_unit'] = 'total'  #Defines how you specify out of transit observing time
                                                    #'frac' : fraction of time in transit versus out = in/out
                                                    #'total' : total observing time (seconds)
exo_dict['observation']['baseline'] = 4.0*60.0*60.0 #in accordance with what was specified above (total observing time)

exo_dict['observation']['noise_floor'] = 0   #this can be a fixed level or it can be a filepath
                                             #to a wavelength dependent noise floor solution (units are ppm)

exo_dict['star']['type'] = 'phoenix'        #phoenix or user (if you have your own)
exo_dict['star']['mag'] = 8.0               #magnitude of the system
exo_dict['star']['ref_wave'] = 1.25         #For J mag = 1.25, H = 1.6, K =2.22.. etc (all in micron)
exo_dict['star']['temp'] = 5500             #in K
exo_dict['star']['metal'] = 0.0             # as log Fe/H
exo_dict['star']['logg'] = 4.0              #log surface gravity cgs

exo_dict['planet']['type'] = 'constant'                  #tells pandexo you want a fixed transit depth

exo_dict['planet']['transit_duration'] = 2.0*60.0*60.0   #transit duration
exo_dict['planet']['td_unit'] = 's'


exo_dict['star']['radius'] = 1
exo_dict['star']['r_unit'] = 'R_sun'              #Same deal with astropy.units here

#exo_dict['planet']['f_unit'] = 'rp^2/r*^2'        #this is what you would do for primary transit

#ORRRRR....
#if you wanted to instead to secondary transit at constant temperature


# exo_dict['planet']['radius'] = 1
# exo_dict['planet']['r_unit'] = 'R_jup'            #Any unit of distance in accordance with astropy.units can be added here

# exo_dict['planet']['f_unit'] = 'fp/f*'
# exo_dict['planet']['temp'] = 3000

exo_dict['planet']['type'] ='user'                       #tells pandexo you are uploading your own spectrum
exo_dict['planet']['exopath'] = 'data/tests/eclipsedepth_T=3000.txt'
exo_dict['planet']['w_unit'] = 'cm'                      #other options include "um","nm" ,"Angs", "sec" (for phase curves)
exo_dict['planet']['f_unit'] = 'fp/f*'               #other options are 'fp/f*'

# result = jdi.run_pandexo(exo_dict, ['NIRSpec G140M', 'NIRSpec G140H', 'NIRSpec G235M', 'NIRSpec G235H',
#  'NIRSpec G395M', 'NIRSpec G395H', 'NIRSpec Prism'], output_file= "data/tests/all_NIRSpec.p")

#result = jdi.run_pandexo(exo_dict, ['NIRSpec G140H'], output_file= "data/tests/all_NIRSpec.p")

NIRSPEC_inst = ['NIRSpec G140M', 'NIRSpec G140H', 'NIRSpec G235M', 'NIRSpec G235H', 'NIRSpec G395M', 'NIRSpec G395H', 'NIRSpec Prism']
# JWST_inst = ['WFC3 G141', 'MIRI LRS', 'NIRISS SOSS', 'NIRSpec G140M', 'NIRSpec G140H', 'NIRSpec G235M', 'NIRSpec G235H', 'NIRSpec G395M', 'NIRSpec G395H', 'NIRSpec Prism', 'NIRCam F322W2', 'NIRCam F444W']
# JWST_inst = ['MIRI LRS', 'NIRISS SOSS', 'NIRSpec G140M', 'NIRSpec G140H', 'NIRSpec G235M', 'NIRSpec G235H', 'NIRSpec G395M', 'NIRSpec G395H', 'NIRSpec Prism', 'NIRCam F322W2', 'NIRCam F444W']

inst = 'NIRSpec G140H'

# for inst in JWST_inst:
# for inst in NIRSPEC_inst:
#for temp in range(500, 3001, 500):

#    exo_dict['planet']['temp'] = temp
result = jdi.run_pandexo(exo_dict, [f'{inst}'], output_file= f"data/pandexo/{inst}_3000.p")
