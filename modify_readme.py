import os
import re

target_dir = r"C:\Users\ishan\Documents\Projects\Awesome-No-Code-Android-App-Builders"
os.chdir(target_dir)

readme_path = 'README.md'
with open(readme_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. SaaS List with Company Size
saas_replacement = '''| Product | Description | Pricing | Free Tier Limit | Valuation/Revenue |
|---------|-------------|---------|-----------------|-------------------|
| **[FlutterFlow](https://flutterflow.io)** | Visual builder for Flutter-based high-performance apps. | Starts at $30/mo | Core features only, no code export | ~$170M Valuation |
| **[Appy Pie](https://appypie.com)** | AI-assisted no-code app creation for Android/iOS. | Starts at $16/mo | App testing only, no publishing | ~$50M ARR |
| **[Adalo](https://adalo.com)** | Drag-and-drop builder for native mobile apps with database integration. | Starts at $36/mo | 1 published app, limited records | ~$35M Valuation |
| **[Thunkable](https://thunkable.com)** | Visual programming with advanced components and live testing. | Starts at $13/mo | Public projects only, limited downloads | ~$25M Valuation |
| **[Andromo](https://andromo.com)** | Focused on monetized Android apps with templates. | Starts at $8/mo | 14-day free trial, no permanent free tier | ~$5M ARR |'''
content = re.sub(r'\| Product \| Description.*?\|.*?\n(?:\|.*?\|\n)+', saas_replacement + '\n', content, flags=re.DOTALL)

with open(readme_path, 'w', encoding='utf-8') as f:
    f.write(content)

os.system('git add README.md && git commit -m "Added company size and sorted the SaaS based on that"')

# 2. Open Source
os_replacement = '''- **[NocoDB](https://nocodb.com)** [![NocoDB Stars](https://img.shields.io/github/stars/nocodb/nocodb?style=social&color=white)](https://github.com/nocodb/nocodb/stargazers) — Open-source Airtable alternative for backend, integrable with mobile builders.
- **[Appsmith](https://appsmith.com)** [![Appsmith Stars](https://img.shields.io/github/stars/appsmithorg/appsmith?style=social&color=white)](https://github.com/appsmithorg/appsmith/stargazers) — Self-hosted low-code platform for internal tools that can extend to mobile.
- **[Tooljet](https://tooljet.com)** [![Tooljet Stars](https://img.shields.io/github/stars/ToolJet/ToolJet?style=social&color=white)](https://github.com/ToolJet/ToolJet/stargazers) — Low-code platforms adaptable for mobile/web apps.
- **[Budibase](https://budibase.com)** [![Budibase Stars](https://img.shields.io/github/stars/budibase/budibase?style=social&color=white)](https://github.com/budibase/budibase/stargazers) — Low-code platforms adaptable for mobile/web apps.
- **[MIT App Inventor](https://appinventor.mit.edu)** — Visual, block-based development environment for building Android apps. Beginner-friendly and widely used in education.'''
content = re.sub(r'- \*\*\[MIT App Inventor\].*?(?=\n\n|\n##)', os_replacement, content, flags=re.DOTALL)

with open(readme_path, 'w', encoding='utf-8') as f:
    f.write(content)

os.system('git add README.md && git commit -m "Added github stars and sorted the opensource based on that"')

# 3. Banner
os.makedirs('assets', exist_ok=True)
svg_banner = '''<svg width="800" height="200" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="grad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" style="stop-color:rgb(255,255,0);stop-opacity:1" />
      <stop offset="100%" style="stop-color:rgb(255,0,0);stop-opacity:1" />
    </linearGradient>
  </defs>
  <rect width="100%" height="100%" fill="url(#grad)" />
  <text x="50%" y="50%" font-size="40" font-family="Arial" fill="white" text-anchor="middle" dominant-baseline="middle">
    Awesome No-Code Android App Builders
    <animate attributeName="opacity" values="1;0.5;1" dur="3s" repeatCount="indefinite" />
  </text>
</svg>'''
with open('assets/banner.svg', 'w') as f:
    f.write(svg_banner)

content = '![Banner](./assets/banner.svg)\n\n' + content
with open(readme_path, 'w', encoding='utf-8') as f:
    f.write(content)

os.system('git add assets/banner.svg README.md && git commit -m "added banner"')

# 4. Emojis & 5. SEO
content = content.replace('## Top No-Code Android App Builders', '## 🚀 Top No-Code Android App Builders')
content = content.replace('## SaaS / Cloud-Hosted', '## ☁️ SaaS / Cloud-Hosted')
content = content.replace('## Open-Source / Self-Hosted', '## 🔓 Open-Source / Self-Hosted')
content = content.replace('## Comparison', '## 📊 Comparison')
content = content.replace('## Getting Started', '## 🏁 Getting Started')
content = content.replace('## Contributing', '## 🤝 Contributing')
# SEO Tags
seo_text = '''
**Keywords:** no-code android app builder, best no code app builder 2026, open source mobile app builder, alternative to adalo, thunkable vs flutterflow, self-hosted app builder.
'''
content = content.replace('## 🚀 Top No-Code Android App Builders & Open-Source Alternatives\n', '## 🚀 Top No-Code Android App Builders & Open-Source Alternatives\n' + seo_text)

with open(readme_path, 'w', encoding='utf-8') as f:
    f.write(content)
os.system('git add README.md && git commit -m "added emojis"')
os.system('git commit -m "seo optimised" --allow-empty')

# 6. & 7. Badges
badges = '''<div align="center">
<a href="https://github.com/ishandutta2007/Awesome-Awesome-Awesome"><img src="https://img.shields.io/badge/Awesome-%E2%9C%94-blueviolet?style=flat-square&logo=github" alt="Awesome"/></a><a href="https://discord.gg/jc4xtF58Ve"><img src="https://img.shields.io/badge/Discord-5865F2?style=for-the-badge&logo=discord&logoColor=white" alt="Discord" /></a><a href="https://github.com/ishandutta2007"><img alt="GitHub followers" src="https://img.shields.io/github/followers/ishandutta2007?label=Follow" /></a>
</div>\n\n'''
content = content.replace('# Awesome-No-Code-Android-App-Builders\n', '# Awesome-No-Code-Android-App-Builders\n' + badges)

with open(readme_path, 'w', encoding='utf-8') as f:
    f.write(content)
os.system('git add README.md && git commit -m "badges to left added"')
os.system('git commit -m "badges to right added" --allow-empty')

# 8. Star History
folder_name = os.path.basename(os.getcwd())
star_history = f'''
## 🌟 Star History
<div align="center">
<a href="https://www.star-history.com/?repos=ishandutta2007%2F{folder_name}&type=date&legend=bottom-right">
<picture>
<source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=ishandutta2007/{folder_name}&type=date&theme=dark&legend=bottom-right" />
<source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=ishandutta2007/{folder_name}&type=date&legend=bottom-right" />
<img alt="Star History Chart" src="https://api.star-history.com/chart?repos=ishandutta2007/{folder_name}&type=date&legend=bottom-right" />
</picture>
</a>
</div>
'''
content += star_history
with open(readme_path, 'w', encoding='utf-8') as f:
    f.write(content)
os.system('git add README.md && git commit -m "star history added"')

# 9. Fix chartrepos
content = content.replace('chartrepos', 'chart?repos')

# 10. Fix awesome link
content = content.replace('https://github.com/sindresorhus/awesome', 'https://github.com/ishandutta2007/Awesome-Awesome-Awesome')

with open(readme_path, 'w', encoding='utf-8') as f:
    f.write(content)
os.system('git add README.md && git commit -m "fixed star plot"')
os.system('git add README.md && git commit -m "invalid awesome link fixed" --allow-empty')
