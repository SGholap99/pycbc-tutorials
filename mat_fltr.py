''' A basic example of matched filtering '''

import matplotlib.pyplot as pp
import pycbc.noise
import pycbc.psd
import pycbc.waveform
import pycbc.filter

#attributes of PSD
delta_f = 1.0 / 16           # step size in frequency space
flen = int(2048 / delta_f)   # no. of sampling pts.
low_frequency_cutoff = 30.0 # lower bound on frequency in the plot

# call the psd generator
aLIGO =pycbc.psd.aLIGOZeroDetHighPower(flen, delta_f, low_frequency_cutoff)

# Generate 10 sec of noise at 1000Hz
delta_t = 1.0/4096
tsamples = int(16/delta_t)
strain = pycbc.noise.noise_from_psd(tsamples, delta_t, aLIGO, seed=127)
stilde = strain.to_frequencyseries()

#Here we use a waveform as a matched filter
hp, hc = pycbc.waveform.get_fd_waveform(approximant='IMRPhenomD', mass1=10, mass2=10, f_lower=low_frequency_cutoff, delta_f=stilde.delta_f)

hp.resize(len(stilde))
snr = pycbc.filter.matched_filter(hp, stilde, psd=TAMA, low_frequency_cutoff=low_frequency_cutoff  )

pp.plot(snr.sample_times, abs(snr))
pp.ylabel('SNR')
pp.xlabel('time(s)')
pp.show()