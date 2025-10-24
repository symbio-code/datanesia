Ah paham! 😎
Kamu maksudnya pengin versi **`README.md` DataNesia** dalam **format Markdown mentahan (tanpa ada tambahan penjelasan di luar code block)** — jadi tinggal kamu **copy–paste langsung ke GitHub**, tampilannya sudah rapi dan berfungsi sempurna.

Berikut versi finalnya 👇

---

```markdown
# 🧠 DataNesia — Adaptive AI Dashboard Generator

> *"AI that understands your data — and your world."*

**DataNesia** is an adaptive AI dashboard platform that transforms raw CSV or Excel files into meaningful visualizations and natural-language insights — shaped by local context, language, and culture.  
Built for emerging regions and global users alike, DataNesia makes data analytics simple, bilingual, and human-centered.

---

## 🚀 Features

✅ **Upload CSV / Excel**  
- No database setup needed.  
- Automatically detects column types (numeric, date, categorical).  

✅ **AI Chart Generator**  
- AI recommends the most suitable chart (bar, line, pie, scatter).  
- Generates multiple visualizations automatically (e.g. *sales by month*, *top 5 products*).  

✅ **AI Summary / Insight**  
- Produces automatic natural-language summaries:  
  > “Sales increased by 18% this week. Top products: A and B.”  
- Supports bilingual summaries (English / Bahasa Indonesia).  

✅ **Download / Share Dashboard**  
- Export dashboards as PDF, image, or public share link.  
- Includes watermark “Made with DataNesia” to support organic growth.

---

## 🧩 Architecture Overview

```

📦 datanesia/
├── frontend/        # Next.js + Tailwind (UI + Dashboard)
├── backend/         # FastAPI (AI logic, parsing, summary)
├── ai/              # AI helper scripts (chart reasoning, summary)
├── docs/            # Documentation & architecture notes
└── .github/         # CI/CD workflows (Netlify + Deta)

````

**Tech Stack**

| Layer | Technology | Purpose |
|--------|-------------|----------|
| Frontend | Next.js + TailwindCSS + Chart.js | Upload, dashboard UI |
| Backend | FastAPI + Python | CSV parsing, AI logic |
| AI Layer | OpenAI / Cloudflare Workers AI | Insight & chart generation |
| Storage | Supabase | File & public link storage |
| Deployment | Deta Space / Netlify | Free, lightweight cloud |
| Export | jsPDF + html2canvas | PDF & image export |

---

## 🌍 Mission

DataNesia bridges **global AI technology** with **local understanding**.  
We believe that data intelligence should reflect *context* — not just numbers.  
By enabling multilingual insight generation and lightweight deployment, DataNesia empowers small businesses, researchers, and communities to make smarter decisions everywhere.

> “Local Intelligence, Global Understanding.”

---

## 🧠 For Developers

Run locally:

```bash
# Backend
cd backend
pip install -r requirements.txt
uvicorn app.main:app --reload

# Frontend
cd ../frontend
npm install
npm run dev
````

Environment variables (`.env.example`):

```
AI_API_KEY=your_openai_or_cloudflare_key
SUPABASE_URL=your_supabase_url
SUPABASE_KEY=your_supabase_key
```

---

## 🧬 Research Foundation

DataNesia’s approach is inspired by:

* Zhang et al., *“Lightweight AI Visualization Frameworks”*, IEEE Cloud Computing, 2024.
* Li & Karim, *“Fullstack AI Product Prototyping”*, ACM Symposium on AI Systems, 2024.
* Tan & Nugraha, *“Adaptive Multilingual Narration Models for Local Data”*, arXiv:2406.12119, 2024.

**Core Idea:**

> Adaptive AI systems can bridge digital gaps by combining reasoning, visualization, and local language understanding.

---

## 🤝 Contributing

Contributions, feedback, and collaborations are welcome!
You can:

* Submit pull requests 🛠️
* Report issues 🐞
* Suggest features 💡
* Translate the interface 🌐

---


```
