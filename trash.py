import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from scipy.fft import fft
import matplotlib.pyplot as plt

np.random.seed(42)

# Paramètres
n_samples = 400
n_genes = 64
t = np.linspace(0, 2*np.pi, n_genes)

# --- Classe 1 : basse fréquence avec phase aléatoire ---
class1 = []
for _ in range(n_samples//2):
    phase = np.random.rand() * 2*np.pi
    signal = np.sin(1 * t + phase) + 0.3*np.random.randn(n_genes)
    class1.append(signal)

# --- Classe 2 : haute fréquence avec phase aléatoire ---
class2 = []
for _ in range(n_samples//2):
    phase = np.random.rand() * 2*np.pi
    signal = np.sin(6 * t + phase) + 0.3*np.random.randn(n_genes)
    class2.append(signal)

# Dataset
X = np.vstack([class1, class2])
y = np.array([0]*(n_samples//2) + [1]*(n_samples//2))

# Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, stratify=y, random_state=42)

# --- Classif brut ---
clf_raw = LogisticRegression(max_iter=2000)
clf_raw.fit(X_train, y_train)
acc_raw = accuracy_score(y_test, clf_raw.predict(X_test))

# --- Classif fréquentiel ---
X_train_freq = np.abs(fft(X_train))[:, 1:n_genes//2]
X_test_freq  = np.abs(fft(X_test))[:, 1:n_genes//2]

clf_freq = LogisticRegression(max_iter=2000)
clf_freq.fit(X_train_freq, y_train)
acc_freq = accuracy_score(y_test, clf_freq.predict(X_test_freq))

print("Précision en espace brut :", acc_raw)
print("Précision en espace fréquentiel :", acc_freq)

# --- Visualisation spectres moyens ---
freqs = np.arange(1, n_genes//2)
plt.figure(figsize=(10,4))
plt.plot(freqs, X_train_freq[y_train==0].mean(axis=0), label="Classe 1 (basse fréquence)")
plt.plot(freqs, X_train_freq[y_train==1].mean(axis=0), label="Classe 2 (haute fréquence)")
plt.legend()
plt.title("Spectres moyens (différence claire en fréquences)")
plt.xlabel("Fréquence")
plt.ylabel("Amplitude")
plt.show()
