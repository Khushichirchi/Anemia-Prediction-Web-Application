

# # # # # import streamlit as st
# # # # # import joblib
# # # # # import numpy as np

# # # # # # Function to load the trained model
# # # # # def load_model():
# # # # #     model = joblib.load('trained_model_nlr1.pkl')
# # # # #     return model

# # # # # # Load the trained model
# # # # # model = load_model()

# # # # # def preprocess_input_data(age, old, duration, gender):
# # # # #     # Encode gender (if needed)
# # # # #     gender_encoded = 1 if gender == "Female" else 0
    
# # # # #     # Prepare input data for prediction
# # # # #     input_data = np.array([[age, gender_encoded, old, duration,0,0,0]])
    
# # # # #     return input_data

# # # # # def adjust_prediction_based_on_conditions(old_hemoglobin, duration):
# # # # #     increase_percent = (duration // 3) * 0.1
# # # # #     return increase_percent

# # # # # def show_predict_page():
# # # # #     st.title("Hemoglobin Level Increase Prediction")

# # # # #     st.write("""### Please provide the required information for prediction""")

# # # # #     age = st.number_input("Age", min_value=0, max_value=150, value=30, step=1)
# # # # #     old_hemoglobin = st.number_input("Old Hemoglobin Level", min_value=0.0, value=12.0, step=0.1)
# # # # #     duration = st.number_input("Duration (in days)", min_value=0, value=30, step=1)
# # # # #     gender = st.selectbox("Gender", ("Male", "Female"))

# # # # #     ok = st.button("Predict Hemoglobin Increase")
# # # # #     if ok:
# # # # #         # Adjust prediction based on conditions
# # # # #         percent_increase = adjust_prediction_based_on_conditions(old_hemoglobin, duration)

# # # # #         # Display prediction
# # # # #         st.subheader(f"The estimated percentage increase in hemoglobin level is: {percent_increase:.2f}g/dl")
# # # # #         st.write("Note: This is a simplified prediction. Consult a healthcare professional for accurate assessments.")

# # # # # # Run the Streamlit app
# # # # # if __name__ == "__main__":
# # # # #     show_predict_page()











# # # import streamlit as st
# # # import joblib
# # # import numpy as np

# # # # Function to load the trained model
# # # def load_model():
# # #     model = joblib.load('trained_model_nlr1.pkl')
# # #     return model

# # # # Load the trained model
# # # model = load_model()

# # # def preprocess_input_data(age, old, duration, gender):
# # #     # Encode gender (if needed)
# # #     gender_encoded = 1 if gender == "Female" else 0
    
# # #     # Prepare input data for prediction
# # #     input_data = np.array([[age, gender_encoded, old, duration,0,0,0]])
    
# # #     return input_data

# # # def adjust_prediction_based_on_conditions(old_hemoglobin, duration, gender):
# # #     if gender == "Male":
# # #         increase_percent = min(duration // 3, 10) * 0.1
# # #     elif gender == "Female":
# # #         increase_percent = min(duration // 3, 7.5) * 0.075
    
# # #     return old_hemoglobin * (1 + increase_percent / 10)

# # # def show_predict_page():
# # #     st.title("Hemoglobin Level Increase Prediction")

# # #     st.write("""### Please provide the required information for prediction""")

# # #     age = st.number_input("Age", min_value=0, max_value=150, value=30, step=1)
# # #     old_hemoglobin = st.number_input("Old Hemoglobin Level", min_value=0.0, value=12.0, step=0.1)
# # #     duration = st.number_input("Duration (in days)", min_value=0, value=30, step=1)
# # #     gender = st.selectbox("Gender", ("Male", "Female"))

# # #     ok = st.button("Predict Hemoglobin Increase")
# # #     if ok:
# # #         # Adjust prediction based on conditions
# # #         new_hemoglobin = adjust_prediction_based_on_conditions(old_hemoglobin, duration, gender)

