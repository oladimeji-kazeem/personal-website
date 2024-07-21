import streamlit as st
import pandas as pd
import altair as alt
from PIL import Image

# --- page setup ---
about_page = st.Page(
    page = "code/about.py",
    title = "About Me",
    icon = ":material/person:",
    default = True,
)
project_1_page = st.Page(
    page = "code/sales_dashboard.py",
    title = "Sales Dashboard",
    icon = ":material/sell:",
    default = True,
)
project_2_page = st.Page(
    page = "code/hr_dashboard.py",
    title = "HR Dashboard",
    icon = ":material/person_pin_circle:",
    default = True,
)

# Load Images
profile_image = Image.open("C:/Users/oladi/personal-website/personal-website/images/dimeji.jpg")
logo_image = Image.open("C:/Users/oladi/personal-website/personal-website/images/logo.jpg")  # Replace with actual path if different

# Sidebar
st.sidebar.image(logo_image, width=100)
st.sidebar.title("Info")
project_type = st.sidebar.selectbox("Select Project Type", ["About Me", "Data Analysis", "Predictions", "Chat Bot"])

# Main content
st.image(logo_image, width=100)
st.markdown("# CodingIsFun")
st.markdown("### Empowering enterprises with data-driven solutions")

# About Me Page
if project_type == "About Me":
    st.title("Ade Zyzhjgklh")
    st.image(profile_image, width=150)
    st.subheader("Senior Data Analyst, assisting enterprises by supporting data-driven decision-making.")
    
    st.write("### Experience & Qualifications")
    st.write("""
    - 7 Years experience extracting actionable insights from data
    - Strong hands-on experience and knowledge in Python and Excel
    - Good understanding of statistical principles and their respective applications
    - Excellent team-player and displaying a strong sense of initiative on tasks
    """)
    
    st.write("### Hard Skills")
    skills = {
        "PowerBi": 90,
        "MS Excel": 85,
        "Plotly": 80,
        "Python": 95,
        "Logistic regression": 85,
        "Linear regression": 80,
        "Decision trees": 75,
        "Postgres": 80,
        "MongoDB": 75,
        "MySQL": 70
    }
    skill_ratings = pd.DataFrame(list(skills.items()), columns=["Skill", "Rating (%)"])
    st.altair_chart(alt.Chart(skill_ratings).mark_bar().encode(
        x='Skill',
        y='Rating (%)',
        color='Skill'
    ).properties(width=600))
    
    st.write("### Soft Skills")
    st.write("""
    - Communication
    - Teamwork
    - Problem-solving
    - Time Management
    - Adaptability
    """)

# Data Analysis Dropdown
elif project_type == "Data Analysis":
    analysis_page = st.sidebar.selectbox("Select Analysis Dashboard", ["Sales Dashboard", "HR Dashboard", "Finance Dashboard"])

    if analysis_page == "Sales Dashboard":
        st.title("Sales Dashboard")
        st.write("Analysis by month and city.")
        
        data = {
            'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
            'Tokyo': [7000, 6500, 7000, 7500, 6800, 7100, 7200, 7400, 7000, 8000, 7500, 7000],
            'Yokohama': [6200, 6300, 6100, 6600, 6700, 6800, 7000, 7100, 6800, 7500, 7400, 7200],
            'Osaka': [7500, 7400, 7200, 7600, 7700, 8000, 8200, 8300, 8100, 8500, 8600, 8400]
        }
        df = pd.DataFrame(data)
        city = st.selectbox("Select a city", ['Tokyo', 'Yokohama', 'Osaka'])
        
        st.altair_chart(alt.Chart(df).mark_bar().encode(
            x='Month',
            y=city,
            color='Month'
        ).properties(width=600))
        
        st.write("### Data Story")
        st.write(f"""
        The sales dashboard provides insights into the monthly sales performance for three major cities: Tokyo, Yokohama, and Osaka. 
        In the selected city, {city}, we observe the following trends:
        
        - **January**: Sales start strong with a notable dip in February, likely due to seasonal effects.
        - **April**: A peak in sales, possibly driven by a marketing campaign or seasonal demand.
        - **October**: Another significant peak, indicating a recurring pattern that might be explored for targeted promotions.
        
        Understanding these patterns helps in forecasting and planning for future sales strategies.
        """)

    elif analysis_page == "HR Dashboard":
        st.title("HR Dashboard")
        st.write("HR analytics and employee insights coming soon.")
        
        st.write("### Data Story")
        st.write("""
        The HR Dashboard will provide comprehensive insights into employee metrics such as turnover rates, employee satisfaction, and performance metrics.
        These insights will be crucial for making informed decisions on recruitment, retention strategies, and overall workforce management.
        """)

    elif analysis_page == "Finance Dashboard":
        st.title("Finance Dashboard")
        st.write("Financial analysis and metrics coming soon.")
        
        st.write("### Data Story")
        st.write("""
        The Finance Dashboard will present key financial metrics including revenue, expenses, and profitability. 
        By analyzing these metrics, we can identify trends, monitor financial health, and make data-driven decisions to optimize financial performance.
        """)

# Predictions Dropdown
elif project_type == "Predictions":
    prediction_page = st.sidebar.selectbox("Select Prediction Model", ["Hepatitis Prediction", "Lung Cancer Prediction", "Diabetes Prediction"])

    if prediction_page == "Hepatitis Prediction":
        st.title("Hepatitis Prediction")
        st.write("Enter details for hepatitis prediction.")
        # Implement form and prediction logic
        
        st.write("### Data Story")
        st.write("""
        The Hepatitis Prediction model uses patient data to predict the likelihood of hepatitis. 
        Early prediction and diagnosis are crucial for effective treatment and management of the disease.
        By inputting patient details, we can provide a personalized risk assessment.
        """)

    elif prediction_page == "Lung Cancer Prediction":
        st.title("Lung Cancer Prediction")
        st.write("Enter details for lung cancer prediction.")
        # Implement form and prediction logic
        
        st.write("### Data Story")
        st.write("""
        The Lung Cancer Prediction model leverages patient data to predict the risk of lung cancer. 
        This tool aims to facilitate early detection and intervention, potentially improving patient outcomes and survival rates.
        By providing relevant details, users can receive an assessment of their lung cancer risk.
        """)

    elif prediction_page == "Diabetes Prediction":
        st.title("Diabetes Prediction")
        st.write("Enter details for diabetes prediction.")
        # Implement form and prediction logic
        
        st.write("### Data Story")
        st.write("""
        The Diabetes Prediction model analyzes patient data to estimate the risk of diabetes. 
        Early detection is key to managing diabetes and preventing complications. 
        Users can input their information to receive a personalized diabetes risk assessment.
        """)

# Chat Bot Page
elif project_type == "Chat Bot":
    st.title("Chatbot")
    st.write("Chat with the application owner.")
    if 'messages' not in st.session_state:
        st.session_state.messages = []
    
    user_input = st.text_input("You: ")
    if user_input:
        st.session_state.messages.append(f"You: {user_input}")
        st.session_state.messages.append(f"Bot: {get_bot_response(user_input)}")  # Placeholder for chatbot response function
    
    for message in st.session_state.messages:
        st.write(message)

# Placeholder for a function to get chatbot response
def get_bot_response(message):
    return "This is a placeholder response."
