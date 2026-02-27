# AI Meeting Minutes Generator

An AI-powered web application that automatically converts raw meeting transcripts into structured meeting minutes using Natural Language Processing (NLP).

Built with **Streamlit** and **HuggingFace Transformers**, the system generates concise summaries, extracts action items, identifies follow-ups, and allows export via PDF or email.

---

## Features

* 📄 Automatic meeting summary generation
* ✅ Action item extraction
* 📆 Follow-up detection
* 📄 Export summary as PDF
* 📧 Email meeting minutes to recipients
* 🧩 Chunk-based processing for long transcripts

---

## Tech Stack

* **Frontend:** Streamlit
* **NLP Model:** facebook/bart-large-cnn
* **Framework:** HuggingFace Transformers
* **Backend:** Python
* **PDF Generation:** ReportLab
* **Email Service:** SMTP (Gmail)
* **Environment Management:** python-dotenv

---

## System Architecture

1. User inputs raw transcript
2. Transcript preprocessing (speaker normalization)
3. Text chunking (900-character segments)
4. Summarization using BART model
5. Rule-based extraction of action items & follow-ups
6. Export as PDF or send via email

---

## Installation & Setup

### 1️⃣ Clone the repository

```bash
git clone https://github.com/your-username/ai-meeting-minutes-generator.git
cd ai-meeting-minutes-generator
```

### 2️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Create `.env` file

```env
EMAIL_ADDRESS=your_email@gmail.com
EMAIL_PASSWORD=your_app_password
```

> Use Gmail App Password (not your normal password).

### 4️⃣ Run the application

```bash
streamlit run app.py
```

---

## Model Details

* Model: **facebook/bart-large-cnn**
* Task: Abstractive text summarization
* Approach: Chunk-based summarization for handling long transcripts
* Additional NLP: Rule-based action and follow-up detection

---

## Use Case

This system helps organizations, students, and professionals:

* Reduce manual documentation time
* Improve meeting clarity
* Track responsibilities and deadlines
* Maintain structured records

---

## Security Note

* `.env` file is excluded via `.gitignore`
* Email credentials are never stored in the repository

---

## Author

Developed as a Generative AI productivity project focused on real-world workplace automation.
