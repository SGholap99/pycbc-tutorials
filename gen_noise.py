'''this program generated time domain gaussian noise from a given PSD'''

import matplotlib.pyplot as pp
import pycbc.noise
import pycbc.psd

#attributes of PSD
delta_f = 1.0 / 4           # step size in frequency space
flen = int(500 / delta_f)   # no. of sampling pts.
low_frequency_cutoff = 30.0 # lower bound on frequency in the plot

# call the psd generator
TAMA =pycbc.psd.TAMA(flen, delta_f, low_frequency_cutoff)

# Generate 10 sec of noise at 1000Hz
delta_t = 1.0/100
tsamples = int(10/delta_t)
time_series = pycbc.noise.noise_from_psd(tsamples, delta_t, TAMA, seed=127)

pp.plot(time_series.sample_times, time_series)
pp.ylabel('Strain')
pp.xlabel('Time(s)')
pp.show()


