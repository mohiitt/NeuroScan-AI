# Machine Learning for Alzheimer's Disease Detection from Brain MRI

**Exposing Cognitive Test Dependency and Enhancing Clinical Accuracy with Structural Imaging Biomarkers**

**By:** Jainil Rana, Mansi Gupta, Mohit Manoj Barade  
**Course:** CMPE-257 Machine Learning | San Jose State University | Spring 2026

**Live Application Dashboard:** [https://alzheimer-detection-xi.vercel.app](https://alzheimer-detection-xi.vercel.app)

---

## 📌 Problem Description & Motivation
Alzheimer's Disease (AD) affects over 55 million people globally, with early detection being the primary clinical lever for intervention. Structural changes in the brain—such as hippocampal atrophy, cortical thinning, and ventricular enlargement—begin years before noticeable clinical symptoms emerge. Modern T1-weighted MRI scans can capture these early changes.

Existing machine learning studies on the OASIS-1 dataset routinely report 85–90% accuracy using tabular clinical features. However, our study demonstrates that such accuracy is largely an artifact of **circular reasoning**: the dominant predictor is often the Mini-Mental State Examination (MMSE), a direct cognitive measure of the very outcome being predicted. A model predicting dementia primarily from MMSE offers no independent diagnostic value and fails in preclinical cases where MMSE remains normal.

This project addresses this flaw through a rigorous two-phase empirical study: diagnosing the dependency via feature ablation, and correcting it by extracting 104 region-specific structural biomarkers directly from raw MRI scans.

---

## 📊 Dataset Analysis
**OASIS-1:** Open Access Series of Imaging Studies ([Link](https://www.oasis-brains.org/))

- **Subjects:** 416 individuals (cross-sectional)
- **Age Range:** 18–96 years
- **Target Variable:** Clinical Dementia Rating (CDR) binarized to 0 (Healthy) and 1 (Dementia)
- **Data Modalities:**
  - **Tabular Clinical Data:** Demographics (Age, Gender, Education, Socioeconomic Status), cognitive test scores (MMSE), and gross volume measures (eTIV, nWBV, ASF).
  - **Neuroimaging Data:** Structural T1-weighted MRI scans.

---

## ⚙️ Methodology & Two-Phase Pipeline

### Phase 1: Tabular Baseline & Feature Ablation (The MMSE Red Flag)
- **Modeling:** Trained 8 diverse classifiers (Logistic Regression, SVM, Random Forest, XGBoost, etc.) on 8 clinical tabular features using 5-fold stratified cross-validation.
- **Results:** XGBoost achieved **86.9% accuracy** (LogReg achieved 88.10%). However, performance clustered narrowly across all models.
- **The Diagnosis:** Feature importance revealed **MMSE accounted for 37.8%–61.7%** of predictive power. 
- **Ablation Study:** Removing 7 out of 8 features and training **only on MMSE** perfectly matched the full 8-feature baseline accuracy. Phase 1 models were essentially "MMSE classifiers in disguise".

### Phase 2: Enhanced MRI Feature Extraction & Structural Biomarkers
To replace global scalars with localized neuroanatomical fingerprints, we developed an extensive MRI processing pipeline:
- **Tissue Segmentation (FSL FAST):** Processed 400+ MRIs to extract 57 tissue-level features (Gray Matter, White Matter, Cerebrospinal Fluid volumes and ratios). Total compute time ~14 hours.
- **Atlas Registration (Talairach):** Extracted 47 regional metrics covering 5 key bilateral regions:
  - **Hippocampus** (earliest specific biomarker)
  - **Lateral Ventricles** (compensatory expansion)
  - **Entorhinal Cortex** (origin site of tangles)
  - **Inferior & Middle Temporal Gyrus**
- **Enhanced Integration:** Merged 104 structural imaging features with clinical data (116 total features).

---

## 🚀 Key Results & Clinical Validation

1. **Accuracy Improvement:** The enhanced XGBoost model achieved **90.5% accuracy**, outperforming the tabular baseline.
2. **Breaking the MMSE Dependency:** 
   - The importance of MMSE dropped from 37.8% (Phase 1) to just **9.1%** (Phase 2) — a **76% relative reduction**.
   - The model distributed its decision across 15+ anatomical features rather than relying on 3 global metrics.
3. **Ablation & Imaging-Only Performance:**
   - **Without MMSE:** Maintained **85.7% accuracy** (compared to 81.0% in Phase 1 without MMSE).
   - **Imaging-Only (No Cognitive Tests):** Achieved **84.5% accuracy** relying strictly on structural brain measurements and basic demographics, proving the viability of preclinical anatomical diagnosis.
4. **Clinical Validation:** Extracted biomarkers tracked perfectly with known AD pathology (e.g., Hippocampal volume dropped 27% and Ventricular volume increased 52% in mild dementia patients).

---

## 📁 Project Structure

The codebase is organized into modular scripts for end-to-end execution:
- `src/` - Core Python modules for preprocessing (`preprocessor.py`), model definitions (`models.py`), and imaging feature extraction (`imaging/`).
- `scripts/` - Execution pipelines:
  - `train_all_models.py` - Runs Phase 1 baseline training.
  - `run_full_oasis1_pipeline.py` - Parses 400+ session MRIs, merges with clinical data, and validates clinical plausibility.
  - `train_phase2_enhanced.py` - Runs the Phase 2 training suite and ablation studies.
  - `ablation_study.py` & `evaluate_all_models.py` - Evaluation utilities.
- `models/` - Saved model artifacts for Phase 1 and Phase 2 variations (Full, No-MMSE, Imaging-Only).
- `webapp/` - Web dashboard for the NeuroScan AI application.

---

## ⚠️ Challenges Addressed
- **Clinical Data Issues:** Handled missing values (e.g., 43% missing CDR assumed healthy per OASIS guidelines), class imbalance (imputed median/mode, used stratified sampling).
- **Computation Overhead:** FSL FAST segmentation is highly resource-intensive (~14 hours for the dataset), highlighting the complexity of MRI preprocessing.
- **High Dimensionality:** Expanding from 8 to 116 features on 416 samples required robust models like Gradient Boosting to resist the curse of dimensionality, while distance-based models (KNN, SVM) struggled.

---

## 🔮 Limitations and Future Work
- **Longitudinal Data:** Cross-sectional data cannot model atrophy rates. Future work will apply this pipeline to longitudinal datasets (OASIS-2, OASIS-3, ADNI).
- **Deep Learning:** Exploring 3D CNNs and Vision Transformers to bypass manual feature extraction and capture multi-scale, sub-visual textures.
- **Improved Parcellation:** Moving from Talairach bounding boxes to precise subject-specific surface reconstruction via FreeSurfer for higher measurement accuracy.
- **Clinical Deployment:** Developing calibrated probability bounds and using interpretability tools (SHAP) to ensure reliability for doctors triaging cases.

---

## 👥 Team Contributions
- **Mansi Gupta:** Data handling, preprocessing, Phase 2 data integration, missing value imputation, FSL FAST output parsing, and quality control validation.
- **Mohit Manoj Barade:** Model implementation and training (both phases), Phase 2 ablation scenario design (full, no-MMSE, imaging-only), training pipeline scripts, and serialization.
- **Jainil Rana:** Evaluation and analysis, metric computation, feature importance analysis, ablation study design and interpretation, clinical validation of biomarkers, and presentation.

---

## 📚 References
- Marcus, D. S., et al., “Open Access Series of Imaging Studies (OASIS): Cross-sectional MRI Data in Young, Middle Aged, Nondemented, and Demented Older Adults,” *Journal of Cognitive Neuroscience*, 2007.
- Zhang, Y., et al., "Segmentation of Brain MR Images Through a Hidden Markov Random Field Model and the Expectation-Maximization Algorithm," *IEEE Transactions on Medical Imaging*, 2001.
- OASIS Brain Project. [https://www.oasis-brains.org/](https://www.oasis-brains.org/)
