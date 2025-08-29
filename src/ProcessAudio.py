import numpy as np
from scipy.io import wavfile
from scipy.fft import fft, fftfreq

WAVE_LOCATION = "../wav/c-major-scale.wav"
SAMPLE_RATE, data = wavfile.read(open(WAVE_LOCATION, "rb"))

# Convert to mono if stereo
if len(data.shape) > 1:
    data = data.mean(axis=1)

frame_size = 1024  # number of samples per frame
hop_size = 512     # overlap (optional, for smoother tracking)

for start in range(0, len(data), hop_size):
    frame = data[start:start+frame_size]
    
    if len(frame) < frame_size:
        break  # skip last incomplete frame
    
    # FFT
    spectrum = np.abs(fft(frame))
    freqs = fftfreq(frame_size, d=1/SAMPLE_RATE)
    
    # Only positive frequencies
    pos_mask = freqs > 0
    freqs = freqs[pos_mask]
    spectrum = spectrum[pos_mask]
    
    # Find dominant frequency
    dominant_freq = freqs[np.argmax(spectrum)]
    print(f"Frame starting at sample {start}: {dominant_freq:.2f} Hz")