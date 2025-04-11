import streamlit as st
from streamlit_extras.colored_header import colored_header
from streamlit_extras.stylable_container import stylable_container
import base64

# Page Configuration
st.set_page_config(
    page_title="Deb Sundar Khan | Data Analyst Portfolio",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for modern styling
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;600;700&display=swap');

    html, body, [class*="css"] {
        font-family: 'Montserrat', sans-serif;
    }

    .main {
        background-color: #f9fbfd;
    }

    .section-title {
        font-size: 28px;
        font-weight: 700;
        color: #2a3f5f;
        margin-bottom: 20px;
        position: relative;
    }

    .section-title:after {
        content: "";
        display: block;
        width: 60px;
        height: 4px;
        background: linear-gradient(90deg, #6a11cb 0%, #2575fc 100%);
        margin-top: 8px;
        border-radius: 2px;
    }

    .card {
        background: white;
        border-radius: 12px;
        padding: 25px;
        margin-bottom: 25px;
        box-shadow: 0 6px 16px rgba(0,0,0,0.08);
        transition: transform 0.3s ease;
    }

    .card:hover {
        transform: translateY(-5px);
    }

    .timeline-item {
        border-left: 3px solid #2575fc;
        padding-left: 25px;
        padding-bottom: 20px;
        position: relative;
    }

    .timeline-item:before {
        content: "";
        position: absolute;
        width: 12px;
        height: 12px;
        border-radius: 50%;
        background: #6a11cb;
        left: -7.5px;
        top: 5px;
    }

    .skill-badge {
        display: inline-block;
        background: linear-gradient(135deg, #6a11cb 0%, #2575fc 100%);
        color: white;
        padding: 6px 12px;
        border-radius: 20px;
        margin: 5px 5px 5px 0;
        font-size: 14px;
    }

    .contact-input {
        width: 100%;
        padding: 12px;
        border: 1px solid #e0e0e0;
        border-radius: 8px;
        margin-bottom: 15px;
        font-size: 16px;
    }

    .contact-submit {
        background: linear-gradient(135deg, #6a11cb 0%, #2575fc 100%);
        color: white;
        border: none;
        padding: 12px 24px;
        border-radius: 8px;
        cursor: pointer;
        font-size: 16px;
        font-weight: 600;
        transition: all 0.3s ease;
    }

    .contact-submit:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 12px rgba(106,17,203,0.3);
    }
</style>
""", unsafe_allow_html=True)

# Gradient Header
with stylable_container(
        key="header",
        css_styles="""
    {
        background: linear-gradient(135deg, #6a11cb 0%, #2575fc 100%);
        padding: 3rem;
        border-radius: 0 0 15px 15px;
        color: white;
        margin-bottom: 2rem;
    }
    """
):
    col1, col2 = st.columns([3, 1])
    with col1:
        st.title("Deb Sundar Khan")
        st.markdown("#### Data Analytics Professional | MBA in Business Analytics & Data Science")
        st.markdown(
            "An hardworking individual with a passion for Data Analytics, committed to making an impact as a strategic Data Analyst")
    with col2:
        # Keep your image as is
        st.image("Deb Sundar Khan Pic.jpg")

# Sidebar with Contact Info
with st.sidebar:
    colored_header(
        label="About me",
        description="I am an MBA student specializing in Business Analytics and Data Science at Bengal Institute of Business Studies, passionate about turning data into actionable insights. With strong technical skills in Python, SQL, and Machine Learning, I combine analytical thinking with business acumen to solve complex problems. My internship at Prodigy InfoTech honed my ability to derive meaningful insights from data.",
        color_name="blue-70"
    )

    st.markdown("📧 **Email:**  \ndevkhadhn@gmail.com")
    st.markdown("📱 **Phone:**  \n+91 7645012176")
    st.markdown("🔗 **LinkedIn:**  \n[linkedin.com/in/deb-sundar-khan-0470782a1](https://www.linkedin.com/in/deb-sundar-khan-0470782a1)")
    st.markdown("💻 **GitHub:**  \n[github.com/Debsundarkhan](https://github.com/Debsundarkhan)")

    colored_header(
        label="Technical Skills",
        description="",
        color_name="blue-70"
    )

    st.markdown('<div class="skill-badge">Python</div>', unsafe_allow_html=True)
    st.markdown('<div class="skill-badge">SQL</div>', unsafe_allow_html=True)
    st.markdown('<div class="skill-badge">Pandas/Numpy</div>', unsafe_allow_html=True)
    st.markdown('<div class="skill-badge">Machine Learning</div>', unsafe_allow_html=True)
    st.markdown('<div class="skill-badge">Power BI</div>', unsafe_allow_html=True)
    st.markdown('<div class="skill-badge">Data Visualization</div>', unsafe_allow_html=True)

# Main Content
tab1, tab2, tab3, tab4 = st.tabs(["About", "Experience", "Projects", "Contact"])

with tab1:
    st.markdown('<div class="section-title">Professional Profile</div>', unsafe_allow_html=True)

    with stylable_container(
            key="profile_card",
            css_styles="""
        {
            background: white;
            border-radius: 12px;
            padding: 25px;
            box-shadow: 0 6px 16px rgba(0,0,0,0.08);
        }
        """
    ):
        st.markdown("""
        Results-driven **Data Analytics Professional** currently pursuing MBA in Business Analytics and Data Science at Bengal Institute of Business Studies. Key strengths include:

        - Expertise in Python data analysis (Pandas, NumPy, Matplotlib)
        - Strong foundation in SQL and relational databases
        - Machine Learning model development and optimization
        - Business intelligence and data visualization with Power BI
        - Strategic analysis of consumer behavior and market trends

        Passionate about leveraging data to drive business decisions and create impactful solutions.
        """)

    st.markdown('<div class="section-title">Education</div>', unsafe_allow_html=True)

    col1, col2 = st.columns([4, 1])
    with col1:
        with stylable_container(
                key="education_card",
                css_styles="""
            {
                background: white;
                border-radius: 12px;
                padding: 25px;
                box-shadow: 0 6px 16px rgba(0,0,0,0.08);
            }
            """
        ):
            st.markdown('<div class="timeline-item">', unsafe_allow_html=True)
            st.markdown("**PGPBA&DS + MBA**  \n*Bengal Institute of Business Studies*  \nSpecialization in Business Analytics and Data Science")
            st.markdown('<span style="color: #7f8c8d;">2024 - Present</span>', unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)

            st.markdown('<div class="timeline-item">', unsafe_allow_html=True)
            st.markdown("**B.Sc. Mathematics**  \n*P.K.ROY Memorial College, Dhanbad*")
            st.markdown('<span style="color: #7f8c8d;">Graduated 2024</span>', unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)

            st.markdown('<div class="timeline-item">', unsafe_allow_html=True)
            st.markdown("**XII - C.B.S.E**  \n*D.A.V. Model School, C.F.R.I., Dhanbad*")
            st.markdown('<span style="color: #7f8c8d;">2021</span>', unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)

with tab2:
    st.markdown('<div class="section-title">Professional Experience</div>', unsafe_allow_html=True)

    with stylable_container(
            key="experience_card",
            css_styles="""
        {
            background: white;
            border-radius: 12px;
            padding: 25px;
            box-shadow: 0 6px 16px rgba(0,0,0,0.08);
        }
        """
    ):
        st.markdown('<div class="timeline-item">', unsafe_allow_html=True)
        st.markdown("**Data Science Intern (Remote)**  \n*Prodigy InfoTech*")
        st.markdown('<span style="color: #7f8c8d;">January 2025 - February 2025</span>', unsafe_allow_html=True)
        st.markdown("""
        - Analyzed customer behavior and evaluated store trial performance using Python
        - Delivered data-driven insights and strategic recommendations for the chips category
        - Developed store layout optimization suggestions based on customer flow analysis
        - Created visualizations to communicate findings to stakeholders
        """)
        st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="section-title">Certifications</div>', unsafe_allow_html=True)

    cert_cols = st.columns(2)
    with cert_cols[0]:
        with stylable_container(
                key="cert_card1",
                css_styles="""
            {
                background: white;
                border-radius: 12px;
                padding: 20px;
                box-shadow: 0 6px 16px rgba(0,0,0,0.08);
                height: 100%;
            }
            """
        ):
            st.markdown("**Machine Learning with Python**  \n*IIT Kanpur*")
            st.markdown('<span style="color: #7f8c8d;">2024</span>', unsafe_allow_html=True)
            st.markdown("- Built and optimized ML models using Python")
            st.markdown("- Covered supervised and unsupervised learning techniques")

    with cert_cols[1]:
        with stylable_container(
                key="cert_card2",
                css_styles="""
            {
                background: white;
                border-radius: 12px;
                padding: 20px;
                box-shadow: 0 6px 16px rgba(0,0,0,0.08);
                height: 100%;
            }
            """
        ):
            st.markdown("**SQL and Relational Database**  \n*IBM*")
            st.markdown('<span style="color: #7f8c8d;">2024</span>', unsafe_allow_html=True)
            st.markdown("- Mastered SQL queries and database design")
            st.markdown("- Gained expertise in data management and optimization")

    cert_cols = st.columns(2)
    with cert_cols[0]:
        with stylable_container(
                key="cert_card3",
                css_styles="""
            {
                background: white;
                border-radius: 12px;
                padding: 20px;
                box-shadow: 0 6px 16px rgba(0,0,0,0.08);
                height: 100%;
            }
            """
        ):
            st.markdown("**Accenture Nordics Consultant Simulation**  \n*Forage*")
            st.markdown('<span style="color: #7f8c8d;">2024</span>', unsafe_allow_html=True)
            st.markdown("- Analyzed data to recommend UX improvements")
            st.markdown("- Managed project priorities for healthcare client")

    with cert_cols[1]:
        with stylable_container(
                key="cert_card4",
                css_styles="""
            {
                background: white;
                border-radius: 12px;
                padding: 20px;
                box-shadow: 0 6px 16px rgba(0,0,0,0.08);
                height: 100%;
            }
            """
        ):
            st.markdown("**Tata Data Visualization Simulation**  \n*Forage*")
            st.markdown('<span style="color: #7f8c8d;">2024</span>', unsafe_allow_html=True)
            st.markdown("- Created Power BI dashboards for retail client")
            st.markdown("- Supported executive decision-making")

with tab3:
    st.markdown('<div class="section-title">Featured Projects</div>', unsafe_allow_html=True)

    proj_cols = st.columns(2)
    with proj_cols[0]:
        with stylable_container(
                key="proj_card1",
                css_styles="""
            {
                background: white;
                border-radius: 12px;
                padding: 20px;
                box-shadow: 0 6px 16px rgba(0,0,0,0.08);
                height: 100%;
            }
            """
        ):
            st.markdown("**Consumer Trend Analysis**  \n*Tata Consumer Products*")
            st.markdown("""
            - Conducted data analysis on Tata Consumer Products trends
            - Used Python (Pandas/Matplotlib) to analyze sales patterns
            - Derived insights on customer preferences
            - Created visualizations of key findings
            """)
            st.markdown('<div class="skill-badge">Python</div>', unsafe_allow_html=True)
            st.markdown('<div class="skill-badge">Pandas</div>', unsafe_allow_html=True)
            st.markdown('<div class="skill-badge">Matplotlib</div>', unsafe_allow_html=True)

    with proj_cols[1]:
        with stylable_container(
                key="proj_card2",
                css_styles="""
            {
                background: white;
                border-radius: 12px;
                padding: 20px;
                box-shadow: 0 6px 16px rgba(0,0,0,0.08);
                height: 100%;
            }
            """
        ):
            st.markdown("**Social Media Sentiment Analysis**  \n*Python Project*")
            st.markdown("""
            - Analyzed and visualized sentiment patterns from social media
            - Used Python (NLTK/TextBlob) to classify emotions
            - Identified key trends in user sentiment
            - Created interactive visualizations
            """)
            st.markdown('<div class="skill-badge">Python</div>', unsafe_allow_html=True)
            st.markdown('<div class="skill-badge">NLTK</div>', unsafe_allow_html=True)
            st.markdown('<div class="skill-badge">TextBlob</div>', unsafe_allow_html=True)

    proj_cols = st.columns(2)
    with proj_cols[0]:
        with stylable_container(
                key="proj_card3",
                css_styles="""
            {
                background: white;
                border-radius: 12px;
                padding: 20px;
                box-shadow: 0 6px 16px rgba(0,0,0,0.08);
                height: 100%;
            }
            """
        ):
            st.markdown("**Retail Analytics for Customer Segmentation**")
            st.markdown("""
            - Analyzed customer segments and purchasing behavior
            - Developed clustering models for segmentation
            - Provided data-driven marketing recommendations
            - Created customer persona visualizations
            """)
            st.markdown('<div class="skill-badge">Python</div>', unsafe_allow_html=True)
            st.markdown('<div class="skill-badge">Machine Learning</div>', unsafe_allow_html=True)
            st.markdown('<div class="skill-badge">Segmentation</div>', unsafe_allow_html=True)

    with proj_cols[1]:
        with stylable_container(
                key="proj_card4",
                css_styles="""
            {
                background: white;
                border-radius: 12px;
                padding: 20px;
                box-shadow: 0 6px 16px rgba(0,0,0,0.08);
                height: 100%;
            }
            """
        ):
            st.markdown("**Rock Paper Scissors Game**  \n*Python Project*")
            st.markdown("""
            - Developed interactive game against computer
            - Implemented user input validation
            - Designed random choice logic
            - Created score tracking system
            """)
            st.markdown('<div class="skill-badge">Python</div>', unsafe_allow_html=True)
            st.markdown('<div class="skill-badge">Game Development</div>', unsafe_allow_html=True)

with tab4:
    st.markdown('<div class="section-title">Get In Touch</div>', unsafe_allow_html=True)

    with stylable_container(
            key="contact_form",
            css_styles="""
        {
            background: white;
            border-radius: 12px;
            padding: 30px;
            box-shadow: 0 6px 16px rgba(0,0,0,0.08);
        }
        """
    ):
        contact_form = """
        <form action="https://formsubmit.co/devkhadhn@gmail.com" method="POST">
            <input type="hidden" name="_captcha" value="false">
            <input class="contact-input" type="text" name="name" placeholder="Your Name" required>
            <input class="contact-input" type="email" name="email" placeholder="Your Email" required>
            <input class="contact-input" type="text" name="subject" placeholder="Subject">
            <textarea class="contact-input" name="message" placeholder="Your Message" required style="height: 150px;"></textarea>
            <button class="contact-submit" type="submit">Send Message</button>
        </form>
        """
        st.markdown(contact_form, unsafe_allow_html=True)
