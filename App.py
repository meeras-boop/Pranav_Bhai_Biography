import json
import streamlit as st

st.set_page_config(page_title="✨ Pranav's Journey ✨ — Computer Engineer", layout="wide")

# Pranav's Biography Data (No images needed!)
milestones = [
    {
        "id": "birth",
        "title": "🌟 The Beginning",
        "date": "Born",
        "desc": "A star was born! From day one, curiosity was his superpower. Little did we know, a tech genius was in the making!",
        "icon": "👶",
        "gradient": "linear-gradient(135deg, #667eea 0%, #764ba2 100%)"
    },
    {
        "id": "school",
        "title": "📚 School Days",
        "date": "1st - 10th Grade",
        "desc": "Always curious about how things work. Loved mathematics and science! Teachers always praised his logical thinking.",
        "icon": "🏫",
        "gradient": "linear-gradient(135deg, #f093fb 0%, #f5576c 100%)"
    },
    {
        "id": "class10",
        "title": "🏆 10th Grade Scorer",
        "date": "Brilliant Achievement",
        "desc": "Scored exceptional marks in 10th! Proved that hard work, dedication, and smart study always pay off. So proud of you, bhai! 🎉",
        "icon": "🎯",
        "gradient": "linear-gradient(135deg, #fa709a 0%, #fee140 100%)"
    },
    {
        "id": "diploma",
        "title": "💻 Diploma Journey",
        "date": "Computer Engineering - 2nd Sem",
        "desc": "Currently pursuing Diploma in Computer Engineering. Learning programming, data structures, and building a strong foundation in tech!",
        "icon": "🎓",
        "gradient": "linear-gradient(135deg, #a8edea 0%, #fed6e3 100%)"
    },
    {
        "id": "aiml",
        "title": "🤖 AI/ML Explorer",
        "date": "Passion Project",
        "desc": "Deeply interested in Artificial Intelligence and Machine Learning. Exploring neural networks, data science, and creating intelligent systems!",
        "icon": "🧠",
        "gradient": "linear-gradient(135deg, #ff9a9e 0%, #fecfef 100%)"
    },
    {
        "id": "webdev",
        "title": "🌐 Web Developer",
        "date": "Full Stack Enthusiast",
        "desc": "Creating amazing websites and web applications. Mastering HTML, CSS, JavaScript, React, and backend technologies!",
        "icon": "💻",
        "gradient": "linear-gradient(135deg, #a1c4fd 0%, #c2e9fb 100%)"
    },
    {
        "id": "mobile",
        "title": "📱 Mobile Apps",
        "date": "App Development",
        "desc": "Building mobile applications that make life easier. Learning Flutter, React Native, and native app development!",
        "icon": "📱",
        "gradient": "linear-gradient(135deg, #ffecd2 0%, #fcb69f 100%)"
    },
    {
        "id": "skills",
        "title": "⚡ Tech Stack",
        "date": "Skills & Tools",
        "desc": "Python • JavaScript • React • Node.js • Flutter • TensorFlow • Firebase • MongoDB • and counting...",
        "icon": "🔧",
        "gradient": "linear-gradient(135deg, #ff9a9e 0%, #fecfef 100%)"
    },
    {
        "id": "dreams",
        "title": "🚀 Big Dreams",
        "date": "Future Vision",
        "desc": "Aiming to become a top tech innovator, build impactful products, and make the family proud! The sky is not the limit!",
        "icon": "⭐",
        "gradient": "linear-gradient(135deg, #ffd1ff 0%, #ff9a9e 100%)"
    }
]

# Tech stack icons for visual flair
tech_icons = ["🐍", "⚛️", "🟨", "☕", "📱", "🤖", "🗄️", "☁️", "🎨", "🔧", "💡", "⚡"]

