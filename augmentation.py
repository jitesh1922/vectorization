import numpy as np
import librosa 

def add_noise(signal, noise_factor):
    noise = np.random.normal(0, signal.std(), signal.size)
    aug_sig = signal + noise * noise_factor
    return  aug_sig

def time_stretcha(signal, stretch_rate):
    return librosa.effect.time.time_stretch(signal, stretch_rate)

def pitch_scalling(signal, sr, num_semintones):
    return librosa.effect.pitch_shift(signal. sr, num_semintones)

def invert_polarity(signal):
    return signal * -1


def random_gain(signal, min_gain_factor, max_gain_factor):
    gain_factor = random.uniform(min_gain_factor, max_gain_factor)
    return signal  * gain_factor

if __name__ == "__main__":
    signal, sr = librosa.load("wav_file_path")
    aug_signal = add_noise(signal, 0.1)
