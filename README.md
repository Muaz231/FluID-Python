## This file specifies all the files and their functionality:

1) FluidID_configuration_xx.py where xx: 1GHz, 2GHz, 4GHz, 1024_samples_per_chirp contains the configuration parameters for different chirp configurations.
The parameters this file contains are:
		-> Chirp Start Frequency
		-> Chirp Ramp End Time
		-> Chirp IDLE Time
		-> Chirp ADC Start Time 
		-> Frequency Slope
		-> Receiver Sampling Rate
		-> # of TX, # of Receivers, # of samples/chirp

2) FluidID_clean.ipynb is the JUPYTER Notebook that contains all functions for chirp preprocessing such as:
		-> Range-FFT Calculation
		-> AoA calculation using MUSIC & compensation
		-> Frequency Response Estimation using Envelope detection of the time domain IF waveform samples
		-> Data Visualization

3) 77GHz_sim.ipynb is the JUPYTER Notebook that contains simulation of 77GHz FMCW radar for one chirp to estimate the optimal window size to correctly track 
the IF signal envelope.
