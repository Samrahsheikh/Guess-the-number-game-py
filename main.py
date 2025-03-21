import random
import streamlit as st

st.title("🎯 Guess the Number Game!")

# Set number range
lower_bound = 1
upper_bound = 100

# Initialize session state variables
if 'number_to_guess' not in st.session_state:
    st.session_state.number_to_guess = random.randint(lower_bound, upper_bound)
if 'attempts' not in st.session_state:
    st.session_state.attempts = 0
if 'message' not in st.session_state:
    st.session_state.message = ""

# User input
guess = st.number_input(f"Guess a number between {lower_bound} and {upper_bound}", min_value=lower_bound, max_value=upper_bound, step=1)

# Check button
if st.button("Check Guess"):
    st.session_state.attempts += 1
    if guess < st.session_state.number_to_guess:
        st.session_state.message = "Too low! Try again."
    elif guess > st.session_state.number_to_guess:
        st.session_state.message = "Too high! Try again."
    else:
        st.session_state.message = f"🎉 Congratulations! You guessed the number {st.session_state.number_to_guess} in {st.session_state.attempts} attempts."
        st.session_state.number_to_guess = random.randint(lower_bound, upper_bound)  # Reset for new game
        st.session_state.attempts = 0  # Reset attempts

st.write(st.session_state.message)
