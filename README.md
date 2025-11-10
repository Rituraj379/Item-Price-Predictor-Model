# ML Challenge 2025: Smart Product Pricing Solution Template

**Team Name:** [The Overfitters]  
**Team Members:** [Amit Singh, Aniket Tripathi, Ansh Raj]  
**Submission Date:** [13/10/2025]

---

## 1. Executive Summary
*Our solution predicts product prices by fusing text and image data in a multimodal framework. We generate rich semantic embeddings from product descriptions using Word2Vec and combine them with deep visual features extracted from product images. This unified vector allows our gradient boosting model to capture a holistic product view, leading to more accurate price predictions.*



---

## 2. Methodology Overview

### 2.1 Problem Analysis
We approached the pricing challenge as a multimodal regression problem using both textual and visual features. During EDA, we cleaned the data by handling nulls, removing duplicates, splitting product details, and standardizing all quantities to kilograms and liters. Outliers above a price of 200 were removed, and skewed features (price, name length, word count, quantity) were log-transformed. Text data was tokenized, stemmed, and embedded using Word2Vec, while images were resized to 256×256 and encoded via a pretrained Vision Transformer with PCA-reduced 512-dim embeddings. These embeddings were merged by sample ID and used to train a LightGBM model for price prediction.

**Key Observations:**

### 2.2 Solution Strategy

**Approach Type:** Hybrid (Multimodal Single Model)  
**Core Innovation:** Integrated textual and visual modalities by generating Word2Vec embeddings (300 dimensions) for processed product descriptions and Vision Transformer (ViT) embeddings (768 dimensions, reduced to 512 via PCA) for image data. The fused feature vectors were trained using a LightGBM regressor, leveraging gradient boosting for efficient learning of nonlinear relationships between multimodal embeddings and product price, resulting in improved generalization and predictive accuracy.

---

## 3. Model Architecture

### 3.1 Architecture Overview

+--------------------------+        +--------------------------+
|      Text Data           |        |      Image Data          |
| (catalog_content)        |        |                          |
+--------------------------+        +--------------------------+
             |                                 |
             V                                 V
+--------------------------+        +--------------------------+
| 1. Data Cleaning         |        | 11. Image Preprocessing  |
| (Nulls, Duplicates)      |        | (Resize to 256x256)      |
+--------------------------+        +--------------------------+
             |                                 |
             V                                 V
+--------------------------+        +--------------------------+
| 2. Extract Product Details|       | 11. Vision Transformer   |
| (Name, Desc, Qty, Unit)  |        | (ViT) -> 768-dim         |
+--------------------------+        +--------------------------+
             |                                 |
             V                                 V
+--------------------------+        +--------------------------+
| 3. Remove Empty Desc Rows|        | 11. PCA Reduction        |
|     Description rows     |        | -> 512-dim Image Vector  |
|                          |        |                          |
+--------------------------+        +--------------------------+
             |                                  |
             V                                  |
+--------------------------+                    |
| 5. Create New Features   |                    |
| (Length, Uniqueness, desc|                    |
|  word count)             |                    |
+--------------------------+                    |
             |                                  |
             V                                  |
+--------------------------+                    |
| 6. Standardize Units     |                    |
| (oz -> kg, fl oz -> L)   |                    |
+--------------------------+                    |
             |                                  |
             V                                  |
+--------------------------+                    |
| 8. Outlier Removal       |                    |
| (Price > 200)            |                    |
+--------------------------+                    |
             |                                  |
             V                                  |
+--------------------------+                    |
| 9. Log Transform Skew Feat|                   |
| (price, qty, length)     |                    |
+--------------------------+                    |
             |                                  |
             V                                  |
+--------------------------+                    |
| 10. NLP Preprocessing &  |                    |
| Word2Vec -> Text Vector  |                    |
+--------------------------+                    |
             |                                  |
             +---------------+-----------------+
                             |
                             V
             +-------------------------------+
             | 13. Combine Embeddings & Price|
             | (Inner Join on sample_id)     |
             +-------------------------------+
                             |
                             V
             +-------------------------------+
             | 14. Train/Test Split Data     |
             +-------------------------------+
                             |
                             V
             +-------------------------------+
             | 14. Train LightGBM Model      |
             +-------------------------------+
                             |
                             V
             +-------------------------------+
             |        Predicted Price        |
             +-------------------------------+


### 3.2 Model Components

**Text Processing Pipeline:**
- [ ] Preprocessing steps: [Tokenization, stopword removal, stemming, lowercasing, text cleaning]
- [ ] Model type: - [Word2Vec embedding model of dimensions (74697, 205)]
- [ ] Key parameters: [Embedding dimension = 205, window size = 5, min count = 2]

**Image Processing Pipeline:**
- [ ] Preprocessing steps: [Resize images to 256×256, naming by sample ID] 
- [ ] Model type: [Pretrained Vision Transformer (ViT-B-16)]
- [ ] Key parameters: [Original embedding dimension = 768, PCA-reduced dimension = 512, pretrained weights used]


---


## 4. Model Performance

### 4.1 Validation Results
- **SMAPE Score:** [your best validation SMAPE]
- **Other Metrics:** [MAE, RMSE, R² if calculated]


## 5. Conclusion
We developed a multimodal pipeline combining Word2Vec text embeddings and Vision Transformer (ViT) image embeddings, which were fused and fed into a LightGBM regressor for price prediction. Careful data cleaning, unit standardization, and log-transforming skewed features improved model stability and performance. Key lessons include the effectiveness of feature fusion and multimodal representation learning for capturing complex relationships in product pricing.
---

## Appendix

### A. Code artefacts
drive link : https://drive.google.com/drive/folders/1bVclPqz3s-cyWovKkN8A-gJG39E6TDrN?usp=sharing


---

