# 🚖 Ride-Hailing Model: Preprocessing and Integrated Matching/Rebalancing

This project implements a complete ride-hailing simulation system, including data preprocessing, model input generation, and optimization models for integrated matching and vehicle rebalancing.

The system processes trip data to generate **epoch-based model inputs** for the *Integrated Ride-Hailing Matching and Vehicle Rebalancing Model*. Each epoch represents **one minute** of system state and contains the matrices and vectors used in the optimization process.

---

## ⚙️ Environment Setup

### 1. Create Conda Environment
```bash
conda create -n rh_model python=3.10 -y
conda activate rh_model
```

### 2. Install Requirements
```bash
pip install -r requirements.txt
```

**Minimal requirements:**
```
pandas>=2.0
numpy>=1.24
jupyterlab>=4.0
gurobipy>=10.0
matplotlib>=3.7
```

---

## 📂 Required Input Files

Place these files in the same directory as the notebooks:

1. **Raw trip data** (`fhvhv_tripdata_2025-07.csv`)  
   Original FHvHV trip data with timestamps and locations.

2. **Zone centroids** (`taxi_zones_toysample_TableToExcel_csv.csv`)  
   Must include the following columns:
   ```
   LocationID, centroid_x, centroid_y
   ```

---

## 📋 Project Structure

### 1. **Preprocessing** (`preprocessing.ipynb`)
This notebook handles data preparation and feature engineering:

- **Data Loading & Filtering**: Loads raw trip data and filters trips within selected zones.
- **Noise Addition**: Adds Gaussian jitter to pickup/dropoff coordinates for realism.
- **Time-Based Filtering**: Separates training (July 7-11, 18:00-20:00) and test data (July 14, 18:00-20:00).
- **Demand Computation**: Calculates average demand (φ) per zone and 15-minute time bins.
- **Validation**: Checks trip distributions and ensures no missing minutes.

**Outputs:**
- `filtered_fhvhv_trips.csv`: Filtered trips within zones.
- `filtered_fhvhv_trips_with_jitter.csv`: Trips with added coordinate noise.
- `phi_avg_15min_Jul7to11_18to20.csv`: Precomputed demand averages.
- `test_trips_Jul14_18to20.csv`: Test dataset for simulation.

### 2. **Model Implementation** (`FINAL_MAIN_CODE.ipynb`)
This notebook contains the core optimization models and simulation:

- **Integrated (Joint) Model**: Simultaneous matching and rebalancing optimization.
- **Sequential Benchmark Model**: Separate matching then rebalancing phases.
- **Simulation Loop**: Per-minute epoch processing with vehicle state updates.
- **Sensitivity Analysis**: Parameter sweeps for fleet size, penalty, alpha, and time horizons.

**Key Components:**
- **Vehicle Dynamics**: Tracks idle, en-route, on-trip, and rebalancing states.
- **Cost Matrices**: Distance calculations between vehicles, requests, and zones.
- **Impact Tensor**: Models supply-demand balance effects.
- **Gurobi Optimization**: Solves assignment problems with imbalance penalties.

**Outputs:**
- Performance metrics: served/unserved requests, VMT, solver runtime.
- Comparative analysis between joint and sequential approaches.

---

## ▶️ Running the Notebooks

Launch Jupyter:
```bash
jupyter lab
```

### Step 1: Run Preprocessing
Open **`preprocessing.ipynb`** and execute all cells to prepare the data.

### Step 2: Run Model Simulation
Open **`FINAL_MAIN_CODE.ipynb`** and run the cells to execute the models and sensitivity analysis.


✅ **Complete Workflow:**  
1. Run preprocessing to generate clean datasets and demand estimates.  
2. Execute the main code to simulate and optimize ride-hailing operations.  
3. Analyze results for insights into matching efficiency and rebalancing benefits.
