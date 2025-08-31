import os
import requests
from datetime import datetime

def generate_readme_content():
    # Example: Get current time
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S UTC")

    # Example: Fetch some data (e.g., GitHub user data)
    github_username = "sathishzuss" # Replace with your GitHub username
    user_data = {}
    try:
        response = requests.get(f"https://api.github.com/users/{github_username}")
        response.raise_for_status()
        user_data = response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching GitHub user data: {e}")

    # Construct the README content
    content = f"""<div align="center">
  <img src="https://raw.githubusercontent.com/sathishzuss/sathishzuss/output/dist/ocean.gif" alt="snake" />
</div>

# Hi, I'm {user_data.get('name', github_username)}! 👋

### A passionate software engineer from India, building innovative solutions.

## 🚀 About Me

- 🔭 I’m currently working on exciting projects and exploring new horizons in software development.
- 🌱 I’m continuously learning and expanding my knowledge in cutting-edge technologies.
- 👯 I’m open to collaborating on impactful open-source projects.
- 💬 Ask me about anything related to web development, cloud, or automation!
- 📫 How to reach me: {user_data.get('email', 'Not available')}
- ⚡ Fun fact: I love coding, exploring new tech, and solving complex problems!

## 🛠️ Tech Stack

<p align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python" />
  <img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black" alt="JavaScript" />
  <img src="https://img.shields.io/badge/TypeScript-3178C6?style=for-the-badge&logo=typescript&logoColor=white" alt="TypeScript" />
  <img src="https://img.shields.io/badge/React-61DAFB?style=for-the-badge&logo=react&logoColor=black" alt="React" />
  <img src="https://img.shields.io/badge/Node.js-339933?style=for-the-badge&logo=node.js&logoColor=white" alt="Node.js" />
  <img src="https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white" alt="Docker" />
  <img src="https://img.shields.io/badge/AWS-232F3E?style=for-the-badge&logo=amazon-aws&logoColor=white" alt="AWS" />
  <img src="https://img.shields.io/badge/Azure-0078D4?style=for-the-badge&logo=microsoft-azure&logoColor=white" alt="Azure" />
  <img src="https://img.shields.io/badge/Google_Cloud-4285F4?style=for-the-badge&logo=google-cloud&logoColor=white" alt="Google Cloud" />
  <img src="https://img.shields.io/badge/Kubernetes-326CE5?style=for-the-badge&logo=kubernetes&logoColor=white" alt="Kubernetes" />
  <img src="https://img.shields.io/badge/Terraform-7B42BC?style=for-the-badge&logo=terraform&logoColor=white" alt="Terraform" />
  <img src="https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white" alt="Git" />
  <img src="https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white" alt="GitHub" />
</p>

## 📊 GitHub Analytics

<p align="center">
  <img src="https://github-readme-stats.vercel.app/api?username={github_username}&show_icons=true&theme=radical&hide_border=true&count_private=true" alt="GitHub Stats" />
  <img src="https://github-readme-stats.vercel.app/api/top-langs/?username={github_username}&layout=compact&theme=radical&hide_border=true" alt="Top Langs" />
  <img src="https://github-readme-streak-stats.herokuapp.com/?user={github_username}&theme=radical&hide_border=true" alt="GitHub Streak" />
</p>

## 🏆 Achievements

- 🏅 Actively contributing to open-source projects.
- ✨ Always striving for clean and efficient code.
- 🌟 Constantly learning and adapting to new technologies.

## ⚙️ Automations

This README is automatically updated using GitHub Actions!
- Real-time updates for GitHub stats and latest activity.
- Contributions visualized as a snake game.

## Latest Update

This README was last updated on: **{current_time}**

"""
    return content

if __name__ == "__main__":
    readme_content = generate_readme_content()
    with open("ReadME.md", "w") as f:
        f.write(readme_content)
    print("ReadME.md updated successfully!")