# # #         # Display prediction
# # #         st.subheader(f"The estimated new hemoglobin level is: {new_hemoglobin:.2f} g/dl")

# # # # Run the Streamlit app
# # # if __name__ == "__main__":
# # #     show_predict_page()


# # import streamlit as st
# # import joblib
# # import numpy as np

# # # Function to load the trained model
# # def load_model():
# #     model = joblib.load('trained_model_nlr1.pkl')
# #     return model

# # # Load the trained model
# # model = load_model()

# # def preprocess_input_data(age, old, duration, gender):
# #     # Encode gender (if needed)
# #     gender_encoded = 1 if gender == "Female" else 0
    
# #     # Prepare input data for prediction
# #     input_data = np.array([[age, gender_encoded, old, duration,0,0,0]])
    
# #     return input_data

# # def adjust_prediction_based_on_conditions(old_hemoglobin, duration, gender):
# #     if gender == "Male":
# #         increase_percent = min(duration // 3, 10) * 0.1
# #     elif gender == "Female":
# #         increase_percent = min(duration // 3, 10) * 0.08
    
# #     return old_hemoglobin * (1 + increase_percent / 10)

# # def show_predict_page():
# #     st.title("Hemoglobin Level Increase Prediction")

# #     st.write("""### Please provide the required information for prediction""")

# #     age = st.number_input("Age", min_value=0, max_value=150, value=30, step=1)
# #     old_hemoglobin = st.number_input("Old Hemoglobin Level", min_value=0.0, value=12.0, step=0.1)
# #     duration = st.number_input("Duration (in days)", min_value=0, value=30, step=1)
# #     gender = st.selectbox("Gender", ("Male", "Female"))

# #     ok = st.button("Predict Hemoglobin Increase")
# #     if ok:
# #         # Adjust prediction based on conditions
# #         new_hemoglobin = adjust_prediction_based_on_conditions(old_hemoglobin, duration, gender)

# #         # Display prediction
# #         st.subheader(f"The estimated new hemoglobin level is: {new_hemoglobin:.2f} g/dl")

# # # Run the Streamlit app
# # if __name__ == "__main__":
# #     show_predict_page()


# import streamlit as st
# import joblib
# import numpy as np

# # Function to load the trained model
# def load_model():
#     model = joblib.load('trained_model_nlr1.pkl')
#     return model

# # Load the trained model
# model = load_model()

# def preprocess_input_data(age, old, duration, gender):
#     # Encode gender (if needed)
#     gender_encoded = 1 if gender == "Female" else 0
    
#     # Prepare input data for prediction
#     input_data = np.array([[age, gender_encoded, old, duration,0,0,0]])
    
#     return input_data

# def adjust_age_based_on_conditions(age):
#     if age <= 10:
#         return age + 5
#     elif 10 < age <= 28:
#         return age + 3
#     elif 28 < age <= 40:
#         return age + 1
#     elif 45 <= age <= 55:
#         return age + 0.5
#     else:
#         return age + 0.1

# def adjust_prediction_based_on_conditions(old_hemoglobin, duration, gender, age):
#     if gender == "Male":
#         increase_percent = min(duration // 3, 10) * 0.1
#     elif gender == "Female":
#         increase_percent = 0
#         if 1 <= age <= 10:
#             increase_percent = min(duration // 3, 10) * 0.15
#         elif 10 < age <= 28:
#             increase_percent = min(duration // 3, 10) * 0.12
#         elif 28 < age <= 40:
#             increase_percent = min(duration // 3, 10) * 0.08
#         elif 45 <= age <= 55:
#             increase_percent = min(duration // 3, 10) * 0.05
#         else:
#             increase_percent = min(duration // 3, 10) * 0.01
    
#     return old_hemoglobin * (1 + increase_percent / 10)

# def show_predict_page():
#     st.title("Hemoglobin Level Increase Prediction")

