import pandas as pd
import streamlit as st

# Set page title and header
st.markdown("<h1 style='text-align: center;'>LeapCode 踊</h1>", unsafe_allow_html=True)

# Add sidebar for language selection
with st.sidebar:
    language = st.radio("Select Programming Language:", ('C++', 'Python'))

# Load the appropriate database based on language selection
if language == 'C++':
    df = pd.read_csv('./Database/database.csv')
else:
    df = pd.read_csv('./Database/database_python.csv')

# Text input for serial number
k = st.text_input("Enter the serial number of the problem:")

# Display problem when serial number is entered
if k:
    try:
        k = int(k)
        # Find the index of the problem based on the serial number
        problem_index = list(df['Answer']).index(k)
        
        # Display the problem code
        st.code(df['Question'][problem_index], language=language.lower())
        
        # Celebratory balloons
        st.balloons()
    except ValueError:
        st.error("Invalid serial number. Please enter a valid number.")
    except Exception as e:
        st.error(f"An error occurred: {e}")
