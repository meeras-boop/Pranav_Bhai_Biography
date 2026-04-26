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
    "AI & ML": ["Python", "TensorFlow Basics", "Data Science Fundamentals", "Neural Networks", "Pandas", "NumPy"],
    "Web Development": ["HTML5", "CSS3", "JavaScript", "React.js", "Node.js", "Bootstrap", "Tailwind CSS"],
    "Mobile Development": ["Flutter", "React Native", "Android Basics", "iOS Basics"],
    "Database": ["MongoDB", "Firebase", "MySQL", "PostgreSQL Basics"],
    "Tools & Others": ["Git", "VS Code", "Figma", "Postman", "Docker Basics", "Linux/Ubuntu"]
}

# Soft Skills (New Addition)
soft_skills = {
    "Communication": [
        "Excellent verbal and written communication",
        "English Medium Education - Fluent in English",
        "Presentation skills",
        "Public speaking",
        "Active listening"
    ],
    "Leadership & Teamwork": [
        "Team leadership",
        "Collaborative problem solving",
        "Project coordination",
        "Mentoring juniors",
        "Conflict resolution"
    ],
    "Personal Attributes": [
        "Quick learner",
        "Adaptability",
        "Time management",
        "Attention to detail",
        "Critical thinking",
        "Problem-solving mindset",
        "Self-motivated",
        "Disciplined approach"
    ],
    "Interpersonal": [
        "Empathy and emotional intelligence",
        "Networking skills",
        "Cross-cultural communication",
        "Negotiation skills",
        "Feedback reception"
    ]
}

# Sports & Extracurricular
sports = [
    {"name": "Cricket", "role": "All-rounder", "achievement": "College Team Member • Best Batsman Award • School Captain"},
    {"name": "Volleyball", "role": "Spiker", "achievement": "Inter-college Tournament Participant • Best Spiker Award"},
    {"name": "Chess", "role": "Strategic Player", "achievement": "District Level Competitor • School Champion"}
]

# Good Habits (Professional)
habits = [
    "Daily coding practice (2+ hours)",
    "Morning routine: 6 AM wake-up",
    "Weekly tech blog reading (Medium, Dev.to)",
    "Problem-solving on LeetCode (50+ problems solved)",
    "Regular fitness & sports (5 days/week)",
    "Time management & planning using Notion",
    "Reading books (Technical & Self-help)",
    "Learning new technologies every month",
    "Participating in hackathons",
    "Teaching concepts to peers"
]

# Projects
projects = [
    {
        "name": "Personal Portfolio Website",
        "tech": "HTML5, CSS3, JavaScript, React.js",
        "desc": "Modern responsive portfolio showcasing skills, projects, and achievements"
    },
    {
        "name": "Student Management System",
        "tech": "Python, Flask, MongoDB, Bootstrap",
        "desc": "Complete CRUD application for managing student records and attendance"
    },
    {
        "name": "Weather Forecast App",
        "tech": "React.js, OpenWeather API, Axios",
        "desc": "Real-time weather application with 7-day forecast and location detection"
    },
    {
        "name": "Chat Application",
        "tech": "Node.js, Socket.io, Express",
        "desc": "Real-time chat app with multiple rooms and user authentication"
    }
]

# Certifications
certifications = [
    "Python for Everybody (Coursera) - In Progress",
    "The Complete Web Development Bootcamp 2025",
    "Introduction to Artificial Intelligence (Coursera)",
    "English Communication Skills Certificate",
    "Leadership & Team Management Workshop",
    "Data Science Fundamentals (IBM)"
]

# Languages
languages = [
    {"lang": "English", "level": "Fluent (C1) - Professional Working Proficiency", "medium": "English Medium Education"},
    {"lang": "Hindi", "level": "Native (C2)"},
    {"lang": "Gujarati", "level": "Native (C2)"}
]

