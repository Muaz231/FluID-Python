# mmWave Sensing ***(In Progress)***
---

## Getting Started
- This GitHub repository contains Python and MATLAB code for the mmWave Sensing Project
### File Naming Conventions: 

- **FluidID_clean.ipynb** is the *JUPYTER Notebook* that contains <ins> **Python code** </ins>  all functions for chirp preprocessing & signal processing such as: 
 - Range-FFT Calculation
 - AoA calculation using MUSIC & compensation 
 - Frequency Response Estimation using Envelope detection of the time domain IF waveform samples 
 - Data Visualization

- **FluidID_configuration_xx.py** where xx: 1GHz, 2GHz, 4GHz, 1024_samples_per_chirp contains the ***configuration parameters*** for different FMCW chirps.
The parameters this file contains are:
	- Chirp Start Frequency
	- Chirp Ramp End Time
	- Chirp IDLE Time
	- Chirp ADC Start Time 
	- Frequency Slope
	- Receiver Sampling Rate
	- \# of TX, # of Receivers, # of samples/chirp

- **77GHz_sim.ipynb** is the JUPYTER Notebook that contains <ins>**Python code**</ins> simulation of 77GHz FMCW radar for one chirp to estimate the optimal window size to correctly track the IF signal envelope.

- The file **Matlab_TDM_Simulation->MIMORadarVirtualArrayExample_MUSIC_AoA_Estimation.m** contains <ins>**MATLAB code**</ins> (from MATLAB Examples) for simulating TDM MIMO FMCW radar and to estimate the AoA using MUSIC algorithm.

- The file **Matlab_TDM_Simulation->helperDesignFMCWWaveform.m** contains <ins>**MATLAB code**</ins> (from MATLAB Examples) for generating the FMCW waveform.

### Authors
---
-  Muhammad Muaz
- Affiliation: University of Texas at Austin
- Email: [m.muaz@utexas.edu](m.muaz@utexas.edu)
---
