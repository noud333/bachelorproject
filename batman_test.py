import batman
import numpy as np
import matplotlib.pyplot as plt

def main():
    params = batman.TransitParams()
    params.t0 = 0.                       #time of inferior conjunction
    params.per = 1.                      #orbital period
    params.rp = 0.25                      #planet radius (in units of stellar radii)
    params.a = 5.                       #semi-major axis (in units of stellar radii)
    params.inc = 86.                 #orbital inclination (in degrees)
    params.ecc = 0.                      #eccentricity
    params.w = 90.                       #longitude of periastron (in degrees)
    params.u = []                        #limb darkening coefficients [u1, u2]
    params.limb_dark = "uniform"         #limb darkening model

    t = np.linspace(-0.05, 0.05, 100)
    #ld_options = ["uniform", "linear", "quadratic","squareroot", "logarithmic", "exponential", "power2", "nonlinear"]
    #ld_coefficients = [[], [0.3], [0.1, 0.3], [0.1, 0.3], [0.1, 0.3], [0.1, 0.3], [0.1, 0.3], [0.5, 0.1, 0.1, -0.1]]

    
    #params.u = [0.5, 0.7]
    params.limb_dark = "linear"
    params.u = [1]

    #a = [5, 10, 20]
    #rp = [0.05, 0.15, 0.25]
    #inc = [86.25, 87.5, 90]

    # for i in a:
    #     params.a = i

    #     for j in rp:
    #         params.rp = j

    #         for k in inc:
    #             params.inc = k


    #             m = batman.TransitModel(params, t)    #initializes model
    #             flux = m.light_curve(params)          #calculates light curve

    for i in np.linspace(4,6, 5):
    
        params.a = i

        m = batman.TransitModel(params, t)    #initializes model
        flux = m.light_curve(params)          #calculates light curve

        plt.plot(t, flux, label= params.a)
        plt.legend(title=f"{params.limb_dark} LD")
    plt.xlabel("Time from central transit")
    plt.ylabel("Relative flux")
    plt.title(f"{params.limb_dark}, {params.u}")
    plt.savefig(f"data/tests/{params.limb_dark}_LD.png")
    #plt.savefig("data/tests/test.png")
    plt.clf()

if __name__ == "__main__":
    main()