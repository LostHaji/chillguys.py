import streamlit as st


st.set_page_config(page_title="CHLL Guys Resource Hub", layout="centered")


st.markdown(
    """
    <style>
        body {
            background-color: black;
            color: white;
            text-align: center;
        }

        .button-link {
            display: block;
            text-align: center;
            padding: 10px;
            background-color: #e72060;
            color: white;
            border-radius: 5px;
            text-decoration: none;
            font-weight: bold;
            font-size: 16px;
        }
        .button-link:hover {
            background-color: #b3194a;
        }

        .separator {
            border-bottom: 2px solid #e72060;
            margin: 20px 0;
        }

        /* Custom button styling */
        .custom-button {
            padding: 20px 40px;
            background-color: #2c2c2c;
            border-radius: 10px;
            font-size: 20px;
            font-weight: bold;
            color: #e72060;
            cursor: pointer;
            transition: background-color 0.3s;
            border: none;
            margin: 10px;
            width: 250px;  /* Button width for better centering */
        }

        .custom-button:hover {
            background-color: #b3194a;
        }

        .custom-button:active {
            background-color: #9c1b44;
        }

        .custom-button.selected {
            background-color: #e72060;
            color: white;
        }

        /* Style for the logo */
        .logo {
            display: block;
            margin: 0 auto;
            width: 450px; 
        }

        /* Adjusting the columns */
        .column {
            display: flex;
            justify-content: center;
            margin-top: 20px;
        }
    </style>
    """,
    unsafe_allow_html=True,
)


st.markdown(
    """
    <div style="text-align: center;">
        <img src="https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExOXhkbDd6bDhrNmU4MGFlMzR1ZnV0Nm56c2JqamN0NjVvaGF3MGt1MSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9cw/QcwARWARy1xubBa7Xw/giphy.gif" alt="Logo" class="logo"/>
    </div>
    """,
    unsafe_allow_html=True,
)


subjects = {
    "Science": {
        "description": "This section focuses on the definition, explanation, and effects of Electromagnetic Radiation to the Environment.",
        "topics": {
            "Advanced Chem": "https://drive.google.com/drive/folders/1w3aD8Iw3USx2SsaSEl3xEBYCeTsgrEtp?usp=sharing",
            "Physics": "https://drive.google.com/drive/folders/1-x61atzCPmNeMffcamn5e2lffg7GPxdx?usp=sharing",
        },
    },
    "Mathematics": {
        "description": "This section focuses on the Mathematical Concepts related to Electromagnetic Radiation as well as example questions for you to answer.",
        "topics": {
            "Math": "https://drive.google.com/drive/folders/1ftTHj4PVR5Bo9qvgsJORRTsd1aE2Q-zE?usp=sharing",
            "Diff Eq": "https://drive.google.com/drive/folders/13UCgahFLY3vjvOupQ3HtV71NNm0guMIu?usp=sharing",
        },
    },
    "Minor": {
        "description": "This section focuses on the effect of Electromagnetic Radiation to our Society",
        "topics": {
            "Araling Panlipunan": "https://drive.google.com/drive/folders/1563O6GmlFXm8OzXs_M2mqw7xK9krMTPK?usp=sharing",
            "GMRC": "https://drive.google.com/drive/folders/1rp2RDdUVDiU7xuHLTOSexF1jWpLujO_y?usp=sharing",
        },
    },
}


selection = None
col1, col2, col3 = st.columns(3) 
with col1:
    if st.button("Science", key="science", help="Click for Science resources", use_container_width=True):
        selection = "Science"
with col2:
    if st.button("Mathematics", key="math", help="Click for Mathematics resources", use_container_width=True):
        selection = "Mathematics"
with col3:
    if st.button("Minor", key="minor", help="Click for Minor subjects", use_container_width=True):
        selection = "Minor"


def display_subject_section(section_name, section_details):
    st.header(section_name)
    st.write(section_details["description"])
    cols = st.columns(len(section_details["topics"]))
    for idx, (topic_name, topic_link) in enumerate(section_details["topics"].items()):
        with cols[idx]:
            st.markdown(
                f'<a href="{topic_link}" target="_blank" class="button-link">{topic_name}</a>',
                unsafe_allow_html=True,
            )
    st.markdown('<div class="separator"></div>', unsafe_allow_html=True)

if selection:
    display_subject_section(selection, subjects[selection])
