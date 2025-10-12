# 🧬 Frequency-domain representations of single-cell data  
## Reveal distinct information patterns compared to the raw expression space  

---

## 1. Introduction

- **Context**
  - The rapid expansion of single-cell technologies (scRNA-seq, spatial omics, etc.) has provided unprecedented resolution of cellular heterogeneity.  
  - However, the *representation space* used to describe these data strongly influences the patterns and biological signals that can be extracted.  

- **Problem**
  - Most analyses are performed in the raw expression space or after linear/non-linear dimensionality reduction (e.g., PCA, UMAP).  
  - Frequency-domain representations, widely used in physics and signal processing, offer an alternative way to represent complex signals.  

- **Objective**
  - Demonstrate that projecting single-cell data into the frequency domain modifies the nature of the information that can be extracted.  
  - Compare the information content and structure between raw expression space and frequency-domain representations.  

---

## 2. Methods

### 2.1 Dataset
- Public single-cell RNA-seq dataset (e.g., PBMC, Tabula Muris, or similar).  
- Standard preprocessing: normalization, log-transformation, feature selection.  

### 2.2 Frequency projection
- Convert each cell (vector of gene expressions) into a **signal**.  
- Order genes along a 1D axis according to:
  - Gene–gene interaction network,  
  - Correlation or pathway proximity.  
- Apply **frequency transformation** (e.g., FFT, STFT, or scattering transform).  
- Normalize frequency spectra across cells.

### 2.3 Comparative analysis
- Apply the same analytical pipelines in both spaces:
  - Clustering (e.g., Leiden, K-means)
  - Dimensional reduction (PCA, UMAP)
  - Classification (Random Forest, SVM, or simple neural net)
- Compare:
  - Cluster stability and biological annotation
  - Variance explained, entropy, and mutual information
  - Correlation with known biological features (cell type, state, etc.)

---

## 3. Results

- **Visualization**
  - 2D projections (UMAP/t-SNE) in both expression and frequency spaces.  
  - Example spectra for representative cells.  
- **Quantitative comparison**
  - Variance explained and information-theoretic metrics.  
  - Differences in clustering accuracy or biological relevance.  
- **Biological interpretation**
  - Highlight biological processes or pathways better captured in one space vs the other.  

---

## 4. Discussion

- **Interpretation of differences**
  - Raw expression space emphasizes local gene-level variation.  
  - Frequency space emphasizes global structural patterns and periodicity.  
- **Complementarity**
  - The two representations capture *different layers* of biological information.  
  - Combining both could yield richer insights (multi-view integration).  
- **Limitations**
  - Parameter sensitivity in the frequency transformation.  
  - Reduced interpretability of individual frequency components.  
- **Future directions**
  - Integrating temporal or spatial omics.  
  - Exploring other transforms (wavelets, Hilbert-Huang, scattering nets).  

---

## 5. Conclusion

- Frequency-domain representation fundamentally alters the information content derived from single-cell data.  
- These representations do not reproduce the raw expression results but reveal complementary, and sometimes hidden, biological structures.  
- This approach opens new perspectives for signal-based interpretation of omics data.  

---

## 6. Supplementary / Figures (suggested)

| Figure | Description |
|--------|--------------|
| Fig. 1 | Workflow overview: raw data → frequency projection |
| Fig. 2 | Comparison of 2D projections (UMAP) in both spaces |
| Fig. 3 | Example frequency spectra for two distinct cell types |
| Fig. 4 | Variance and information metrics comparison |
| Fig. 5 | Biological interpretation of discovered patterns |
