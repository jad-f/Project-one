# Assessment – CNC Tool Wear Data and Introduction

This is repository follows the structure format that is required for **Data Science Toolbox** assessment by using data from Kaggle dataset source for **CNC Milling Machine Tool Wear Detection** 
Dataset source:[Tool W ear Detection in CNC Milling - Kaggle](https://www.kaggle.com/datasets/shasun/tool-wear-detection-in-cnc-milling).

------------------------------

## Project Author
**Fadia Jadan**  
Single-author submission.

---

## Reading order and requirements

All report content is stored in:

```
report/
```

The analysis uses only Python and Jupyter Notebook.

**Report structure**
1. `03-Python_Analysis.ipynb` — data loading, cleaning, visualisation, and clustering  
   - Generates summary statistics  
   - Builds a correlation heatmap to visualise relationships among variables  
   - Applies clustering (e.g., K-means or hierarchical) to group similar tool-wear patterns  
   - Interprets clusters in the context of machine condition monitoring

Rendered notebook output (`.html`) is included for reproducibility.

---

## Requirements

Python environment setup:
```bash
python -m venv .venv
source .venv/bin/activate     # or .venv\Scripts\activate on Windows
pip install -r requirements.txt
```
pandas
numpy
matplotlib
seaborn
scikit-learn
jupyter
**requirements.txt**
```
pandas
numpy
matplotlib
seaborn
scikit-learn
jupyter
```

---

## Evidence

All exploratory work, plots, and clustering steps are contained in  
```
report/03-Python_Analysis.ipynb
```

---

## Reflection

A short reflection on learning outcomes and process is located in:
```
reflection/Fadia_Reflection.md
```
or as a PDF if rendered with Pandoc:
```bash
pandoc -o Fadia_Reflection.pdf Fadia_Reflection.md
```

---

## Data

The raw dataset is hosted on Kaggle and is **not committed** to this repository to comply with GitHub storage guidelines.  
When running the notebook for the first time, download the dataset manually from Kaggle or use the Kaggle API:
```bash
kaggle datasets download -d shasun/tool-wear-detection-in-cnc-milling
```

Unzip into:
```
data/raw/
```

Processed or transformed data created during analysis will be written to:
```
data/processed/
```

---

## Comments on Repository Practice

- Only final outputs (`.ipynb` and rendered HTML) are committed.  
- Large or intermediate data files are excluded.  
- Binary data are avoided to keep the repository efficient.

---

## References
1. Kaggle. *Tool Wear Detection in CNC Milling* dataset. https://www.kaggle.com/datasets/shasun/tool-wear-detection-in-cnc-milling  
2. University of Bristol. *Data Science Toolbox – Example Assessment Repository*. https://github.com/dsbristol/dst_example_project

3. Scikit-learn documentation for PCA, KMeans, and silhouette analysis. https://scikit-learn.org/stable/modules/clustering.html
Thanks!
