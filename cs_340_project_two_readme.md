# Grazioso Salvare Search-and-Rescue Dashboard

**Course:** CS 340 Client/Server Development  
**Author:** Grant Gimer  
**Date:** October 16, 2026  

---

## Overview

The **Grazioso Salvare Dashboard** is a full-stack web application interfacing with the Austin Animal Center database. It provides an intuitive interface that allows users to quickly locate and identify suitable animals for training in search-and-rescue (SAR) operations. 

In addition to browsing the raw data, interacting with the data table automatically updates a dynamic chart display and an interactive map showing the selected animal's precise geolocation.

---

## Motivation & Architecture

This user-friendly dashboard gives Grazioso Salvare staff direct access to vital shelter data without complicating workflows or exposing internal systems to unnecessary risks of data corruption or query execution errors. The dashboard comes pre-configured with rescue-specific filters (Water Rescue, Mountain/Wilderness Rescue, and Disaster/Individual Tracking), streamlining the candidate selection process.

### Model-View-Controller (MVC) Pattern

This project strictly implements the **Model-View-Controller (MVC)** architectural design:

```
+-------------------------------------------------------+
|                        VIEW                           |
|       Dash Web UI (Data Table, Graph, Leaflet Map)    |
+--------------------------▲----------------------------+
                           | User Interaction / Callbacks
                           |
+--------------------------▼----------------------------+
|                     CONTROLLER                        |
|            Dash Callbacks & Pandas Logic              |
+--------------------------▲----------------------------+
                           | CRUD Queries / Data Stream
                           |
+--------------------------▼----------------------------+
|                        MODEL                          |
|         MongoDB (Austin Animal Center Dataset)        |
|             + Hard-coded Python CRUD Module           |
+-------------------------------------------------------+
```

* **Model:** MongoDB houses the raw shelter data. All database access and queries are executed through an encapsulated Python CRUD module, preventing malformed queries and eliminating direct access errors.
* **View:** The front-end interface is constructed with Dash components, featuring interactive data tables, Plotly Express charts, and an embedded Leaflet map. 
* **Controller:** Dash callback functions monitor user actions (such as filter selection or row clicking), invoke the Model layer, transform query results via Pandas DataFrames, and update the View in real time.

---

## Tools & Technologies

| Tool / Library | Role & Description |
| :--- | :--- |
| **MongoDB** | Document-oriented NoSQL database storing the raw animal shelter records in flexible, JSON-like BSON documents. |
| **PyMongo** | Official Python integration driver for MongoDB, facilitating query execution and CRUD operations. |
| **Dash (Plotly)** | Reactive Python web framework enabling dashboard construction without client-side JavaScript. |
| **Dash DataTable** | Interactive HTML/React table supporting pagination, column sorting, and row-level selection callbacks. |
| **Plotly Express** | Visualization engine used to generate the dynamic breed distribution charts. |
| **Dash Leaflet** | Leaflet.js wrapper providing interactive geolocation mapping, coordinate plotting, and dynamic markers. |
| **Pandas** | High-performance data manipulation library converting PyMongo query cursors into structured DataFrames for Dash. |

---

## Getting Started & Prerequisites

### Prerequisites

* **Python:** Version 3.8+
* **MongoDB Server:** Running locally (`localhost:27017`) or via a remote connection URI
* **Environment:** JupyterLab, Jupyter Notebook, or an IDE terminal (VS Code, PyCharm, Codio)

### Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/grazioso-salvare-dashboard.git
   cd grazioso-salvare-dashboard
   ```

2. **Create and activate a virtual environment (optional but recommended):**
   ```bash
   python -m venv venv
   source venv/bin/activate       # On macOS/Linux
   venv\Scripts\activate          # On Windows
   ```

3. **Install dependencies:**
   ```bash
   pip install pymongo pandas dash dash-leaflet plotly
   ```

4. **Ensure MongoDB is running:**
   ```bash
   mongod --dbpath /path/to/data/db
   ```

5. **Run the application:**
   ```bash
   python app.py
   # Or run all cells within the provided Jupyter Notebook (.ipynb)
   ```
   Open your browser and navigate to `http://127.0.0.1:8050/` (or the mapped Codio port).

---

## Screenshots & Workflow

### 1. Initial State / Reset Filter (Unfiltered)
Displays all records from the Austin Animal Center dataset with full pagination, unfiltered breed charts, and default map markers.

![Initial State / Reset Filter](screenshots/1_initial_state.png)

---

### 2. Water Rescue Filter Execution
Filters candidates specifically suited for water rescue operations (e.g., Labrador Retriever Mix).

![Water Rescue Filter](screenshots/2_water_rescue.png)

---

### 3. Mountain Rescue or Wilderness Rescue Filter Execution
Applies criteria to select high-endurance breeds suitable for rugged environments (e.g., German Shepherd, Alaskan Malamute, Siberian Husky, Rottweiler).

![Mountain or Wilderness Rescue Filter](screenshots/3_mountain_wilderness_rescue.png)

---

### 4. Disaster Rescue or Individual Tracking Filter Execution
Filters dogs exhibiting strong tracking and scent-detection characteristics (e.g., Bloodhound, German Shepherd, Rottweiler).

![Disaster Rescue or Individual Tracking Filter](screenshots/4_disaster_tracking.png)