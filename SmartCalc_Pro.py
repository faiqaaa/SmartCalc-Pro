import streamlit as st
import math
import time
from datetime import datetime

# Adding a background picture and button styles
st.markdown(
    """
    <style>
    .main {
        background-image: url('https://www.pinterest.com/pin/1089800809819106014/');
        background-size: cover;
        background-position: center;
    }
    button {
        background-color: #FF6347;
        color: white;
        border-radius: 10px;
        font-size: 20px;
        padding: 10px;
        transition: transform 0.3s;
    }
    button:hover {
        transform: scale(1.1);
        background-color: #FF4500;
    }
    input {
        padding: 10px;
        font-size: 18px;
        border-radius: 8px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Title at the top
st.markdown("<h1 style='text-align: center; color: lightblue;'>SmartCalc Pro</h1>", unsafe_allow_html=True)

# Side time display
st.sidebar.markdown("<h2 style='color: orange;'>Current Time</h2>", unsafe_allow_html=True)
st.sidebar.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

# Calculator Section in the center
st.markdown("<h2 style='text-align: center; color: pink;'>Calculator</h2>", unsafe_allow_html=True)
option = st.selectbox("Select Operation", ["Addition", "Subtraction", "Multiplication", "Division", "Sin", "Cos", "Tan", "Logarithm", "Power"], key='calc_option')

num1 = st.number_input("Enter first number", value=0.0, key='num1')
num2 = st.number_input("Enter second number", value=0.0, key='num2')

start_time = time.time()

# Button with animation and calculation
if st.button("Run", key='calc', help="Click to calculate!", use_container_width=True):
    result = None
    if option == "Addition":
        result = num1 + num2
    elif option == "Subtraction":
        result = num1 - num2
    elif option == "Multiplication":
        result = num1 * num2
    elif option == "Division":
        result = num1 / num2 if num2 != 0 else "Error (Division by zero)"
    elif option == "Sin":
        result = math.sin(num1)
    elif option == "Cos":
        result = math.cos(num1)
    elif option == "Tan":
        result = math.tan(num1)
    elif option == "Logarithm":
        result = math.log(num1) if num1 > 0 else "Error (Invalid input)"
    elif option == "Power":
        result = math.pow(num1, num2)

    # Runtime limit of 5 seconds
    if time.time() - start_time > 5:
        st.error("Operation took too long!")
    else:
        st.success(f"Result: {result}")

        # Celebration animation when answer is displayed
        st.balloons()

# Gaming Section on the right
st.markdown("<h2 style='text-align: center; color: lightgreen;'>Gaming Zone</h2>", unsafe_allow_html=True)
game_option = st.selectbox("Select a Game", ["Number Guessing", "Tic-Tac-Toe"], key='game_option')

if game_option == "Number Guessing":
    st.write("Guess a number between 1 and 100!")
    guess = st.number_input("Your Guess:", min_value=1, max_value=100, key='guess')
    number = 42  # Secret number for simplicity
    if st.button("Check Guess", key='check_guess', use_container_width=True):
        if guess == number:
            st.success("You guessed it right!")
        else:
            st.warning("Wrong guess! Try again.")
elif game_option == "Tic-Tac-Toe":
    st.write("Tic-Tac-Toe coming soon!")

# Footer with "Powered by Faiqa Mubeen"
st.markdown(
    "<h4 style='text-align: center; color: skyblue;'>Powered by Faiqa Mubeen</h4>", unsafe_allow_html=True
)
