# CS 340 Project Two README

## Grazioso Salvare Search-and-Rescue Dashboard

The Grazioso Salvare Dashboard is a full-stack application interfacing with the Austin Animal Center database to provide a web interface that allows the user to quickly locate suitable animals for training for search and rescue operations. In addition to browsing the raw data, interacting with the data table automatically updates a graph display and interactive map showing the animal’s precise location. 

## Motivation & Architecture

This user-friendly dashboard gives Grazioso Salvare staff access to this vital information without complicating access or exposing systems to unnecessary risks of data corruption or query execution error. The dashboard is pre-programmed with filters most useful for finding dogs suitable for training, simplifying the process. 

This project implements the Model-View-Controller structure:

* **Model:** MongoDB is utilized to house the raw data from which the system works. All data access is done through a hard-coded Python access script which eliminates all possibility of access errors.
* **View:** The web interface is built upon a foundation of Dash for displaying data tables and creating callbacks enabling interactivity on the page. Pandas DataFrames are used within the application logic to convert the raw data retrieved from the MongoDB into a format usable by the application.
* **Controller:** Utilizing callback functions from Dash, the application responds to user inputs such as page clicks. 

## Tools Used

* **MongoDB:** MongoDB serves as the database model. It features a JSON-like query structure and has deep integration within the Python ecosystem. Its data storage is a direct parallel with the extremely useful dictionary data structure in Python, making it a breeze to work with.
* **PyMongo:** MongoDB’s official Python integration library.
* **Dash:** Web application framework enabling responsive web application development without JavaScript.
* **Dash DataTable:** HTML/React table with client side pagination and view sorting.
* **Plotly Express:** Data visualization, used to display a histogram of dog breeds
* **Dash Leaflet:** Integrates Leaflet.js mapping directly into the Dash ecosystem, enabling real-time geolocation marker updates, interactive popups, and tooltips based on latitude and longitude coordinates. 
* **Pandas:** DataFrame objects facilitating the conversion of data between PyMongo and Dash formats. 

