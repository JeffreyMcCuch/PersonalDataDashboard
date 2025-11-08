import re
import streamlit as st
from Dashboard import GetUserName, GetFavNumberSquaredRoot
from GetWeatherAPI import GetWeatherAPI

# ---Initialize state variables ---
if "step" not in st.session_state:
    st.session_state.step = "welcome"
if "userName" not in st.session_state:
    st.session_state.userName = ""

# ---Step functions ---
def enterUserName():
    st.subheader("Enter Your Info 👇")
    first_name = st.text_input("Please enter your first name:")
    last_name = st.text_input("Please enter your last name:")

    if st.button("Submit Name"):
        if first_name and last_name:
            st.session_state.userName = GetUserName(first_name, last_name)
            st.session_state.step = "fav_number"  # Move to next step
            st.rerun()
        else:
            st.warning("Please fill out both your first and last name.")

def enterFavNumber():
    userName = st.session_state.userName
    st.success(f"Welcome, {userName}! 👋")
    favorite_number = st.number_input("Please enter your favorite number, and we'll figure out the quare root:", step=1.0)

    if st.button("Submit Number"):
        FavNumberResult = GetFavNumberSquaredRoot(favorite_number)
        if FavNumberResult is not False:
            st.session_state.favorite_number = favorite_number
            st.session_state.FavNumberResult = FavNumberResult
            st.session_state.step = "local_weather"  # Move to next step
            st.rerun()
        else:
            st.warning("Sorry negative numbers are not supported. Try another number!")

def enterZipCode():
    st.success(f"Got it, {st.session_state.userName}! Your favorite number is {st.session_state.favorite_number} its square root is {st.session_state.FavNumberResult:.2f} ✅")
    st.subheader("Now Let find out your Local Weather Info 🌤️")
    zip_code = st.text_input("Please enter your 5-digit zip code to get local weather info:")
    if st.button("Submit ZIP Code"):
        # Validate ZIP code: must be exactly 5 digits
        if re.fullmatch(r"\d{5}", zip_code):
            weather_info = GetWeatherAPI.MakeWeatherAPICall(zip_code)
            st.session_state.weather_info = weather_info
            st.session_state.step = "Profile_Picture"  # Move to next step
            st.rerun()
        else:
            st.error("Please enter a valid 5-digit ZIP code (e.g., 12345).")

def enterProfilePicture():
    st.success(f"{st.session_state.weather_info} ✅")
    st.subheader("\nFinally, Upload Your Profile Picture 📸!")
    profile_picture = st.file_uploader("Upload your profile picture here:", type=["jpg", "jpeg", "png"])

    if profile_picture is not None:
        st.session_state.image_uploaded = profile_picture
        st.session_state.step = "CompleteDashboard"  # Move to next step
        st.rerun()

def CompleteDashboard():
    st.success("Great we got your photo! You're almost done! ✅\n")
    st.image(st.session_state.image_uploaded, caption="Your Profile Picture",  use_container_width=True)
    st.subheader("Click the button below to complete:")
    if st.button("Complete Dashboard"):
        st.session_state.step = "done" # Final step
        st.rerun()

def Done():
    st.balloons()
    st.title("Here's Your Personal Data Dashboard Summary 🎉\n\n")
    st.write(f"**Name:** \n{st.session_state.userName}\n")
    st.write(f"**Square Root of Favorite Number {st.session_state.favorite_number}:**\n{st.session_state.FavNumberResult:.2f}\n")
    st.write(f"{st.session_state.weather_info}")
    st.image(st.session_state.image_uploaded, caption="Your Profile Picture", use_container_width=True)
    st.success("\nThank you for using the Personal Data Dashboard! 👏")

# ---Page layout ---
st.title("🎯 Personal Data Dashboard")

if st.session_state.step == "welcome":
    st.write("Hello, welcome to the Personal Data Dashboard!")
    if st.button("Enter Info"):
        st.session_state.step = "enter_name"
        st.rerun()

elif st.session_state.step == "enter_name":
    enterUserName()

elif st.session_state.step == "fav_number":
    enterFavNumber()

elif st.session_state.step == "local_weather":
    enterZipCode()

elif st.session_state.step == "Profile_Picture":
    enterProfilePicture()

elif st.session_state.step == "CompleteDashboard":
    CompleteDashboard()

elif st.session_state.step == "done":
    Done()