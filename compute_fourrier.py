import pandas as pd
import numpy as np


def get_fourrier_transform(data_file:str) -> dict:
    """Compute FFT for signal extracted from a single file and return FFT, Amplitude and Phase
    
    Args:
        - data_file (str) : path to the input csv file

    Returns:
        - (dict) : with FFT, AMPLITUDE and PHASE
    
    """

    # define time exis
    fs = 200.0 # frequence echantillonage
    t = np.arange(0, 2, 1/fs)

    # load data
    y = np.array(pd.read_csv(data_file)['y'])

    # FFT
    n = len(y)               # nombre d'échantillons
    yf = np.fft.rfft(y)      # FFT réelle (utile pour signaux réels)

    # Amplitude (spectre)
    amplitude = np.abs(yf) * 2 / n  # normalisation
    phase = np.angle(yf)            # phase optionnelle

    return {"FFT":yf, "AMPLITUDE":amplitude, "PHASE":phase}



if __name__ == "__main__":

    m = get_fourrier_transform("/tmp/freqtest/cell_22_freq.csv")
    print(m)

    
