# summer26-water-use-sustainability
How will Phoenix's water supply be affected by climate change and upcoming data centers?

# Problem Definition

Many areas of the Southwest US are expected to face water shortages under climate change. At the same time, data centers are being built across this region, which could further put a strain on water availability. Using the city of Phoenix, AZ and the surrounding county (Maricopa county) as an example, we aim to forecast municipal water demand and supply in the near future. Phoenix receives most its municipal water from the Salt River Project, which manages a system of reservoirs on the Salt river and Verde river. We will model inflow into and outflow from these reservoirs as a function of various factors such as temperature, precipitation, population dependent on the reservoir for water, number of farms in the vicinity, number of data centers, etc. 

# Repository Structure

## [run.sh](run.sh)

Bash script for running all code files.

## [Code](Code)

This directory contains the Jupyter Notebooks used to preprocess climate datasets, perform data cleaning, select and evaluate models, and run predictive forecasting for both the Verde and Salt River systems.

### Directory Structure

The notebooks are numbered sequentially.:

#### 🔹 Phase 1: Data Ingestion & Preprocessing
* **`00_ClimateDataPreprocessing.ipynb`** — Downloads, filters and aggregates climate data (temperature and precipitation). 
* **`01_Data_Cleaning.ipynb`** — Standard baseline data engineering, missing-value handling, and variance-stabilization formatting (such as log transformations).
* **`02_Data_Cleaning_FutureValues_of_Features.ipynb`** — Data cleaning for future projected values of features.

#### 🔹 Phase 2: Modeling and Predictions
* **`Baselines/`** *(Folder)* — Contains code for baseline time series models.

    #### 🔹 Phase 2(a): Verde River Modeling and Predictions
    * **`03_verde_eda.ipynb`** — Some basic EDA for Verde River flow data.
    * **`04_verde_modeling.ipynb`** — Implements time series cross validation to compare Verde River flow models.
    * **`05_verde_final_results.ipynb`** — Final Verde River model training and evaluation.
    * **`06_verde_future_predictions.ipynb`** — Predicts future Verde River flow using our final models and climate projections.

    #### 🔹 Phase 2(b): Salt River Modeling and Predictions
    * **`07_salt_river_eda.ipynb`** — Som basic EDA for Salt River flow data
    * **`08_salt_river_modeling.ipynb`** — Implements time series cross validation to compare Salt river flow models. 
    * **`09_salt_river_future_predictions.ipynb`** — Predicts future Salt River flow using our final models and climate projections

#### 🔹 Phase 3: Confidence Intervals
* **`04_confidence_intervals.ipynb`** —
  
#### 🔹 Phase 4: Final plots
* **`12_Final_Plots.ipynb`** — Plots of our assorted data sets and model predictions.
## [Data](Data)

This directory contains the datasets used for our models. Data is separated into immutable raw data and cleaned, processed data.

### Directory Structure

* **`RawData/`**
  * *Description:* Contains unmodified data gathered directly from various sources.
  * *Policy:* These files are kept completely unmodified.
* **`FormattedData/`**
  * *Description:* Contains the cleaned and processed datasets used during model training and evaluation.
  * The final conglomerated data set we used for modeling is [Combined_Monthly_Data.csv](Data/FormattedData/Combined_Monthly_Data.csv)
  * *Key Modifications:* This folder hosts datasets that have undergone missing-value imputation, timeline synchronization, feature lag mapping (e.g., Lags 1, 5, 6, 11), and the critical $log(x+1)$ variance-stabilization transformations.

## [Output](Output)

This directory contains various outputs (graphs, model evaluation summaries, etc) generated throughout the data cleaning, EDA and model selection and evaluation processes.

## [Presentation](presentation)

This directory contains our final executive summary and our final presentation.

### Directory Structure

* **`Water Sustainability Presentation.pdf`** — Our final presentation.
* **`executive_summary.pdf`** — Our executive summary detailing data gathering and cleaning, model selection and evaluation, future predictions with confidence intervals, and limitations and recommendations of our project.
* **`final_presentation_recording.mp4`** — A recording of our final presentation.
