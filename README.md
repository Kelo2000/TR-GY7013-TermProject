  
# 🚖An integrated matching and vehicle-rebalancing framework for ride-hailing services: a simulation using NYC taxi data

Ride-hailing services have revolutionized urban transportation by offering flexible, on-demand mobility, serving millions of trips monthly in cities like New York. These systems comprise two key components: ride matching, which assigns passengers to available vehicles, and vehicle rebalancing, which repositions idle vehicles to anticipate future demand. Traditionally treated as separate tasks, this project proposes an integrated optimization approach that jointly decides on matching and rebalancing, outperforming sequential methods by reducing vehicle miles traveled while maintaining high service quality. Using mixed-integer linear programming and real NYC trip data, our simulations demonstrate clear advantages in efficiency and performance.

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
