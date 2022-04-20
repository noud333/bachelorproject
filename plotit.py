import pandexo.engine.justplotit as jpi
import pickle as pk
import matplotlib.pyplot as plt

#load in output from run
out = pk.load(open(f'data/pandexo/NIRSpec G140H_3000.p', 'rb'))
#for a single run
x,y, e = jpi.jwst_1d_spec(out, R=100, num_tran=1, model=False, x_range=[.9,1.28], output_file=f'data/pandexo/NIRSPEC G140H_3000.html')


# NIRSPEC_inst = ['NIRSpec G140M', 'NIRSpec G140H', 'NIRSpec G235M', 'NIRSpec G235H', 'NIRSpec G395M', 'NIRSpec G395H', 'NIRSpec Prism']
# JWST_inst = ['MIRI LRS', 'NIRISS SOSS', 'NIRSpec G140M', 'NIRSpec G140H', 'NIRSpec G235M', 'NIRSpec G235H', 'NIRSpec G395M', 'NIRSpec G395H', 'NIRSpec Prism', 'NIRCam F322W2', 'NIRCam F444W']

# for inst in JWST_inst:
#     for temp in range(500, 3001, 500):


#         #load in output from run
#         out = pk.load(open(f'data/pandexo/{inst}_{temp}.p', 'rb'))
#         #for a single run
#         x,y, e = jpi.jwst_1d_spec(out, R=100, num_tran=1, model=False, x_range=[.9,1.28], output_file=f'data/pandexo/{inst}_{temp}.html')
