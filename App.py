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
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        .stApp { margin: 0; padding: 0; }
        .stApp > header { display: none !important; }
        .main .block-container { padding: 0 !important; max-width: 100% !important; }
        .stApp { margin-top: -60px; }
        .element-container, .stMarkdown, .stMarkdown div { margin: 0; padding: 0; }
    </style>
""", unsafe_allow_html=True)

html = r"""
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Pranav Pinara • Portfolio</title>
<style>
    * { margin: 0; padding: 0; box-sizing: border-box; }
    
    body {
        font-family: 'Segoe UI', -apple-system, BlinkMacSystemFont, sans-serif;
        background: #0f0c29;
        color: #fff;
        line-height: 1.5;
    }
    
    .container {
        max-width: 1200px;
        margin: 0 auto;
        padding: 30px 20px;
    }
    
    /* Header */
    .header {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        border-radius: 20px;
        padding: 40px;
        margin-bottom: 30px;
        text-align: center;
    }
    
    .name {
        font-size: 48px;
        font-weight: 800;
        margin-bottom: 10px;
    }
    
    .title {
        font-size: 20px;
        opacity: 0.95;
        margin-bottom: 20px;
    }
    
    .info-row {
        display: flex;
        justify-content: center;
        gap: 20px;
        flex-wrap: wrap;
        margin-top: 15px;
    }
    
    .info-badge {
        background: rgba(255,255,255,0.2);
        padding: 6px 16px;
        border-radius: 25px;
        font-size: 14px;
    }
    
    /* Sections */
    .section {
        background: rgba(255,255,255,0.05);
        border-radius: 16px;
        padding: 25px;
        margin-bottom: 25px;
        backdrop-filter: blur(10px);
        border: 1px solid rgba(255,255,255,0.1);
    }
    
    .section-title {
        font-size: 24px;
        font-weight: 700;
        margin-bottom: 20px;
        padding-bottom: 8px;
        border-bottom: 2px solid #667eea;
        display: inline-block;
    }
    
    /* Education */
    .edu-card {
        background: rgba(255,255,255,0.08);
        border-radius: 12px;
        padding: 18px;
        margin-bottom: 15px;
    }
    
    .edu-degree {
        font-size: 20px;
        font-weight: 700;
        color: #a8c0ff;
    }
    
    .edu-details {
        display: flex;
        gap: 20px;
        margin-top: 10px;
        flex-wrap: wrap;
    }
    
    .edu-badge {
        background: rgba(102,126,234,0.3);
        padding: 4px 12px;
        border-radius: 20px;
        font-size: 13px;
    }
    
    /* Skills Grid */
    .skills-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
        gap: 20px;
    }
    
    .skill-cat {
        background: rgba(255,255,255,0.08);
        border-radius: 12px;
        padding: 18px;
    }
    
    .skill-cat h3 {
        font-size: 18px;
        margin-bottom: 12px;
        color: #a8c0ff;
    }
    
    .skill-tags {
        display: flex;
        flex-wrap: wrap;
        gap: 8px;
    }
    
    .skill-tag {
        background: rgba(102,126,234,0.3);
        padding: 5px 12px;
        border-radius: 20px;
        font-size: 12px;
    }
    
    /* Projects */
    .project-card {
        background: rgba(255,255,255,0.08);
        border-radius: 12px;
        padding: 18px;
        margin-bottom: 15px;
    }
    
    .project-name {
        font-size: 18px;
        font-weight: 700;
        color: #a8c0ff;
    }
    
    .project-tech {
        font-size: 12px;
        color: #ff9a9e;
        margin: 5px 0 8px 0;
    }
    
    /* Sports */
    .sports-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
        gap: 15px;
    }
    
    .sport-card {
        background: rgba(255,255,255,0.08);
        border-radius: 12px;
        padding: 15px;
        text-align: center;
    }
    
    .sport-icon {
        font-size: 36px;
    }
    
    .sport-name {
        font-size: 16px;
        font-weight: 700;
        margin: 8px 0 4px 0;
    }
    
    /* Lists */
    .habit-list, .cert-list {
        display: flex;
        flex-wrap: wrap;
        gap: 10px;
        list-style: none;
    }
    
    .habit-list li, .cert-list li {
        background: rgba(102,126,234,0.2);
        padding: 6px 14px;
        border-radius: 20px;
        font-size: 13px;
    }
    
    /* Footer */
    .footer {
        text-align: center;
        padding: 20px;
        color: #888;
        font-size: 13px;
    }
    
    @media (max-width: 768px) {
        .name { font-size: 32px; }
        .header { padding: 25px; }
        .section { padding: 18px; }
        .skills-grid { grid-template-columns: 1fr; }
    }
</style>
</head>
<body>

