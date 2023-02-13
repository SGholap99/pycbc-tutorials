'''code to generate builltin PSDs in LALsimulation'''

import matplotlib.pyplot as pp
import pycbc.psd

#print(pycbc.psd.get_lalsim_psd_list()) #gets the list of all possible noises for different detectors

#attributes for psd generation
delta_f = 1.0 / 4           # step size in frequency space
flen = int(500 / delta_f)   # no. of sampling pts.
low_frequency_cutoff = 30.0 # lower bound on frequency in the plot

# call the psd generator
TAMA =pycbc.psd.TAMA(flen, delta_f, low_frequency_cutoff)

pp.plot(TAMA.sample_frequencies, TAMA, label='TAMA Detector')
pp.legend()
pp.show()



