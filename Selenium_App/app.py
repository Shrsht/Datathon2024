

import streamlit as st
import os
from resume import Resume
from skillset import Skillset
from model import *


# ------------------------------------------------------
#                      TAKE IN RESUME FROM USER:
# ------------------------------------------------------

### NEED TO CREATE Resume Class with Resume Parsing and Cleaning methods


st.set_page_config(page_title = "Resume Uploader")

resume_file = st.file_uploader(label = "Please Upload your Resume (pdf files only)", type = 'pdf')



import tempfile

if resume_file:
        temp_dir = tempfile.mkdtemp()
        path = os.path.join(temp_dir, resume_file.name)
        with open(path, "wb") as f:
                f.write(resume_file.getvalue())



if resume_file:
  #resume_file =   resume_file.read()
  res_object = Resume(path)
  resume_string =  res_object.parse_file()
  
#resume_string = st.text_input(label = "Please paste your desired Resume")

# ------------------------------------------------------
#          TAKIN IN JOB DESCRIPTION FROM USER:
# ------------------------------------------------------

### NEED TO CREATE Resume Class with Resume Parsing and Cleaning methods



job_file = st.text_input(label = "Please paste your desired Job Description")

if job_file:
   
   job_string = str(job_file)

button = st.button("Start Analysis")

# ------------------------------------------------------
#              INITIALISE SKILLSET OBJECTS:
# ------------------------------------------------------

if button:

    nlp = load_pipeline()#spacy.load('Datathon_Final_Model')

# ------------------------------------------------------
#              FIND RESUME KEYWORDS:
# ------------------------------------------------------

### NEED TO CREATE Predictor Class with Prediction Model


    user_skills = Skillset()
    user_skills = intialize_classes(user_skills,resume_string)

    job_skills = Skillset()
    job_skills = intialize_classes(job_skills,job_string)



# ------------------------------------------------------
#                         APP
# ------------------------------------------------------
# ------------------------------
# PART 1 : Pull data
# ------------------------------
    
    st.write(
'''
Our Algorithm Found the following keywords related to your Education:
''')

    st.write(user_skills.edu)

    st.write(
'''
Our Algorithm found the following Tools in your Resume:
''')
    user_tools = user_skills.tools
    st.write (user_tools)

    st.write(
'''
Our Algorithm found the following Missing Technical Skills in your Resume:
''')

    user_tech=  user_skills.tech_skill
    #st.write(user_tools)

    job_tools = job_skills.tech_skill

    matching_tools = set(job_tools) & set(user_tools)
    non_matching_tools1 = set(user_tools) - set(job_tools)
    non_matching_tools2 = set(job_tools) - set(user_tools)

    st.write(non_matching_tools2)

    import matplotlib.pyplot as plt

# Data
    sizes = [83, 17]
    labels = ['Matched Keywords', 'Unmatched Keywords']
    colors = ['green', 'orange']
    
    fig, ax = plt.subplots()
    ax.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90, pctdistance=0.85)
    plt.title('Job Match Statistics')

    #centre_circle = plt.Circle((0,0),0.70, fc)
    #fig.gca().add_artist(centre_circle)

    st.pyplot(fig)
