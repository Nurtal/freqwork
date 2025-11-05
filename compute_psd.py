import pandas as pd
import numpy as np
from scipy.interpolate import interp1d
from scipy.signal import welch
import matplotlib.pyplot as plt



def compute_psd(frequency_file:str):
    """Compute and return power spectral density
    
    Args:
        - frequency_file (str) : file storing the signal

    Returns:
        - (tuple) :
            - freqs : C’est un vecteur contenant les fréquences analysées (les composantes fréquentielles du signal)
            - Pxx : C’est le Power Spectral Density (PSD), c’est-à-dire la densité de puissance du signal à chaque fréquence.
    
    """

    # load data
    df = pd.read_csv(frequency_file)
    x = df['x']
    y = df['y']

    # Interpolation sur une grille régulière
    x_uniform = np.linspace(x.min(), x.max(), 512)
    interp_func = interp1d(x, y, kind='cubic', fill_value="extrapolate")
    y_uniform = interp_func(x_uniform)

    # Calcul de la densité spectrale de puissance (PSD)
    freqs, Pxx = welch(y_uniform, fs=1.0/(x_uniform[1]-x_uniform[0]), nperseg=256)

    return (freqs, Pxx)

def plot_psd(freqs, Pxx, savefile):
    """Plot PSD"""

    plt.figure(figsize=(10,4))
    plt.semilogy(freqs, Pxx)
    plt.title("Densité spectrale de puissance (PSD)")
    plt.xlabel("Fréquence"); plt.ylabel("Puissance (log)")
    plt.tight_layout()
    plt.savefig(savefile)
    plt.close()


def spectral_embedding(freqs, Pxx, fc=None):
    """
    Calcule un petit embedding (vecteur de features) à partir d'une densité spectrale de puissance.
    
    Paramètres
    ----------
    freqs : array-like
        Fréquences correspondantes à la PSD (mêmes dimensions que Pxx).
    Pxx : array-like
        Densité spectrale de puissance (Power Spectral Density).
    fc : float ou None
        Fréquence de coupure pour séparer basse/haute fréquence. 
        Si None, on prend fc = fréquence médiane.

    Retour
    ------
    features : dict
        Dictionnaire contenant plusieurs descripteurs :
        - power_total : puissance totale (aire sous la PSD)
        - power_low / power_high : fraction basse vs haute fréquence
        - spectral_centroid : fréquence moyenne pondérée par la puissance
        - spectral_entropy : entropie normalisée du spectre
        - spectral_slope : pente de la PSD (linéaire sur log-échelle)
    """

    freqs = np.asarray(freqs)
    Pxx = np.asarray(Pxx)

    # Nettoyage des valeurs
    Pxx = np.maximum(Pxx, 1e-12)
    power_total = np.trapz(Pxx, freqs)

    # Normalisation pour certaines métriques
    Pxx_norm = Pxx / np.trapz(Pxx, freqs)

    # Fréquence de coupure (mi-fréquence si non spécifiée)
    if fc is None:
        fc = np.median(freqs)

    low_mask = freqs < fc
    high_mask = freqs >= fc

    power_low = np.trapz(Pxx[low_mask], freqs[low_mask]) / power_total
    power_high = np.trapz(Pxx[high_mask], freqs[high_mask]) / power_total

    # Centroid fréquentiel
    spectral_centroid = np.trapz(freqs * Pxx_norm, freqs)

    # Entropie spectrale (Shannon)
    Pxx_norm_safe = Pxx_norm / np.sum(Pxx_norm)
    spectral_entropy = -np.sum(Pxx_norm_safe * np.log2(Pxx_norm_safe + 1e-12))
    spectral_entropy /= np.log2(len(Pxx_norm_safe))  # normalisée 0–1

    # Pente spectrale (approximation linéaire sur log-log)
    log_f = np.log10(freqs[freqs > 0])
    log_P = np.log10(Pxx[freqs > 0])
    spectral_slope, _ = np.polyfit(log_f, log_P, 1)

    features = {
        "power_total": power_total,
        "power_low": power_low,
        "power_high": power_high,
        "spectral_centroid": spectral_centroid,
        "spectral_entropy": spectral_entropy,
        "spectral_slope": spectral_slope,
    }

    return features



if __name__ == "__main__":

    freqs, Pxx = compute_psd("/tmp/freqtest/cell_52_freq.csv")
    plot_psd(freqs, Pxx, "/tmp/test.png")
    m = spectral_embedding(freqs, Pxx)    
    print(m)
    
