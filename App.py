import json
import streamlit as st

# Remove Streamlit's default padding and header
st.set_page_config(
    page_title="Pranav Pinara • Portfolio", 
    layout="wide", 
    page_icon="⚡",
    initial_sidebar_state="collapsed"
)

# Hide Streamlit's default elements
st.markdown("""
    <style>
        /* Hide Streamlit branding and default elements */
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        .stApp {
            margin: 0;
            padding: 0;
        }
        .stApp > header {
            display: none !important;
        }
        .main .block-container {
            padding: 0 !important;
            max-width: 100% !important;
        }
        /* Remove all default margins */
        .stApp {
            margin-top: -60px;
        }
        .element-container, .stMarkdown, .stMarkdown div {
            margin: 0;
            padding: 0;
        }
    </style>
""", unsafe_allow_html=True)

# Professional Resume-Style Data
profile = {
    "name": "Pranav Pinara",
    "title": "Computer Engineering Student",
    "bio": "2nd Semester Diploma Student | Tech Enthusiast | Sportsman",
    "birthdate": "12th November 2009",
    "email": "pranav.Pinara@student.edu",
    "location": "India"
}

# Academic Achievements
academics = [
    {
        "degree": "Diploma in Computer Engineering",
        "institution": "Current Program",
        "year": "2025 - Present",
        "sem1": "98%",
        "sem2": "In Progress",
        "status": "2nd Semester • Ongoing"
    },
    {
        "degree": "10th Grade (SSC)",
        "institution": "Board Examination",
        "year": "2024",
        "percentage": "94%",
        "status": "Completed with Distinction"
    }
]

# Technical Skills
tech_skills = {
    "AI & ML": ["Python", "TensorFlow Basics", "Data Science Fundamentals", "Neural Networks"],
    "Web Development": ["HTML5", "CSS3", "JavaScript", "React.js", "Node.js"],
    "Mobile Development": ["Flutter", "React Native", "Android Basics"],
    "Database": ["MongoDB", "Firebase", "MySQL Basics"],
    "Tools & Others": ["Git", "VS Code", "Figma", "Postman"]
}

# Sports & Extracurricular
sports = [
    {"name": "Cricket", "role": "All-rounder", "achievement": "College Team Member • Best Batsman Award"},
    {"name": "Volleyball", "role": "Spiker", "achievement": "Inter-college Tournament Participant"},
    {"name": "Chess", "role": "Strategic Player", "achievement": "District Level Competitor"}
]

# Good Habits (Professional)
habits = [
    "Daily coding practice (2+ hours)",
    "Morning routine: 6 AM wake-up",
    "Weekly tech blog reading",
    "Problem-solving on LeetCode",
    "Regular fitness & sports",
    "Time management & planning"
]

# Projects
projects = [
    {
        "name": "Portfolio Website",
        "tech": "HTML, CSS, JavaScript",
        "desc": "Personal portfolio showcasing skills and projects"
    },
    {
        "name": "College Management System",
        "tech": "Python, Flask, MongoDB",
        "desc": "Student record management system (Academic project)"
    },
    {
        "name": "Weather App",
        "tech": "React.js, API Integration",
        "desc": "Real-time weather application"
    }
]

# Certifications
certifications = [
    "Python for Everybody (In Progress)",
    "Web Development Bootcamp - 2025",
    "Introduction to AI (Coursera)"
]

# Languages
languages = [
    {"lang": "English", "level": "Professional Working"},
    {"lang": "Hindi", "level": "Native"},
    {"lang": "Gujarati", "level": "Native"}
]

