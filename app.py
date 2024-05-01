from pathlib import Path

import streamlit as st
from PIL import Image


# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "CV.pdf"


# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | Christopher Mitchell"
PAGE_ICON = ":wave:"
NAME = "Christopher Mitchell"
DESCRIPTION = """
Analytics Engineer
"""
EMAIL = "chris@chrismitchell.xyz"
SOCIAL_MEDIA = {
    "LinkedIn": "https://www.linkedin.com/in/christopher-m-48045187",
    "GitHub": "https://github.com/Rawlsy-py",
}
PROJECTS = {}


st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)


# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()


# --- HERO SECTION ---
col2 = st.columns(2, gap="small")

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📫", EMAIL)


# --- SOCIAL LINKS ---
st.write("\n")
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")


st.write(
    """
## Christopher Mitchell

Tamworth, England, B78  
07852793796  
[Christopher_m_mitchell@live.co.uk](mailto:Christopher_m_mitchell@live.co.uk)  

### Skills
- Experienced Analytics Engineer specialising in data pipeline development and automation.
- Proficient in Python, SQL, and R for data analytics, credit risk modelling, and machine learning.
- Skilled in Snowflake, Azure, Tableau, Git/Github, DataOps, and data solutions architecture.
- Background in Data Science, developing and deploying a credit risk model for retail finance.
- Confident in presenting complex data solutions to non-technical stakeholders.
- Currently pursuing a postgraduate degree in Computer Science part-time.
- Conducting novel research in server-side development for web applications with Rust.
- Expected graduation in May 2024.

### Experience
#### BINK, ASCOT — Analytics Engineer
*March 2023 - Present (Full Time, Remote)*
- Designed and maintained agile data pipelines using DBT, SQL, Python, Tableau, and PGSQL.
- Collaborated with cross-functional teams to provide actionable insights.
- Lead ground up creation of Snowflake Data Warehouse solution for working with big data.
- Utilised modern data stack deployed on Azure Cloud using Docker and Kubernetes.
- Developed and maintained CI/CD pipeline using GitHub Actions.
- Created, Maintained, and Presented Tableau dashboards to stakeholders.
- Automated data testing and introduced code review, and development standards within data team.
- Prepared Data Warehouse for AI and ML development work.
- Presented regularly to stakeholders, both technical and non-technical.
- Attended conferences with Snowflake and DBT Labs.

#### STREET UK FOUNDATION, BIRMINGHAM — Data Scientist
*May 2022 - Feb 2023 (Full Time, Hybrid)*
- Architected and engineered full azure data stack solution including:
  - Azure Data Factory, SQL and NoSQL databases, automated ETL pipelines, and machine learning.
- Utilised SQL, R, Python, and PowerBI for ETL processes, analytics, and machine learning.
- Analysed web service usage patterns and created self-service PowerBI dashboards.
- Led advanced analytics efforts, including K-Means Clustering for demographic data.
- Revitalised credit risk modelling with open banking API integration in Python.
- Designed data experiments (A/B Testing) for software solutions.
- Regularly reported updates to senior management team and board of trustees.
- Worked with marketing department to analyse ROI of campaigns.

### Employment History Prior to Career Switch
- **STREET UK FOUNDATION, BIRMINGHAM**
  - Admin Officer (June 2021 - May 2022)
  - Credit Control Officer (Oct 2020 - June 2021)
- **HSBC, BIRMINGHAM**
  - Collections Advisor (Feb 2020 - Sept 2020)
- **SHIRE LEASING PLC, TAMWORTH**
  - Collections Executive (April 2018 - Feb 2020)
  - Graduate Forensics Administrator (July 2017 - March 2018)
- **DRAYTON MANOR PARK, TAMWORTH**
  - Food and Beverage Host (July 2016 - July 2017)

### Education
- **UNIVERSITY OF WOLVERHAMPTON — MSc in Computer Science**
  - Sept 2021 - May 2024, Part-Time Hybrid Learning
  - Average Grade: Distinction
  - Novel research into the Rust programming language and its applications to software engineering.
  - Acquired proficiency in Python, R, Machine learning, AI, and cloud data technologies.
  - Completed projects in web development and mobile application development.
  - Learnt frameworks such as React, Flutter, Laravel, NodeJS, Django, FastAPI, and Actix.
  - Eager to apply these skills to software engineering roles.
  - Transcripts available upon request
- **UNIVERSITY OF LINCOLN — LLB in Law and Politics**
  - Sept 2013 - July 2016
- **POLESWORTH HIGH SCHOOL, TAMWORTH — A Levels**
  - Sept 2011 - July 2013, 3 at A-C
- **WILNECOTE HIGH SCHOOL, TAMWORTH — GCSEs**
  - Sept 2007 - July 2011, 7 at A-C including English and Mathematics
"""
)


# --- Projects & Accomplishments ---
st.write("\n")
st.subheader("Projects & Accomplishments")
st.write("---")
for project, link in PROJECTS.items():
    st.write(f"[{project}]({link})")