html = r"""
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0, user-scalable=yes">
<title>Pranav Pinara • Professional Portfolio</title>
<style>
    * {
        margin: 0;
        padding: 0;
        box-sizing: border-box;
    }

    body {
        font-family: 'Segoe UI', 'Poppins', -apple-system, BlinkMacSystemFont, sans-serif;
        background: linear-gradient(135deg, #0a0e27 0%, #1a1a3e 100%);
        color: #fff;
        line-height: 1.6;
        overflow-x: hidden;
        width: 100%;
        min-height: 100vh;
    }

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
        animation: slideDown 0.8s ease;
    }

    @keyframes slideDown {
        from {
            opacity: 0;
            transform: translateY(-30px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
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
        transition: transform 0.2s;
    }

    .info-item:hover {
        transform: translateY(-2px);
        background: rgba(255,255,255,0.3);
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
        transition: all 0.3s ease;
    }

    .section:hover {
        transform: translateY(-5px);
        background: rgba(255,255,255,0.08);
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
        transition: transform 0.2s;
    }

    .academic-card:hover {
        transform: translateX(5px);
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
        grid-template-columns: repeat(auto-fit, minmax(350px, 1fr));
        gap: 25px;
    }

    .skill-category {
        background: rgba(255,255,255,0.08);
        border-radius: 15px;
        padding: 20px;
        transition: transform 0.2s;
    }

    .skill-category:hover {
        transform: translateY(-5px);
        background: rgba(255,255,255,0.12);
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
        transition: all 0.2s;
    }

    .skill-tag:hover {
        transform: translateY(-2px);
        background: rgba(102,126,234,0.6);
        cursor: default;
    }

    /* Soft Skills Specific */
    .soft-skill-item {
        background: rgba(102,126,234,0.2);
        padding: 8px 12px;
        border-radius: 10px;
        font-size: 13px;
        margin: 5px;
        display: inline-block;
        transition: all 0.2s;
    }

    .soft-skill-item:hover {
        transform: translateY(-2px);
        background: rgba(102,126,234,0.4);
    }

    /* Sports Grid */
    .sports-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
        gap: 20px;
    }

    .sport-card {
        background: rgba(255,255,255,0.08);
        border-radius: 15px;
        padding: 20px;
        text-align: center;
        transition: transform 0.2s;
    }

    .sport-card:hover {
        transform: translateY(-5px);
        background: rgba(255,255,255,0.12);
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
        grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
        gap: 15px;
    }

    .habit-item {
        background: rgba(102,126,234,0.2);
        padding: 12px;
        border-radius: 10px;
        text-align: center;
        font-size: 14px;
        transition: transform 0.2s;
    }

    .habit-item:hover {
        transform: translateY(-3px);
        background: rgba(102,126,234,0.3);
    }

    /* Projects */
    .project-card {
        background: rgba(255,255,255,0.08);
        border-radius: 15px;
        padding: 20px;
        margin-bottom: 15px;
        transition: transform 0.2s;
    }

    .project-card:hover {
        transform: translateX(5px);
        background: rgba(255,255,255,0.12);
    }

    .project-name {
        font-size: 18px;
        font-weight: 700;
        margin-bottom: 5px;
        color: #a8c0ff;
    }

    .project-tech {
        font-size: 12px;
        color: #ff9a9e;
        margin-bottom: 10px;
    }

    .project-desc {
        font-size: 14px;
        color: #ddd;
    }

    /* Certification & Languages */
    .cert-list, .lang-list {
        list-style: none;
        padding: 0;
    }

    .cert-list li, .lang-list li {
        padding: 12px 0;
        border-bottom: 1px solid rgba(255,255,255,0.1);
        transition: transform 0.2s;
    }

    .cert-list li:hover, .lang-list li:hover {
        transform: translateX(5px);
        color: #a8c0ff;
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

        .habits-list {
            grid-template-columns: 1fr;
        }
    }

    /* Footer */
    .footer {
        text-align: center;
        padding: 30px;
        color: #888;
        font-size: 14px;
        border-top: 1px solid rgba(255,255,255,0.1);
        margin-top: 20px;
    }
</style>
</head>
<body>

<div class="container">
    <!-- Header -->
    <div class="header">
        <div class="name">⚡ Pranav Pinara ⚡</div>
        <div class="title">Computer Engineering Student • 2nd Semester</div>
        <div class="bio">Passionate about AI/ML • Web Development • Mobile Apps • Leadership</div>
        <div class="info-grid">
            <div class="info-item">🎂 12th November 2009</div>
            <div class="info-item">📍 Ahmedabad, India</div>
            <div class="info-item">🎯 94% (10th) • 98% (Sem 1)</div>
            <div class="info-item">🗣️ English Medium • Fluent</div>
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
            <div class="institution">Board Examination • 2024 • English Medium</div>
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
                    <span class="skill-tag">Pandas/NumPy</span>
                </div>
            </div>
            
            <div class="skill-category">
                <h3>🌐 Web Development</h3>
                <div class="skill-list">
                    <span class="skill-tag">HTML5/CSS3</span>
                    <span class="skill-tag">JavaScript</span>
                    <span class="skill-tag">React.js</span>
                    <span class="skill-tag">Node.js</span>
                    <span class="skill-tag">Bootstrap/Tailwind</span>
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
                <h3>🗄️ Database & Tools</h3>
                <div class="skill-list">
                    <span class="skill-tag">MongoDB</span>
                    <span class="skill-tag">Firebase</span>
                    <span class="skill-tag">MySQL</span>
                    <span class="skill-tag">Git/GitHub</span>
                    <span class="skill-tag">Docker Basics</span>
                </div>
            </div>
        </div>
    </div>

    <!-- Soft Skills (New Section) -->
    <div class="section">
        <h2 class="section-title">💼 Professional & Soft Skills</h2>
        <div class="skills-grid">
            <div class="skill-category">
                <h3>🗣️ Communication</h3>
                <div>
                    <span class="soft-skill-item">✅ English Medium Education</span>
                    <span class="soft-skill-item">✅ Fluent in English (C1 Level)</span>
                    <span class="soft-skill-item">✅ Excellent Verbal & Written</span>
                    <span class="soft-skill-item">✅ Presentation Skills</span>
                    <span class="soft-skill-item">✅ Public Speaking</span>
                    <span class="soft-skill-item">✅ Active Listening</span>
                </div>
            </div>
            
            <div class="skill-category">
                <h3>👥 Leadership & Teamwork</h3>
                <div>
                    <span class="soft-skill-item">✅ Team Leadership</span>
                    <span class="soft-skill-item">✅ Collaborative Problem Solving</span>
                    <span class="soft-skill-item">✅ Project Coordination</span>
                    <span class="soft-skill-item">✅ Mentoring</span>
                    <span class="soft-skill-item">✅ Conflict Resolution</span>
                </div>
            </div>
            
            <div class="skill-category">
                <h3>⚡ Personal Attributes</h3>
                <div>
                    <span class="soft-skill-item">✅ Quick Learner</span>
                    <span class="soft-skill-item">✅ Adaptability</span>
                    <span class="soft-skill-item">✅ Time Management</span>
                    <span class="soft-skill-item">✅ Attention to Detail</span>
                    <span class="soft-skill-item">✅ Critical Thinking</span>
                    <span class="soft-skill-item">✅ Self-Motivated</span>
                    <span class="soft-skill-item">✅ Disciplined Approach</span>
                </div>
            </div>
            
            <div class="skill-category">
                <h3>💡 Interpersonal</h3>
                <div>
                    <span class="soft-skill-item">✅ Empathy & Emotional Intelligence</span>
                    <span class="soft-skill-item">✅ Networking Skills</span>
                    <span class="soft-skill-item">✅ Cross-cultural Communication</span>
                    <span class="soft-skill-item">✅ Negotiation Skills</span>
                    <span class="soft-skill-item">✅ Feedback Reception & Growth</span>
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
                <div class="sport-achievement">College Team • Best Batsman • School Captain</div>
            </div>
            
            <div class="sport-card">
                <div class="sport-icon">🏐</div>
                <div class="sport-name">Volleyball</div>
                <div class="sport-role">Spiker</div>
                <div class="sport-achievement">Inter-college Participant • Best Spiker Award</div>
            </div>
            
            <div class="sport-card">
                <div class="sport-icon">♟️</div>
                <div class="sport-name">Chess</div>
                <div class="sport-role">Strategic Player</div>
                <div class="sport-achievement">District Level Competitor • School Champion</div>
            </div>
        </div>
    </div>

    <!-- Good Habits -->
    <div class="section">
        <h2 class="section-title">✅ Daily Discipline & Habits</h2>
        <div class="habits-list">
            <div class="habit-item">💻 Daily Coding (2+ hours)</div>
            <div class="habit-item">🌅 6 AM Wake-up Routine</div>
            <div class="habit-item">📚 Weekly Tech Reading</div>
            <div class="habit-item">🎯 LeetCode Problems (50+ solved)</div>
            <div class="habit-item">🏃 Regular Fitness (5 days/week)</div>
            <div class="habit-item">⏰ Time Management with Notion</div>
            <div class="habit-item">📖 Reading Books (Tech + Self-help)</div>
            <div class="habit-item">🚀 Learning New Tech Monthly</div>
            <div class="habit-item">💡 Participating in Hackathons</div>
            <div class="habit-item">👨‍🏫 Teaching Concepts to Peers</div>
        </div>
    </div>

    <!-- Projects -->
    <div class="section">
        <h2 class="section-title">🚀 Featured Projects</h2>
        <div class="project-card">
            <div class="project-name">Personal Portfolio Website</div>
            <div class="project-tech">React.js, HTML5, CSS3, JavaScript</div>
            <div class="project-desc">Modern responsive portfolio showcasing skills, projects, and achievements</div>
        </div>
        
        <div class="project-card">
            <div class="project-name">Student Management System</div>
            <div class="project-tech">Python, Flask, MongoDB, Bootstrap</div>
            <div class="project-desc">Complete CRUD application for managing student records and attendance</div>
        </div>
        
        <div class="project-card">
            <div class="project-name">Weather Forecast App</div>
            <div class="project-tech">React.js, OpenWeather API, Axios</div>
            <div class="project-desc">Real-time weather application with 7-day forecast and location detection</div>
        </div>
        
        <div class="project-card">
            <div class="project-name">Real-time Chat Application</div>
            <div class="project-tech">Node.js, Socket.io, Express</div>
            <div class="project-desc">Real-time chat app with multiple rooms and user authentication</div>
        </div>
    </div>

    <!-- Certifications -->
    <div class="section">
        <h2 class="section-title">📜 Certifications</h2>
        <ul class="cert-list">
            <li>🎓 Python for Everybody (Coursera) - In Progress</li>
            <li>🎓 The Complete Web Development Bootcamp 2025</li>
            <li>🎓 Introduction to Artificial Intelligence (Coursera)</li>
            <li>🎓 English Communication Skills Certificate</li>
            <li>🎓 Leadership & Team Management Workshop</li>
            <li>🎓 Data Science Fundamentals (IBM)</li>
        </ul>
    </div>

    <!-- Languages -->
    <div class="section">
        <h2 class="section-title">🌍 Languages</h2>
        <ul class="lang-list">
            <li>🇬🇧 English - Fluent (C1 Level) • English Medium Education</li>
            <li>🇮🇳 Hindi - Native (C2 Level)</li>
            <li>🇮🇳 Gujarati - Native (C2 Level)</li>
        </ul>
    </div>

    <!-- Footer -->
    <div class="footer">
        ⚡ Built with precision • Always learning, always growing • Portfolio of Pranav Pinara ⚡
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
st.components.v1.html(html, height=1400, scrolling=True)