<div class="container">
    <!-- Header -->
    <div class="header">
        <div class="name">⚡ Pranav Pinara ⚡</div>
        <div class="title">Computer Engineering Student | Aspiring AI/ML Engineer</div>
        <div class="info-row">
            <div class="info-badge">🎂 12 Nov 2009</div>
            <div class="info-badge">📍 Ahmedabad, India</div>
            <div class="info-badge">📧 pranav.Pinara@student.edu</div>
        </div>
    </div>

    <!-- Education -->
    <div class="section">
        <h2 class="section-title">🎓 Education</h2>
        <div class="edu-card">
            <div class="edu-degree">Diploma in Computer Engineering</div>
            <div>2nd Semester • Current CGPA: 9.8/10</div>
            <div class="edu-details">
                <span class="edu-badge">Semester 1: 98%</span>
                <span class="edu-badge">Semester 2: Ongoing</span>
            </div>
        </div>
        <div class="edu-card">
            <div class="edu-degree">10th Grade (SSC)</div>
            <div>Board Examination • 2024</div>
            <div class="edu-details">
                <span class="edu-badge">94% • Distinction</span>
            </div>
        </div>
    </div>

    <!-- Technical Skills -->
    <div class="section">
        <h2 class="section-title">💻 Technical Skills</h2>
        <div class="skills-grid">
            <div class="skill-cat">
                <h3>🤖 AI/ML</h3>
                <div class="skill-tags">
                    <span class="skill-tag">Python</span>
                    <span class="skill-tag">TensorFlow</span>
                    <span class="skill-tag">Data Science</span>
                    <span class="skill-tag">Neural Networks</span>
                </div>
            </div>
            <div class="skill-cat">
                <h3>🌐 Web Dev</h3>
                <div class="skill-tags">
                    <span class="skill-tag">React.js</span>
                    <span class="skill-tag">Node.js</span>
                    <span class="skill-tag">JavaScript</span>
                    <span class="skill-tag">HTML/CSS</span>
                </div>
            </div>
            <div class="skill-cat">
                <h3>📱 Mobile</h3>
                <div class="skill-tags">
                    <span class="skill-tag">Flutter</span>
                    <span class="skill-tag">React Native</span>
                    <span class="skill-tag">Android</span>
                </div>
            </div>
            <div class="skill-cat">
                <h3>🗄️ Database & Tools</h3>
                <div class="skill-tags">
                    <span class="skill-tag">MongoDB</span>
                    <span class="skill-tag">Firebase</span>
                    <span class="skill-tag">Git</span>
                    <span class="skill-tag">Docker</span>
                </div>
            </div>
        </div>
    </div>

    <!-- Soft Skills -->
    <div class="section">
        <h2 class="section-title">💼 Professional Skills</h2>
        <div class="skills-grid">
            <div class="skill-cat">
                <h3>🗣️ Communication</h3>
                <div class="skill-tags">
                    <span class="skill-tag">Fluent English</span>
                    <span class="skill-tag">Presentation</span>
                    <span class="skill-tag">Public Speaking</span>
                </div>
            </div>
            <div class="skill-cat">
                <h3>👥 Leadership</h3>
                <div class="skill-tags">
                    <span class="skill-tag">Team Management</span>
                    <span class="skill-tag">Project Coordination</span>
                    <span class="skill-tag">Mentoring</span>
                </div>
            </div>
            <div class="skill-cat">
                <h3>⚡ Personal</h3>
                <div class="skill-tags">
                    <span class="skill-tag">Problem Solving</span>
                    <span class="skill-tag">Quick Learner</span>
                    <span class="skill-tag">Time Management</span>
                </div>
            </div>
        </div>
    </div>

    <!-- Projects -->
    <div class="section">
        <h2 class="section-title">🚀 Projects</h2>
        <div class="project-card">
            <div class="project-name">Personal Portfolio</div>
            <div class="project-tech">React.js • HTML/CSS • JavaScript</div>
            <div>Modern responsive portfolio showcasing skills and work</div>
        </div>
        <div class="project-card">
            <div class="project-name">Student Management System</div>
            <div class="project-tech">Python • Flask • MongoDB</div>
            <div>Complete CRUD application for student records</div>
        </div>
        <div class="project-card">
            <div class="project-name">Weather Forecast App</div>
            <div class="project-tech">React.js • OpenWeather API</div>
            <div>Real-time weather with 7-day forecast</div>
        </div>
        <div class="project-card">
            <div class="project-name">Real-time Chat App</div>
            <div class="project-tech">Node.js • Socket.io • Express</div>
            <div>Multi-room chat with authentication</div>
        </div>
    </div>

    <!-- Sports & Achievements -->
    <div class="section">
        <h2 class="section-title">🏆 Sports & Achievements</h2>
        <div class="sports-grid">
            <div class="sport-card">
                <div class="sport-icon">🏏</div>
                <div class="sport-name">Cricket</div>
                <div style="font-size: 12px; opacity: 0.8;">All-rounder • College Team</div>
            </div>
            <div class="sport-card">
                <div class="sport-icon">🏐</div>
                <div class="sport-name">Volleyball</div>
                <div style="font-size: 12px; opacity: 0.8;">Spiker • Tournament Player</div>
            </div>
            <div class="sport-card">
                <div class="sport-icon">♟️</div>
                <div class="sport-name">Chess</div>
                <div style="font-size: 12px; opacity: 0.8;">District Level • School Champion</div>
            </div>
        </div>
    </div>

    <!-- Daily Habits -->
    <div class="section">
        <h2 class="section-title">✅ Daily Discipline</h2>
        <ul class="habit-list">
            <li>💻 Daily Coding (2+ hrs)</li>
            <li>🌅 6 AM Wake-up</li>
            <li>🎯 LeetCode Practice</li>
            <li>🏃 Regular Fitness</li>
            <li>📚 Tech Reading</li>
            <li>⏰ Time Management</li>
        </ul>
    </div>

    <!-- Certifications -->
    <div class="section">
        <h2 class="section-title">📜 Certifications</h2>
        <ul class="cert-list">
            <li>Python for Everybody - Coursera</li>
            <li>Web Development Bootcamp 2025</li>
            <li>Introduction to AI - Coursera</li>
            <li>Data Science Fundamentals - IBM</li>
        </ul>
    </div>

    <!-- Footer -->
    <div class="footer">
        ⚡ Open for internships • Available for opportunities • Pranav Pinara ⚡
    </div>
</div>

<script>
    // Scroll animations
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
        section.style.transition = 'all 0.5s ease';
        observer.observe(section);
    });
</script>

</body>
</html>
"""

st.components.v1.html(html, height=1200, scrolling=True)
