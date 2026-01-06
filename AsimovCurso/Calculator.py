# Creating a English Calculator using Python AND Streamlit for my personal repository :)
import streamlit as st

# Project Title
st.title('🤖 Welcome to your inteligent calculator')

# Numeric input required
# User must enter a numeric value
num1 = st.number_input('Please complete with the first number', value=0.0)
num2 = st.number_input('Please complete with the second number', value=0.0)

# User must select an account type
# Account type selection required
operation = st.selectbox (
    'Select the account type you want',
    ("Addition", "Subtraction", "Multiplication", "Division")
)

# Calculator Bottons
if st.button('Calculate'):
    if operation == 'Addition':
        result = num1 + num2
    
    elif operation == 'Subtraction':
        result = num1 - num2

    elif operation == 'Multiplication':
        result = num1 * num2
    
    elif operation == 'Division':
        if num2 == 0:
            st.error('Error, this operation doesnt works when the divisor = 0')
            result = None
        else:
            num1 / num2


