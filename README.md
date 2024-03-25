# Datathon2024: Job Application Assistant:

Our submission to Datathon 2024 has been to create a Job-Application Assistant that accepts an uploaded Resume and uses a Fine-Tuned BERT() Named Entity Recognition model to generate analytics on the applicant's fit for a given job-description as well as provide recommendations on missing key-words and phrases to the resume. 

This model is unique in that it does **NOT** make use of any pre-trained transformer models and was actually trained and fine-tuned on manually collected and annotated job-descriptions. This allowed the BERT() model to not only identify a set of keywords form a document but to also predict labels for these keywords such as 'education','technical-skills','interpersonal-skills',etc. 

Using both the keywords and their corresponding labels, our Streamlit web-app generates visual analytics and provides reccomendations on missing keywords. 

### Team Members: Shresht Venkatraman, Anurag Reddy, Bharat Gudipudi, Colten 

### Data Collection:

The **Selenium_Scraping** Notebook in this Repository contains the code used to scrape 250 job_descirptions off LinkedIn. These job descriptions have been cleaned and stored in the **clean_jobs.csv** file

### Model Building:

The creation of our BERT - Named Entity Recognition Model is outlined in the notebook titled **Model_GPU_Training.ipynb**. It contains all the required information and documentation of our HuggingFace Transformers as well as associated packages used to deploy our model. 

The Transformer Model itself is stored in the file labeled - **model_best**. Due to the large size of the Spacy model as well the GPU computational requirements, we recommend you download the model_best file and initialise the pipeline on your local system 

The key aspect of our implementation is our ability to perform *" fine-tuning"*. As explained in the accompanying video, pre-trained BERT models did not give us satisfactory Key-Word tags and recognition ability. We made use of novel approach of **annotated training data** to get the BERT Transformer to predict both Keywords in a document but also to assign Labels to those keywords for assesment. 

Our inspiration for the devlopment of the model comes from: https://towardsdatascience.com/how-to-fine-tune-bert-transformer-with-spacy-3-6a90bfe57647

### Streamlit App:

We attempted to create a basic streamlit application that takes in Resume files and job descriptions as inputs. This app runs our Fine Tuned BERT model to generate keyword analytics and outputs. Due to time contstraints the app is still at its bare minimum stage, however it works well as a proof-of-concept. 

### Data Annotation:
The Innovative Aspect of our Job Application Assistant is that it predicts both keywords and keyword-labels. This has been achieved through a manual creation of labelled-training data. 
