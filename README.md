# Laptop Price Prediction 
A machine learning web application that predicts the price of laptops based on various features such as brand, processor type, RAM, storage, graphics card, screen size, and more.


Try it out : <a href="https://laptop-price-predictor-ys.streamlit.app/" target="_blank">Live</a>


<hr>

## Table of Contents
- Introduction
- Features
- Dataset Description
- Technologies Used
- Installation
- Usage
- Results
- Demo

<hr>

## 1. Introduction
The Laptop Price Prediction project utilizes a regression model trained on laptop data to predict their market price. This tool is designed for both sellers and buyers, helping them make informed decisions based on features like brand, specifications, performance, graphics card, screen size, and more.

<hr>

## 2. Features
- 💻 Predicts the price of a laptop based on input features such as brand, specifications, and performance.
- 🌐 Interactive and user-friendly interface built with Streamlit.

<hr>

## 3. Dataset Description
The dataset used includes the following columns:

- **Laptop Name**: The unique identifier or model name of the laptop.
- **Brand**: Laptop brand.
- **Model**: Specific model name.
- **Type**: Type of laptop (Ultrabook, Notebook, etc.).
- **Screen Size**: Screen size in inches.
- **RAM (Random Access Memory)**: The amount of RAM available for multitasking.
- **Operating System (OS)**: The type of operating system installed.
- **Weight**: Laptop weight in kg.
- **Price (Euros)**: The cost of the laptop in Euros.
- **Screen Type**: Type of screen display.
- **Screen Features**: Features such as Touchscreen, IPS panel, Retina display.
- **CPU (Central Processing Unit)**: The processor brand, model, and frequency.
- **GPU (Graphics Processing Unit)**: The graphics card brand and model.
- **Primary Storage**: Storage capacity and type (HDD, SSD, etc.).
- **Secondary Storage**: Additional storage capacity and type.

<hr>

## 4. Technologies Used
#### Programming Language: 
- Python
#### Frameworks and Libraries:
- Streamlit (for the web interface)
- Scikit-learn (for machine learning models)
- NumPy and Pandas (for data manipulation)
- Matplotlib and Seaborn (for visualizations)

<hr>

## 5. Installation
#### Follow these steps to set up the project locally:

1. Clone the repository:<br>
**command:** <code>git clone https://github.com/yashsahu02/Laptop_Price_Prediction.git</code>

2. Navigate to the project directory:<br>

3. Install the dependencies:<br>
**command:** <code>pip install -r requirements.txt</code>

## 6. Usage
#### Run the application:
- **command:** <code>streamlit run app.py</code><br>
Here app.py is name of python file.
#### Use the web interface to:
- Manually input laptop details (e.g., brand, processor, RAM, storage, etc.).
- View the predicted price of the laptop.

<hr>

## 7. Results
- The **RandomForestRegressor** achieved the highest performance as compared to other algorithms.
#### Model Performance:
- **R2 Score**:0.87
- **Mean Absolute Error**:170.10
- **Mean Squared Error**:65143.43
- **Root Mean Squared Error**:255.23

<hr>

## 8. Demo

<!--
- Watch the full project demo:

**Demo Video**


<br>
-->

**Screenshots**

![Image](https://github.com/user-attachments/assets/9b9507cd-475c-492d-bf07-a5ac079a9427)

<br>

![Image](https://github.com/user-attachments/assets/167e7b6c-a67d-48b8-8db3-e65947fb42d2)

<br>

![Image](https://github.com/user-attachments/assets/2a846be1-fe45-4b5d-9ef5-e12387cc811d)

**About Page**
![Image](https://github.com/user-attachments/assets/d8c1f7f6-0970-451d-b4c9-07ec15fc4b73)
![Image](https://github.com/user-attachments/assets/f8ccb336-8209-4cbb-a3b9-47261ed64ca2)

<br>
<br>

#### Prediction (Predicted Price)
<!--
screen shot 2
-->