html = r"""
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0, user-scalable=yes">
<title>Pranav Pinara • Portfolio</title>
<style>
    * {
        margin: 0;
        padding: 0;
        box-sizing: border-box;
    }

    body {
        font-family: 'Segoe UI', 'Poppins', -apple-system, BlinkMacSystemFont, sans-serif;
        background: #0a0e27;
        color: #fff;
        line-height: 1.6;
        overflow-x: hidden;
        width: 100%;
        min-height: 100vh;
    }

    /* Remove any default margins */
    html, body {
        margin: 0;
        padding: 0;
        width: 100%;
    }

    .container {
        max-width: 1400px;
        margin: 0 auto;
        padding: 40px 20px;
        width: 100%;
    }

    /* Header Section */
    .header {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        border-radius: 20px;
        padding: 50px;
        margin-bottom: 30px;
        text-align: center;
        width: 100%;
    }

    .name {
        font-size: 56px;
        font-weight: 800;
        margin-bottom: 10px;
        letter-spacing: -1px;
    }

    .title {
        font-size: 24px;
        opacity: 0.95;
        margin-bottom: 15px;
    }

    .bio {
        font-size: 16px;
        opacity: 0.85;
        margin-bottom: 20px;
    }

    .info-grid {
        display: flex;
        justify-content: center;
        gap: 30px;
        flex-wrap: wrap;
        margin-top: 20px;
    }

    .info-item {
        background: rgba(255,255,255,0.2);
        padding: 8px 18px;
        border-radius: 25px;
        font-size: 14px;
    }

    /* Section Styles */
    .section {
        background: rgba(255,255,255,0.05);
        border-radius: 20px;
        padding: 30px;
        margin-bottom: 25px;
        backdrop-filter: blur(10px);
        border: 1px solid rgba(255,255,255,0.1);
        width: 100%;
    }

    .section-title {
        font-size: 28px;
        font-weight: 700;
        margin-bottom: 25px;
        padding-bottom: 10px;
        border-bottom: 3px solid #667eea;
        display: inline-block;
    }

    /* Academic Cards */
    .academic-card {
        background: rgba(255,255,255,0.08);
        border-radius: 15px;
        padding: 20px;
        margin-bottom: 20px;
    }

    .degree {
        font-size: 22px;
        font-weight: 700;
        color: #a8c0ff;
        margin-bottom: 8px;
    }

    .institution {
        font-size: 16px;
        color: #ccc;
        margin-bottom: 10px;
    }

    .stats {
        display: flex;
        gap: 20px;
        margin-top: 15px;
        flex-wrap: wrap;
    }

    .stat-badge {
        background: rgba(102,126,234,0.3);
        padding: 5px 12px;
        border-radius: 20px;
        font-size: 14px;
        font-weight: 600;
    }

    /* Skills Grid */
    .skills-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
        gap: 25px;
    }

    .skill-category {
        background: rgba(255,255,255,0.08);
        border-radius: 15px;
        padding: 20px;
    }

    .skill-category h3 {
        font-size: 20px;
        margin-bottom: 15px;
        color: #a8c0ff;
    }

    .skill-list {
        display: flex;
        flex-wrap: wrap;
        gap: 10px;
    }

    .skill-tag {
        background: rgba(102,126,234,0.3);
        padding: 6px 14px;
        border-radius: 20px;
        font-size: 13px;
        transition: transform 0.2s;
    }

    .skill-tag:hover {
        transform: translateY(-2px);
        background: rgba(102,126,234,0.5);
    }

    /* Sports Grid */
    .sports-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
        gap: 20px;
    }

    .sport-card {
        background: rgba(255,255,255,0.08);
        border-radius: 15px;
        padding: 20px;
        text-align: center;
    }

    .sport-icon {
        font-size: 48px;
        margin-bottom: 10px;
    }

    .sport-name {
        font-size: 20px;
        font-weight: 700;
        margin-bottom: 8px;
    }

    .sport-role {
        font-size: 14px;
        color: #a8c0ff;
        margin-bottom: 8px;
    }

    .sport-achievement {
        font-size: 12px;
        color: #ccc;
    }

    /* Habits List */
    .habits-list {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
        gap: 15px;
    }

    .habit-item {
        background: rgba(102,126,234,0.2);
        padding: 12px;
        border-radius: 10px;
        text-align: center;
        font-size: 14px;
    }

    /* Projects */
    .project-card {
        background: rgba(255,255,255,0.08);
        border-radius: 15px;
        padding: 20px;
        margin-bottom: 15px;
    }

    .project-name {
        font-size: 18px;
        font-weight: 700;
        margin-bottom: 5px;
    }

    .project-tech {
        font-size: 12px;
        color: #a8c0ff;
        margin-bottom: 10px;
    }

    /* Certification & Languages */
    .cert-list, .lang-list {
        list-style: none;
        padding: 0;
    }

    .cert-list li, .lang-list li {
        padding: 10px 0;
        border-bottom: 1px solid rgba(255,255,255,0.1);
    }

    /* Responsive */
    @media (max-width: 768px) {
        .container {
            padding: 20px 15px;
        }
        
        .name {
            font-size: 36px;
        }
        
        .title {
            font-size: 18px;
        }
        
        .section {
            padding: 20px;
        }
        
        .skills-grid {
            grid-template-columns: 1fr;
        }
        
        .header {
            padding: 30px 20px;
        }
        
        .info-grid {
            gap: 15px;
        }
        
        .info-item {
            font-size: 12px;
            padding: 6px 12px;
        }
    }

    /* For very small phones */
    @media (max-width: 480px) {
        .name {
            font-size: 28px;
        }
        
        .section-title {
            font-size: 22px;
        }
        
        .degree {
            font-size: 18px;
        }
    }

    /* Footer */
    .footer {
        text-align: center;
        padding: 30px;
        color: #888;
        font-size: 14px;
    }
</style>
</head>
<body>

<div class="container">
    <!-- Header -->
    <div class="header">
        <div class="name">⚡ Pranav Pinara ⚡</div>
        <div class="title">Computer Engineering Student • 2nd Semester</div>
        <div class="bio">Passionate about AI/ML • Web Development • Mobile Apps</div>
        <div class="info-grid">
            <div class="info-item">🎂 12th November 2009</div>
            <div class="info-item">📍 Ahmedabad, India</div>
            <div class="info-item">🎯 94% (10th) • 98% (Sem 1)</div>
        </div>
    </div>

    <!-- Academics -->
    <div class="section">
        <h2 class="section-title">📚 Education</h2>
        
        <div class="academic-card">
            <div class="degree">Diploma in Computer Engineering</div>
            <div class="institution">2nd Semester • Current CGPA: 9.8/10</div>
            <div class="stats">
                <span class="stat-badge">1st Semester: 98%</span>
                <span class="stat-badge">2nd Semester: In Progress</span>
            </div>
        </div>

        <div class="academic-card">
            <div class="degree">10th Grade (SSC)</div>
            <div class="institution">Board Examination • 2024</div>
            <div class="stats">
                <span class="stat-badge">Percentage: 94%</span>
                <span class="stat-badge">Distinction</span>
            </div>
        </div>
    </div>

    <!-- Technical Skills -->
    <div class="section">
        <h2 class="section-title">💻 Technical Skills</h2>
        <div class="skills-grid">
            <div class="skill-category">
                <h3>🤖 AI & Machine Learning</h3>
                <div class="skill-list">
                    <span class="skill-tag">Python</span>
                    <span class="skill-tag">TensorFlow Basics</span>
                    <span class="skill-tag">Data Science</span>
                    <span class="skill-tag">Neural Networks</span>
                </div>
            </div>
            
            <div class="skill-category">
                <h3>🌐 Web Development</h3>
                <div class="skill-list">
                    <span class="skill-tag">HTML5/CSS3</span>
                    <span class="skill-tag">JavaScript</span>
                    <span class="skill-tag">React.js</span>
                    <span class="skill-tag">Node.js</span>
                </div>
            </div>
            
            <div class="skill-category">
                <h3>📱 Mobile Development</h3>
                <div class="skill-list">
                    <span class="skill-tag">Flutter</span>
                    <span class="skill-tag">React Native</span>
                    <span class="skill-tag">Android Basics</span>
                </div>
            </div>
            
            <div class="skill-category">
                <h3>🗄️ Database</h3>
                <div class="skill-list">
                    <span class="skill-tag">MongoDB</span>
                    <span class="skill-tag">Firebase</span>
                    <span class="skill-tag">MySQL</span>
                </div>
            </div>
        </div>
    </div>

    <!-- Sports & Extracurricular -->
    <div class="section">
        <h2 class="section-title">🏆 Sports & Extracurricular</h2>
        <div class="sports-grid">
            <div class="sport-card">
                <div class="sport-icon">🏏</div>
                <div class="sport-name">Cricket</div>
                <div class="sport-role">All-rounder</div>
                <div class="sport-achievement">College Team • Best Batsman</div>
            </div>
            
            <div class="sport-card">
                <div class="sport-icon">🏐</div>
                <div class="sport-name">Volleyball</div>
                <div class="sport-role">Spiker</div>
                <div class="sport-achievement">Inter-college Participant</div>
            </div>
            
            <div class="sport-card">
                <div class="sport-icon">♟️</div>
                <div class="sport-name">Chess</div>
                <div class="sport-role">Strategic Player</div>
                <div class="sport-achievement">District Level Competitor</div>
            </div>
        </div>
    </div>

    <!-- Good Habits -->
    <div class="section">
        <h2 class="section-title">✅ Daily Discipline</h2>
        <div class="habits-list">
            <div class="habit-item">💻 Daily Coding (2+ hours)</div>
            <div class="habit-item">🌅 6 AM Wake-up Routine</div>
            <div class="habit-item">📚 Weekly Tech Reading</div>
            <div class="habit-item">🎯 LeetCode Problems</div>
            <div class="habit-item">🏃 Regular Fitness</div>
            <div class="habit-item">⏰ Time Management</div>
        </div>
    </div>

    <!-- Projects -->
    <div class="section">
        <h2 class="section-title">🚀 Featured Projects</h2>
        <div class="project-card">
            <div class="project-name">Portfolio Website</div>
            <div class="project-tech">HTML, CSS, JavaScript</div>
            <div class="project-desc">Personal portfolio showcasing skills and projects</div>
        </div>
        
        <div class="project-card">
            <div class="project-name">College Management System</div>
            <div class="project-tech">Python, Flask, MongoDB</div>
            <div class="project-desc">Student record management system</div>
        </div>
        
        <div class="project-card">
            <div class="project-name">Weather App</div>
            <div class="project-tech">React.js, API Integration</div>
            <div class="project-desc">Real-time weather application with forecast</div>
        </div>
    </div>

    <!-- Certifications -->
    <div class="section">
        <h2 class="section-title">📜 Certifications</h2>
        <ul class="cert-list">
            <li>🎓 Python for Everybody (In Progress)</li>
            <li>🎓 Web Development Bootcamp - 2025</li>
            <li>🎓 Introduction to AI (Coursera)</li>
        </ul>
    </div>

    <!-- Languages -->
    <div class="section">
        <h2 class="section-title">🌍 Languages</h2>
        <ul class="lang-list">
            <li>🇬🇧 English - Professional Working Proficiency</li>
            <li>🇮🇳 Hindi - Native</li>
            <li>🇮🇳 Gujarati - Native</li>
        </ul>
    </div>

    <!-- Footer -->
    <div class="footer">
        ⚡ Built with precision • Portfolio of Pranav Pinara ⚡
    </div>
</div>

<script>
    // Smooth scroll and simple animations
    const sections = document.querySelectorAll('.section');
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if(entry.isIntersecting) {
                entry.target.style.opacity = '1';
                entry.target.style.transform = 'translateY(0)';
            }
        });
    }, {threshold: 0.1});
    
    sections.forEach(section => {
        section.style.opacity = '0';
        section.style.transform = 'translateY(20px)';
        section.style.transition = 'all 0.6s ease';
        observer.observe(section);
    });
</script>

</body>
</html>
"""

# Use full container width without any padding
st.components.v1.html(html, height=1200, scrolling=True)