html = r"""
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=yes">
<title>✨ Pranav's Tech Journey ✨</title>
<style>
    * {
        margin: 0;
        padding: 0;
        box-sizing: border-box;
    }

    body {
        font-family: 'Segoe UI', 'Poppins', -apple-system, BlinkMacSystemFont, 'Inter', sans-serif;
        background: linear-gradient(135deg, #0f0c29, #302b63, #24243e);
        min-height: 100vh;
        overflow-x: hidden;
        color: #fff;
        position: relative;
    }

    /* Animated gradient background */
    body::before {
        content: '';
        position: fixed;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background: radial-gradient(circle at 20% 50%, rgba(102, 126, 234, 0.3), transparent 50%),
                    radial-gradient(circle at 80% 80%, rgba(118, 75, 162, 0.3), transparent 50%),
                    radial-gradient(circle at 40% 20%, rgba(255, 80, 120, 0.2), transparent 50%);
        pointer-events: none;
        z-index: 0;
        animation: gradientShift 10s ease infinite;
    }

    @keyframes gradientShift {
        0%, 100% { opacity: 0.5; }
        50% { opacity: 1; }
    }

    /* Floating shapes */
    .floating-shape {
        position: fixed;
        pointer-events: none;
        z-index: 0;
        opacity: 0.1;
        animation: float 20s infinite linear;
    }

    @keyframes float {
        0% {
            transform: translate(0, 0) rotate(0deg);
        }
        100% {
            transform: translate(100px, 100px) rotate(360deg);
        }
    }

    .container {
        max-width: 1300px;
        margin: 0 auto;
        padding: 20px;
        position: relative;
        z-index: 2;
    }

    /* Hero Section */
    .hero {
        text-align: center;
        padding: 60px 20px 40px;
        margin-bottom: 50px;
        position: relative;
    }

    .glow-text {
        font-size: 70px;
        font-weight: bold;
        background: linear-gradient(135deg, #fff, #a8c0ff, #3f2b96);
        -webkit-background-clip: text;
        background-clip: text;
        color: transparent;
        animation: glow 3s ease-in-out infinite;
        text-shadow: 0 0 30px rgba(102, 126, 234, 0.5);
        margin-bottom: 20px;
    }

    @keyframes glow {
        0%, 100% { opacity: 1; }
        50% { opacity: 0.8; text-shadow: 0 0 50px rgba(102, 126, 234, 0.8); }
    }

    .hero-subtitle {
        font-size: 24px;
        color: rgba(255,255,255,0.9);
        margin-bottom: 30px;
    }

    .tech-strip {
        display: flex;
        justify-content: center;
        gap: 20px;
        flex-wrap: wrap;
        padding: 20px;
        background: rgba(255,255,255,0.1);
        border-radius: 60px;
        backdrop-filter: blur(10px);
        margin-top: 30px;
    }

    .tech-icon {
        font-size: 32px;
        animation: bounce 2s ease infinite;
        display: inline-block;
        cursor: default;
    }

    @keyframes bounce {
        0%, 100% { transform: translateY(0); }
        50% { transform: translateY(-10px); }
    }

    /* Stats Section */
    .stats {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
        gap: 20px;
        margin: 50px 0;
    }

    .stat-card {
        background: rgba(255,255,255,0.1);
        backdrop-filter: blur(10px);
        border-radius: 20px;
        padding: 25px;
        text-align: center;
        transition: transform 0.3s;
        border: 1px solid rgba(255,255,255,0.2);
    }

    .stat-card:hover {
        transform: translateY(-5px);
        background: rgba(255,255,255,0.15);
    }

    .stat-number {
        font-size: 48px;
        font-weight: bold;
        background: linear-gradient(135deg, #ff9a9e, #fecfef);
        -webkit-background-clip: text;
        background-clip: text;
        color: transparent;
    }

    .stat-label {
        font-size: 14px;
        margin-top: 10px;
        opacity: 0.8;
    }

    /* Timeline Grid */
    .timeline-title {
        text-align: center;
        font-size: 42px;
        margin: 50px 0 30px;
        background: linear-gradient(135deg, #fff, #a8c0ff);
        -webkit-background-clip: text;
        background-clip: text;
        color: transparent;
    }

    .timeline-grid {
        display: grid;
        grid-template-columns: repeat(auto-fill, minmax(350px, 1fr));
        gap: 25px;
        margin-bottom: 50px;
    }

    .milestone-card {
        background: rgba(255,255,255,0.1);
        backdrop-filter: blur(10px);
        border-radius: 25px;
        padding: 25px;
        cursor: pointer;
        transition: all 0.3s ease;
        border: 1px solid rgba(255,255,255,0.2);
        animation: cardSlide 0.6s ease backwards;
    }

    @keyframes cardSlide {
        from {
            opacity: 0;
            transform: translateY(30px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }

    .milestone-card:hover {
        transform: translateY(-10px) scale(1.02);
        background: rgba(255,255,255,0.15);
        border-color: rgba(255,255,255,0.4);
        box-shadow: 0 20px 40px rgba(0,0,0,0.3);
    }

    .card-icon {
        font-size: 60px;
        margin-bottom: 15px;
        display: inline-block;
    }

    .card-title {
        font-size: 24px;
        font-weight: bold;
        margin-bottom: 10px;
        color: #fff;
    }

    .card-date {
        display: inline-block;
        padding: 5px 15px;
        background: rgba(255,255,255,0.2);
        border-radius: 20px;
        font-size: 12px;
        margin-bottom: 15px;
    }

    .card-desc {
        color: rgba(255,255,255,0.8);
        line-height: 1.6;
        font-size: 14px;
    }

    /* Modal */
    .modal {
        display: none;
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background: rgba(0,0,0,0.8);
        backdrop-filter: blur(20px);
        z-index: 1000;
        justify-content: center;
        align-items: center;
        animation: fadeIn 0.3s ease;
    }

    @keyframes fadeIn {
        from { opacity: 0; }
        to { opacity: 1; }
    }

    .modal-content {
        background: linear-gradient(135deg, rgba(255,255,255,0.95), rgba(255,255,255,0.98));
        border-radius: 40px;
        max-width: 500px;
        width: 90%;
        padding: 40px;
        text-align: center;
        animation: scaleIn 0.4s cubic-bezier(0.68, -0.55, 0.265, 1.55);
        position: relative;
    }

    @keyframes scaleIn {
        from {
            transform: scale(0.8);
            opacity: 0;
        }
        to {
            transform: scale(1);
            opacity: 1;
        }
    }

    .modal-icon {
        font-size: 80px;
        margin-bottom: 20px;
        animation: bounce 0.5s ease;
    }

    .modal-title {
        font-size: 32px;
        margin-bottom: 15px;
        color: #333;
    }

    .modal-date {
        color: #764ba2;
        font-weight: 600;
        margin-bottom: 20px;
        padding: 5px 15px;
        background: rgba(118, 75, 162, 0.1);
        display: inline-block;
        border-radius: 20px;
    }

    .modal-desc {
        color: #666;
        line-height: 1.8;
        margin-bottom: 30px;
        font-size: 16px;
    }

    .modal-close {
        background: linear-gradient(135deg, #667eea, #764ba2);
        color: white;
        border: none;
        padding: 12px 35px;
        border-radius: 50px;
        font-size: 16px;
        font-weight: 600;
        cursor: pointer;
        transition: all 0.3s;
    }

    .modal-close:hover {
        transform: scale(1.05);
        box-shadow: 0 10px 25px rgba(102, 126, 234, 0.4);
    }

    /* Sister's Message */
    .sister-section {
        background: rgba(255,255,255,0.1);
        backdrop-filter: blur(10px);
        border-radius: 30px;
        padding: 40px;
        margin: 50px 0;
        text-align: center;
        border: 1px solid rgba(255,255,255,0.2);
    }

    .sister-message {
        max-width: 700px;
        margin: 0 auto;
    }

    .sister-message h3 {
        font-size: 32px;
        margin-bottom: 20px;
        color: #fff;
    }

    .sister-message p {
        font-size: 18px;
        line-height: 1.8;
        color: rgba(255,255,255,0.9);
        margin-bottom: 20px;
    }

    .heart-animation {
        font-size: 40px;
        animation: heartbeat 1.5s ease infinite;
        display: inline-block;
    }

    @keyframes heartbeat {
        0%, 100% { transform: scale(1); }
        50% { transform: scale(1.2); }
    }

    /* Signature */
    .signature {
        text-align: center;
        padding: 30px;
        opacity: 0.7;
        font-size: 14px;
    }

    /* Responsive */
    @media (max-width: 768px) {
        .glow-text {
            font-size: 40px;
        }
        
        .hero-subtitle {
            font-size: 18px;
        }
        
        .timeline-grid {
            grid-template-columns: 1fr;
        }
        
        .stat-number {
            font-size: 32px;
        }
        
        .tech-icon {
            font-size: 24px;
        }
    }
</style>
</head>
<body>

<div class="container">
    <!-- Hero Section -->
    <div class="hero">
        <div class="glow-text">✨ Pranav's Galaxy ✨</div>
        <div class="hero-subtitle">Computer Engineering Student | Tech Explorer | Dream Chaser</div>
        <div class="tech-strip">
            <span class="tech-icon" style="animation-delay: 0s">🐍</span>
            <span class="tech-icon" style="animation-delay: 0.2s">⚛️</span>
            <span class="tech-icon" style="animation-delay: 0.4s">🤖</span>
            <span class="tech-icon" style="animation-delay: 0.6s">📱</span>
            <span class="tech-icon" style="animation-delay: 0.8s">🌐</span>
            <span class="tech-icon" style="animation-delay: 1s">💻</span>
            <span class="tech-icon" style="animation-delay: 1.2s">🔧</span>
            <span class="tech-icon" style="animation-delay: 1.4s">🚀</span>
        </div>
    </div>

    <!-- Stats Section -->
    <div class="stats">
        <div class="stat-card">
            <div class="stat-number">🎯 10th</div>
            <div class="stat-label">Academic Scorer</div>
        </div>
        <div class="stat-card">
            <div class="stat-number">💻 2nd Sem</div>
            <div class="stat-label">Computer Engineering</div>
        </div>
        <div class="stat-card">
            <div class="stat-number">⚡ 4+</div>
            <div class="stat-label">Tech Domains</div>
        </div>
        <div class="stat-card">
            <div class="stat-number">🚀 ∞</div>
            <div class="stat-label">Future Potential</div>
        </div>
    </div>

    <!-- Timeline Title -->
    <div class="timeline-title">📖 My Journey So Far 📖</div>

    <!-- Milestones Grid -->
    <div class="timeline-grid" id="timelineGrid"></div>

    <!-- Sister's Special Message -->
    <div class="sister-section">
        <div class="sister-message">
            <div class="heart-animation">💖</div>
            <h3>A Heartfelt Message From Your Sister</h3>
            <p>My Dearest Pranav,</p>
            <p>Watching you grow into this amazing, talented, and passionate young man fills my heart with so much joy and pride! Your curiosity for technology, your dedication to learning, and your big dreams inspire me every single day.</p>
            <p>Remember, every expert was once a beginner. Keep exploring, keep failing forward, and keep believing in yourself. The tech world is lucky to have you!</p>
            <p>I'll always be your biggest cheerleader, your safe space, and your forever supporter. Keep shining, my little brother! 🌟</p>
            <p style="font-size: 20px; margin-top: 20px;">With all my love,<br>Your Sister 💕</p>
            <div class="heart-animation">💕</div>
        </div>
    </div>

    <div class="signature">
        ✨ Made with 💖 by Your Sister ✨
    </div>
</div>

<!-- Modal -->
<div id="modal" class="modal">
    <div class="modal-content">
        <div id="modalIcon" class="modal-icon"></div>
        <div id="modalTitle" class="modal-title"></div>
        <div id="modalDate" class="modal-date"></div>
        <p id="modalDesc" class="modal-desc"></p>
        <button class="modal-close" onclick="closeModal()">💖 Lovingly Close 💖</button>
    </div>
</div>

<script>
    // Milestones data
    const MILESTONES = __PAYLOAD__;
    
    // Build timeline grid
    const timelineGrid = document.getElementById('timelineGrid');
    
    MILESTONES.forEach((milestone, index) => {
        const card = document.createElement('div');
        card.className = 'milestone-card';
        card.style.animationDelay = (index * 0.05) + 's';
        card.innerHTML = `
            <div class="card-icon">${milestone.icon}</div>
            <div class="card-title">${milestone.title}</div>
            <div class="card-date">${milestone.date}</div>
            <div class="card-desc">${milestone.desc.substring(0, 100)}${milestone.desc.length > 100 ? '...' : ''}</div>
        `;
        card.onclick = () => openModal(milestone);
        timelineGrid.appendChild(card);
    });
    
    // Modal functions
    function openModal(milestone) {
        document.getElementById('modalIcon').innerHTML = milestone.icon;
        document.getElementById('modalTitle').innerHTML = milestone.title;
        document.getElementById('modalDate').innerHTML = milestone.date;
        document.getElementById('modalDesc').innerHTML = milestone.desc;
        document.getElementById('modal').style.display = 'flex';
    }
    
    function closeModal() {
        document.getElementById('modal').style.display = 'none';
    }
    
    // Close modal when clicking outside
    document.getElementById('modal').onclick = function(e) {
        if (e.target === this) closeModal();
    };
    
    // Escape key to close
    document.addEventListener('keydown', function(e) {
        if (e.key === 'Escape') closeModal();
    });
    
    // Add floating shapes dynamically
    const shapes = ['⬜', '🟦', '🟪', '🟩', '🟧', '🔷', '🔶'];
    for (let i = 0; i < 15; i++) {
        const shape = document.createElement('div');
        shape.className = 'floating-shape';
        shape.textContent = shapes[Math.floor(Math.random() * shapes.length)];
        shape.style.left = Math.random() * 100 + '%';
        shape.style.top = Math.random() * 100 + '%';
        shape.style.fontSize = (20 + Math.random() * 40) + 'px';
        shape.style.animationDuration = (15 + Math.random() * 20) + 's';
        shape.style.animationDelay = (Math.random() * 10) + 's';
        document.body.appendChild(shape);
    }
    
    // Confetti on load
    setTimeout(() => {
        for (let i = 0; i < 50; i++) {
            setTimeout(() => createConfetti(), i * 80);
        }
    }, 500);
    
    function createConfetti() {
        const confetti = document.createElement('div');
        confetti.style.position = 'fixed';
        confetti.style.left = Math.random() * 100 + '%';
        confetti.style.top = '-10px';
        confetti.style.width = '10px';
        confetti.style.height = '10px';
        const colors = ['#667eea', '#764ba2', '#ff9a9e', '#fecfef', '#a8edea'];
        confetti.style.backgroundColor = colors[Math.floor(Math.random() * colors.length)];
        confetti.style.borderRadius = '50%';
        confetti.style.pointerEvents = 'none';
        confetti.style.zIndex = '9999';
        confetti.style.animation = `fall ${2 + Math.random() * 2}s linear forwards`;
        document.body.appendChild(confetti);
        setTimeout(() => confetti.remove(), 4000);
    }
    
    // Add fall animation if not exists
    if (!document.querySelector('#fall-style')) {
        const style = document.createElement('style');
        style.id = 'fall-style';
        style.textContent = `
            @keyframes fall {
                0% {
                    transform: translateY(0) rotate(0deg);
                    opacity: 1;
                }
                100% {
                    transform: translateY(100vh) rotate(360deg);
                    opacity: 0;
                }
            }
        `;
        document.head.appendChild(style);
    }
</script>

</body>
</html>
"""

# Replace payload with actual data
milestones_data = []
for m in milestones:
    milestones_data.append({
        "id": m["id"],
        "title": m["title"],
        "date": m["date"],
        "desc": m["desc"],
        "icon": m["icon"],
        "gradient": m["gradient"]
    })

payload_json = json.dumps(milestones_data)
html = html.replace("__PAYLOAD__", payload_json)

st.components.v1.html(html, height=1200, scrolling=True)
