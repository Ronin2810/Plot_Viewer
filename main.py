import streamlit as st
from PIL import Image

# Mapping each option to two corresponding plot file paths
options = ["Computational Tools","Dynamics, Kinematics and Vibrations","Electricity and Magnetism", "Engineering Economics", "Ethics and Professional Practice", "Fluid Mechanics", "Heat Transfer","Material Properties and Processing","Mathematics","Measurements, Instrumentation and Controls","Mechanical Design and Analysis","Probability and Statistics","Statics","Thermodynamics","Mechanics of Materials","Examinees Plot"]

plots = {
    "Computational Tools": ("./plots/Computational Tools_ratio_score.png", "./plots/Computational Tools_scaled_score.png"),
    
    "Dynamics, Kinematics and Vibrations": ("./plots/Dynamics and Kinematics_ratio_score.png", "./plots/Dynamics and Kinematics_scaled_score.png"),

    "Electricity and Magnetism": ("./plots/Electricity and Magnetism_ratio_score.png", "./plots/Electricity and Magnetism_scaled_score.png"),
    
    "Engineering Economics": ("./plots/Engineering Economics_ratio_score.png", "./plots/Engineering Economics_scaled_score.png"),
    
    "Ethics and Professional Practice": ("./plots/Ethics_ratio_score.png", "./plots/Ethics_scaled_score.png"),
    
    "Fluid Mechanics": ("./plots/Fluid Mechanics_ratio_score.png", "./plots/Fluid Mechanics_scaled_score.png"),
    
    "Heat Transfer": ("./plots/Heat Transfer_ratio_score.png", "./plots/Heat Transfer_scaled_score.png"),

    "Material Properties and Processing": ("./plots/Material and Process_ratio_score.png", "./plots/Material and Process_scaled_score.png"),

    "Mathematics": ("./plots/Mathematics_ratio_score.png", "./plots/Mathematics_scaled_score.png"),

    "Measurements, Instrumentation and Controls": ("./plots/Measurement and Control_ratio_score.png", "./plots/Measurement and Control_scaled_score.png"),
    
    "Mechanical Design and Analysis": ("./plots/Mechanical Design and Analysis_ratio_score.png", "./plots/Mechanical Design and Analysis_scaled_score.png"),
    
    "Probability and Statistics": ("./plots/Probability and Statistics_ratio_score.png", "./plots/Probability and Statistics_scaled_score.png"),
    
    "Statics": ("./plots/Statics_ratio_score.png", "./plots/Statics_scaled_score.png"),
    
    "Thermodynamics": ("./plots/Thermodynamics_ratio_score.png", "./plots/Thermodynamics_scaled_score.png"),
    
    "Mechanics of Materials": ("./plots/Mechanism of Materials_ratio_score.png", "./plots/Mechanism of Materials_scaled_score.png"),
    
    "Examinees Plot": ("./plots/examinees.png", "./plots/examinees_purdueme.png"),
}

# Streamlit app
st.title("ABET Plots Viewer")

# Dropdown menu to select an option
selected_option = st.selectbox("Select an option to view plots:", options)

# Display the corresponding plots
if selected_option and selected_option!="Examinees Plot":
    plot1_path, plot2_path = plots[selected_option]

    # Display the first plot
    st.subheader(f"Ratio Score for {selected_option}")
    image1 = Image.open(plot1_path)
    st.image(image1, use_container_width=True)
    
    # Display the second plot
    st.subheader(f"Scaled Score for {selected_option}")
    image2 = Image.open(plot2_path)
    st.image(image2, use_container_width=True)

elif selected_option and selected_option=="Examinees Plot":
    plot1_path, plot2_path = plots[selected_option]

    # Display the first plot
    st.subheader(f"ME Examinees (ABET) Plot")
    image1 = Image.open(plot1_path)
    st.image(image1, use_column_width=True)
    
    # Display the second plot
    st.subheader(f"Purdue ME Examinees (ABET) Plot")
    image2 = Image.open(plot2_path)
    st.image(image2, use_column_width=True)