import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image



# Function to display hemoglobin information
def display_hemoglobin_info():
    st.write(
        """
    ### Information about Hemoglobin:
    Hemoglobin is a protein in your red blood cells that carries oxygen to your body's organs and tissues and transports carbon dioxide from your organs and tissues back to your lungs.
    Anemia, characterized by a deficiency in red blood cells or hemoglobin concentration, remains a widespread global health concern affecting approximately 25 of the world’s population.
    This condition not only poses significant challenges for individuals but also exerts a considerable burden on healthcare systems.In the ever-evolving landscape of healthcare, the integration of technology has become increasingly crucial for
    enhancing the accuracy and efficiency of disease prediction and management. Real-time data collection and predictive analytics have emerged as powerful tools in this realm, offering
    a paradigm shift in the way we approach healthcare. This paper delves into the realm of real-time data collection and its application in predicting anemia, a condition characterized
    by a deficiency of red blood cells or hemoglobin in the blood
    """
    )

# Function to display blogs related to hemoglobin
def display_hemoglobin_blogs():
    st.write(
        """
    ### Blogs:
    - [Understanding Hemoglobin Levels](https://www.drkarunhematology.com/blog/top-effective-tips-to-increase-your-hemoglobin-count-naturally/#:~:text=Consume%20Iron%2DRich%20Foods,and%20raisins%2C%20and%20fortified%20cereals)
    - [Importance of Hemoglobin in the Body](https://my.clevelandclinic.org/health/diseases/3929-anemia)
    """
    )

# def display_images():
#     st.write("### Hemoglobin Structure:")
#     image = r"C:\Users\KHUSHI_CHIRCHI\Desktop\major project\iron level.jpg"  # Path to your local image file or URL
#     st.image(image, use_column_width=True)  # Display image with column width
def resize_image(image_path, width, height):
    img = Image.open(image_path)
    img = img.resize((width, height))
    return img

def display_images():
    st.write("### Information:")
    
    # Define paths to the images
    images = [
        r"C:\Users\KHUSHI_CHIRCHI\Desktop\major project\image1.jpg",
        #'https://lh6.googleusercontent.com/c1-DU2uLj-0cJen6gWw2tvyJRHk7eOePzo-24_xzadgiS0aEV595b8JclY4gIiwIV0hs2TPRVVW-GTvPvy-YsVLCthr63ZvVQDGwNvAjpb1dZY0OoanQGrUZazfWVopQXgyozySBrys5WilMR4eEvAM',
        r"C:\Users\KHUSHI_CHIRCHI\Desktop\major project\image2.jpg",
        r"C:\Users\KHUSHI_CHIRCHI\Desktop\major project\image3.jpg",
        r"C:\Users\KHUSHI_CHIRCHI\Desktop\major project\image4.jpg"
    ]

    resized_images = [resize_image(image, 400, 400) for image in images]

    col1, col2 = st.columns(2)
    with col1:
        st.image(resized_images[0], caption='Iron needs')
    with col2:
        st.image(resized_images[1], caption='Effect on Women')
    
    col3, col4 = st.columns(2)
    with col3:
        st.image(resized_images[2], caption='Range')
    with col4:
        st.image(resized_images[3], caption='Eat Healthy')
    
    # Display images in two rows and two columns
    # col1, col2 = st.columns(2)
    # with col1:
    #     st.image(images[0], caption='Iron needs', use_column_width=True)
    # with col2:
    #     st.image(images[1], caption='Effect on Women', use_column_width=True)
    
    # col3, col4 = st.columns(2)
    # with col3:
    #     st.image(images[2], caption='Range', use_column_width=True)
    # with col4:
    #     st.image(images[3], caption='Eat Healthy', use_column_width=True)

# Function to display explore page
def show_explore_page():
    st.title("Explore Hemoglobin Data")

    # Display information about hemoglobin
    display_hemoglobin_info()
    
    # Display blogs related to hemoglobin
    display_hemoglobin_blogs()

    display_images()


    # Your data exploration logic here
    pass

# Call the function to display the explore page
show_explore_page()
