import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

def main():
    css = '''
    <style>
    body {
        color: white;
        background-color: white;
        font-family: Tahoma, sans-serif;
    }
    .centered {
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        height: 100;
    }
    </style>
    '''
    st.markdown(css, unsafe_allow_html=True); st.markdown("<div class='centered'>", unsafe_allow_html=True); st.markdown("<h1 style='text-align: center;font-family: Tahoma, sans-serif;'>Elevate Your Resume</h1>", unsafe_allow_html=True)
    uploaded_file = st.file_uploader("Upload your resume (PDF)", type=["pdf"])
    if uploaded_file is not None:
        # Code related to ML model integration

        # Once analysis is done, navigate to the results page
        st.success("Resume analysis is complete!")
        if st.button("View Results"):
            results_page()
    st.markdown("</div>", unsafe_allow_html=True)


def results_page(rating_percentage, keyword_list, category_counts, category_percentages, add_keywords, replace_keywords):
    st.title(f"Your Rating: {rating_percentage}%")
    st.markdown("<div style='border: 1px solid white; padding: 10px;'>", unsafe_allow_html=True)
    st.header("Breakdown"); st.subheader("Identified Keywords:"); st.markdown("<ul>", unsafe_allow_html=True)
    for keyword in keyword_list:
        st.markdown(f"<li>{keyword}</li>", unsafe_allow_html=True)
    st.markdown("</ul>", unsafe_allow_html=True)
    st.subheader("Keyword Categories Analysis:")
    
    # Bar chart
    st.markdown("<div style='display: flex;'>", unsafe_allow_html=True)
    fig, ax = plt.subplots(); categories = list(category_counts.keys()); counts = list(category_counts.values())
    ax.bar(categories, counts, color='skyblue', edgecolor='white') 
    plt.xticks(rotation=45); st.pyplot(fig); st.markdown("</div>", unsafe_allow_html=True)

    # Pie chart
    st.markdown("<div style='display: flex;'>", unsafe_allow_html=True)
    fig, ax = plt.subplots(); ax.pie(list(category_percentages.values()), labels=categories, autopct='%1.1f%%', startangle=90)
    ax.axis('equal')
    st.pyplot(fig); st.markdown("</div>", unsafe_allow_html=True)

    st.subheader("Suggestions for Improvement:"); st.subheader("Add Keywords:"); st.markdown("<ul>", unsafe_allow_html=True)
    for keyword in add_keywords:
        st.markdown(f"<li>{keyword}</li>", unsafe_allow_html=True)
    st.markdown("</ul>", unsafe_allow_html=True)
    st.subheader("Replace Keywords:"); st.markdown("<ul>", unsafe_allow_html=True)
    for keyword, replacement in replace_keywords.items():
        st.markdown(f"<li>{keyword} -> {replacement}</li>", unsafe_allow_html=True)
    st.markdown("</ul>", unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)



if __name__ == "__main__":
    main()

