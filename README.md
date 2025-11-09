# 🚖 Ride-Hailing Model Input Generator

This project prepares **epoch-based model input data** for the *Integrated Ride-Hailing Matching and Vehicle Rebalancing Model*.

Each epoch represents **one minute** of system state and contains the matrices and vectors used in the optimization process.

---

## ⚙️ Conda Environment Setup

### 1. Create Conda Environment
```bash
conda create -n tlc_data python=3.10 -y
conda activate tlc_data
```

### 2. Install Requirements
```bash
pip install -r requirements.txt
```

## Jupyter Notebook(Minimal requirements):
if you run directly on jupyter notebook, make sure to run this command
```
!pip install numpy pandas matplotlib
```

---

## 📂 Required Input Files

before running main loop code, you will have these files:

1. **(Optional)Trip data** (`fhvhv_tripdata_2025-07.csv.csv`)  
   Must include the following columns:
   ```
   request_datetime, pickup_datetime, dropoff_datetime,
   pulocationid, dolocationid,
   pu_x, pu_y, do_x, do_y
   ```
   Extract the file from [fhvhv_tripdata_2025-07.zip](fhvhv_tripdata_2025-07.zip)and make sure you put the file in the base path of the directory

2. **Filtered trip data** (`fhvhv_trips_reqtime_18to20_July1to8_2025.csv`)  
   Must include the following columns:
   ```
   request_datetime, pickup_datetime, dropoff_datetime,
   pulocationid, dolocationid,
   pu_x, pu_y, do_x, do_y
   ```

3. **Zone centroids** (`taxi_zones_toysample_TableToExcel_csv.csv`)  
   Must include the following columns:
   ```
   LocationID, centroid_x, centroid_y
   ```

4. **Precomputed Demand (φ) averages** (`phi_avg_15min.csv`)  
   Average future demand per zone and 15-minute time bin.  
   Columns:
   ```
   zone, time_bin_label, avg_requests
   ```

---

## ▶️ Running the Notebook


Open **[main.ipynb](main.ipynb)** and run The Main LOOP CELL(since required files have already been created).  
The notebook loads the filtered trips, computes distances, and creates an input to our model per minutes:

```python
epochs.append(dict(
    t=pd.to_datetime(t),
    request_batch=Rt.copy(),
    vehicles_snapshot=vehicles.copy(),
    idx_idle=idx_idle,
    idx_rebalancing=idx_rebal,
    c1=c1, c2=c2, c3=c3,
    phi=phi, gamma=gamma,
    impact=impact,
    zone_ids=zone_ids,
))
```


Each epoch contains:

| Key | Description |
|-----|--------------|
| `c1, c2, c3` | Distance cost matrices |
| `phi, gamma` | Demand & supply vectors |
| `impact` | 3D impact tensor |
| `idx_idle, idx_rebalancing` | Vehicle indices by state |
| `request_batch, vehicles_snapshot` | State snapshots for that minute |