#     st.write("""### Please provide the required information for prediction""")

#     age = st.number_input("Age", min_value=0, max_value=150, value=30, step=1)
#     age = adjust_age_based_on_conditions(age)  # Adjust age based on conditions
#     old_hemoglobin = st.number_input("Old Hemoglobin Level", min_value=0.0, value=12.0, step=0.1)
#     duration = st.number_input("Duration (in days)", min_value=0, value=30, step=1)
#     gender = st.selectbox("Gender", ("Male", "Female"))

#     ok = st.button("Predict Hemoglobin Increase")
#     if ok:
#         # Adjust prediction based on conditions
#         new_hemoglobin = adjust_prediction_based_on_conditions(old_hemoglobin, duration, gender, age)

#         # Display prediction
#         st.subheader(f"The estimated new hemoglobin level is: {new_hemoglobin:.2f} g/dl")

# # Run the Streamlit app
# if __name__ == "__main__":
#     show_predict_page()



import streamlit as st
import joblib
import numpy as np

# Function to load the trained model
def load_model():
    model = joblib.load('trained_model_nlr1.pkl')
    return model

# Load the trained model
model = load_model()

def preprocess_input_data(age, old, duration, gender):
    # Encode gender (if needed)
    gender_encoded = 1 if gender == "Female" else 0
    
    # Prepare input data for prediction
    input_data = np.array([[age, gender_encoded, old, duration,0,0,0]])
    
    return input_data

def adjust_age_based_on_conditions(age, gender):
    if gender == "Female":
        if age <= 10:
            return age + 5
        elif 10 < age <= 28:
            return age + 3
        elif 28 < age <= 40:
            return age + 1
        elif 45 <= age <= 55:
            return age + 0.5
        else:
            return age + 0.1
    else:  # Male
        if age <= 18:
            return age + 3
        elif 18 < age <= 45:
            return age + 1
        else:
            return age + 0.1

def adjust_prediction_based_on_conditions(old_hemoglobin, duration, gender, age):
    if gender == "Male":
        increase_percent = 0
        if 1 <= age <= 18:
            increase_percent = min(duration // 3, 10) * 0.15
        elif 18 < age <= 45:
            increase_percent = min(duration // 3, 10) * 0.12
        else:
            increase_percent = min(duration // 3, 10) * 0.08
    elif gender == "Female":
        increase_percent = 0
        if 1 <= age <= 10:
            increase_percent = min(duration // 3, 10) * 0.15
        elif 10 < age <= 28:
            increase_percent = min(duration // 3, 10) * 0.12
        elif 28 < age <= 40:
            increase_percent = min(duration // 3, 10) * 0.08
        elif 45 <= age <= 55:
            increase_percent = min(duration // 3, 10) * 0.05
        else:
            increase_percent = min(duration // 3, 10) * 0.01
    
    return old_hemoglobin * (1 + increase_percent / 10)

def show_predict_page():
    st.title("Hemoglobin Level Increase Prediction")

    st.write("""### Please provide the required information for prediction""")

    age = st.number_input("Age", min_value=0, max_value=150, value=30, step=1)
    gender = st.selectbox("Gender", ("Male", "Female"))
    age = adjust_age_based_on_conditions(age, gender)  # Adjust age based on conditions
    old_hemoglobin = st.number_input("Old Hemoglobin Level", min_value=0.0, value=12.0, step=0.1)
    duration = st.number_input("Duration (in days)", min_value=0, value=30, step=1)

    ok = st.button("Predict Hemoglobin Increase")
    if ok:
        # Adjust prediction based on conditions
        new_hemoglobin = adjust_prediction_based_on_conditions(old_hemoglobin, duration, gender, age)

        # Display prediction
        st.subheader(f"The estimated new hemoglobin level is: {new_hemoglobin:.2f} g/dl")

# Run the Streamlit app
if __name__ == "__main__":
    show_predict_page()
