'''this program generates time domain waveforms'''

import matplotlib.pyplot as pp
from pycbc.waveform import get_td_waveform
from pycbc.waveform import td_approximants

#print(td_approximants())

for apx in ['TaylorT1', 'TaylorT2']:
    hp, hc = get_td_waveform(approximant=apx, mass1=10, mass2=10, delta_t=1.0/4000, f_lower=40)

    pp.plot(hp.sample_times, hp, label=apx)

pp.ylabel('Strain')
pp.xlabel('Times(s)')
pp.legend()
pp.show()