 Smart Product Pricing Solution Template
 
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

# 🛒 Product Price Prediction Architecture Overview

This document outlines the data processing and modeling pipeline for predicting product prices using both text and image data.

---

## 🏗️ Architecture Flow Diagram

The process begins with two parallel data streams: **Text Data (catalog_content)** and **Image Data**.

### **I. Text Data Stream (Catalog Content)**

| Step | Process | Description |
| :---: | :--- | :--- |
| **1** | **Data Cleaning** | Handle **Nulls** and **Duplicates** in the raw text data. |
| **2** | **Extract Product Details** | Parse text to extract structured details: **Name**, **Description**, **Quantity (Qty)**, and **Unit**. |
| **3** | **Remove Empty Desc Rows**| Filter out rows where the product **Description** is missing or empty. |
| **5** | **Create New Features** | Engineer features based on description: **Length**, **Uniqueness** score, and **Description Word Count**. |
| **6** | **Standardize Units** | Convert disparate units to a standard format (e.g., **oz $\rightarrow$ kg**, **fl oz $\rightarrow$ L**). |
| **8** | **Outlier Removal** | Clean numerical data by removing extreme outliers (e.g., **Price > 200**). |
| **9** | **Log Transform Skewed Features** | Apply a **Log Transformation** to normalize highly skewed numerical features (**price**, **qty**, **length**). |
| **10** | **NLP Preprocessing & Vectorization** | Perform standard NLP tasks and convert text to a numerical **Text Vector** using **Word2Vec**. |

### **II. Image Data Stream**

| Step | Process | Description |
| :---: | :--- | :--- |
| **11.i**| **Image Preprocessing** | Standardize images by **Resizing to 256x256** pixels. |
| **11.ii**| **Vision Transformer (ViT)** | Pass preprocessed images through a **ViT** model to generate a **768-dimensional** feature vector. |
| **11.iii**| **PCA Reduction** | Apply **Principal Component Analysis (PCA)** to reduce the vector dimension to a **512-dimensional Image Vector**. |

---

## 🧠 Model Training Pipeline

| Step | Process | Description |
| :---: | :--- | :--- |
| **13** | **Combine Embeddings & Price** | Perform an **Inner Join** on the common identifier (`sample_id`) to merge the **Text Vector** and the **Image Vector** with the target **Price**. |
| **14.i**| **Train/Test Split Data** | Divide the combined, preprocessed dataset into **training** and **testing** sets. |
| **14.ii**| **Train LightGBM Model** | Train the final predictive model, **LightGBM**, using the combined feature set. |
| **Output**| **Predicted Price** | The final output of the trained model. |


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

