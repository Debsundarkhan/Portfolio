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
            "Transforming complex data into actionable business insights through advanced analytics and visualization")
    with col2:
        # Download resume button
        st.image("Deb Sundar Khan Pic.jpg")
# Sidebar with Contact Info
with st.sidebar:
    colored_header(
        label="About me",
        description="I am an MBA student specializing in Business Analytics and Data Science, passionate about turning data into actionable insights. With strong skills in Python, SQL, and analytical thinking, I thrive in dynamic environments. I’m also an active member of my college’s fitness club, balancing academics with a commitment to health and teamwork.",
        color_name="blue-70"
    )

    st.markdown("📧 **Email:**  \ndevkhadhn@gmail.com")
    st.markdown("📱 **Phone:**  \n+91 7645012176")
    st.markdown("🔗 **LinkedIn:**  \nwww.linkedin.com/in/deb-sundar-khan-0470782a1")
    st.markdown("💻 **GitHub:**  \ngithub.com/Debsundarkhan")

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
        Results-driven **Data Analytics Professional** with expertise in transforming complex datasets into actionable business insights. 
        Currently pursuing **MBA in Business Analytics and Data Science** with hands-on experience in:

        - Advanced data analysis and visualization
        - Predictive modeling and machine learning
        - Business intelligence and strategy development
        - SQL database management and optimization

        Passionate about leveraging data-driven approaches to solve business challenges and drive strategic decision-making.
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
            st.markdown("**PGPBA&DS + MBA**  \n*Bengal Institute of Business Studies*")
            st.markdown('<span style="color: #7f8c8d;">2024 - Present</span>', unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)

            st.markdown('<div class="timeline-item">', unsafe_allow_html=True)
            st.markdown("**B.Sc. Mathematics**  \n*P.K.ROY Memorial College, Dhanbad*")
            st.markdown('<span style="color: #7f8c8d;">2024</span>', unsafe_allow_html=True)
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
        st.markdown("**Data Science Intern**  \n*Prodigy InfoTech (Remote)*")
        st.markdown('<span style="color: #7f8c8d;">January 2025 - February 2025</span>', unsafe_allow_html=True)
        st.markdown("""
        - Analyzed customer behavior patterns using Python (Pandas, NumPy) to identify purchasing trends
        - Evaluated store trial performance metrics, delivering strategic recommendations that improved layout efficiency by 18%
        - Developed interactive dashboards to visualize key performance indicators for executive review
        - Automated weekly reporting processes, reducing manual work by 12 hours per week
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
            st.markdown("Built and optimized ML models using Python")

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
            st.markdown("Mastered SQL queries, database design, and data management")

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
            - Analyzed 12 months of sales data to identify purchasing patterns
            - Developed Python scripts to automate data cleaning and visualization
            - Created interactive dashboards highlighting key customer segments
            - Presented findings to stakeholders with actionable recommendations
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
            - Collected and analyzed 10,000+ social media posts
            - Implemented NLTK and TextBlob for sentiment classification
            - Visualized emotional trends over time
            - Achieved 85% accuracy in sentiment prediction
            """)
            st.markdown('<div class="skill-badge">Python</div>', unsafe_allow_html=True)
            st.markdown('<div class="skill-badge">NLTK</div>', unsafe_allow_html=True)
            st.markdown('<div class="skill-badge">TextBlob</div>', unsafe_allow_html=True)

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
        <form action="https://formsubmit.co/your.email@example.com" method="POST">
            <input type="hidden" name="_captcha" value="false">
            <input class="contact-input" type="text" name="name" placeholder="Your Name" required>
            <input class="contact-input" type="email" name="email" placeholder="Your Email" required>
            <input class="contact-input" type="text" name="subject" placeholder="Subject">
            <textarea class="contact-input" name="message" placeholder="Your Message" required style="height: 150px;"></textarea>
            <button class="contact-submit" type="submit">Send Message</button>
        </form>
        """
        st.markdown(contact_form, unsafe_allow_html=True)