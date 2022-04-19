import numpy as np

NUM_TX = 1 # tx order tx0,tx2,tx1, face to the board (left,right,upper)  -- Only using tx0 for FLUID-ID Project
NUM_RX = 4

START_FREQ = 77 # Starting frequencies of chirps (77-80 GHz)
ADC_START_TIME = 3.26
FREQ_SLOPE = 16.222
ADC_SAMPLES = 256 # data samples per chirp
SAMPLE_RATE = 4500
RX_GAIN = 30 

IDLE_TIME = 4
RAMP_END_TIME = 61.27
#  2 for 1843
NUM_FRAMES = 0 
#  Set this to 0 to continuously stream data
LOOPS_PER_FRAME = 128*4 # num of chirp loop, one loop has four chirps
#PERIODICITY = 100 
# time for one chirp in ms  100ms == 10FPS
NUM_DOPPLER_BINS = LOOPS_PER_FRAME
NUM_RANGE_BINS = ADC_SAMPLES
NUM_ANGLE_BINS = 64
RANGE_RESOLUTION = (3e8 * SAMPLE_RATE * 1e3) / (2 * FREQ_SLOPE * 1e12 * ADC_SAMPLES)
MAX_RANGE = (300 * SAMPLE_RATE) / (2 * FREQ_SLOPE * 1e3)
DOPPLER_RESOLUTION = 3e8 / (2 * START_FREQ * 1e9 * (IDLE_TIME + RAMP_END_TIME) * 1e-6 * NUM_DOPPLER_BINS * NUM_TX)
MAX_DOPPLER = 3e8 / (4 * START_FREQ * 1e9 * (IDLE_TIME + RAMP_END_TIME) * 1e-6 * NUM_TX)
BANDWIDTH = np.abs(FREQ_SLOPE*ADC_SAMPLES/SAMPLE_RATE)*1e9 # Total Sweep BW (Hz)