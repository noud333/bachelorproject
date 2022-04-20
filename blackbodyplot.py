import wave
from platon.TP_profile import Profile
from platon.eclipse_depth_calculator import EclipseDepthCalculator
import matplotlib.pyplot as plt
import json
import numpy as np

planet_temp = 3000

for planet_temp in range(500,3001,500):
    p = Profile()
    p.set_isothermal(planet_temp)

    calc = EclipseDepthCalculator(method="xsec") #"ktables" for correlated k
    wavelengths, depths = calc.compute_depths(p, 696340 * (10**3), 1.99 * (10**30), 69911 * (10**3) , 5778, stellar_blackbody=True)
    #wavelengths, depths = calc.compute_depths(p, Rs, Mp, Rp, Tstar)

    # input(wavelengths)
    # input(depths)

    plt.plot(wavelengths, depths)
    #plt.xscale('log')
    # plt.yscale('log')
    #plt.xlim(0.0000009, 0.0000013)
    plt.ylim(depths[0]/2, depths[-1]+ depths[0])
    plt.title(f'T planet = {planet_temp}')
    plt.xlabel('Wavelength (m)')
    plt.ylabel('Eclipse depth (f_planet / f_star)')
    plt.savefig(f"data/tests/eclipsedepth_T={planet_temp}.png")
    plt.cla()


    wavelengths = np.array(wavelengths) * 100
    depths = np.array(depths)


    data = np.column_stack([wavelengths, depths])
    datafile_path = f'data/tests/eclipsedepth_T={planet_temp}.txt'
    np.savetxt(datafile_path , data, fmt=['%2.10f','%2.45f'])

    # change star to blackbody, look into ranges of JWST machines.
    # look into signal to noise
