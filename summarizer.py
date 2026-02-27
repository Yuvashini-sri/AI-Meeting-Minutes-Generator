# summarizer.py
from transformers import pipeline

# Load Hugging Face summarizer
summarizer_pipeline = pipeline("summarization", model="facebook/bart-large-cnn", framework="pt")

def preprocess_transcript(text):
    """
    Cleans up transcript for summarization.
    Converts 'Speaker: Message' → 'Speaker said message.'
    """
    lines = text.strip().split("\n")
    sentences = []
    for line in lines:
        if ":" in line:
            speaker, message = line.split(":", 1)
            sentences.append(f"{speaker.strip()} said {message.strip()}.")
        else:
            sentences.append(line.strip())
    return " ".join(sentences)

def extract_action_items(text):
    """
    Extracts sentences that look like tasks or commitments.
    """
    action_keywords = ["will", "shall", "need to", "update", "finalize", "prepare", "launch", "send"]
    items = []
    for line in text.split("."):
        if any(keyword in line.lower() for keyword in action_keywords):
            items.append(line.strip())
    return items

def extract_followups(text):
    """
    Extracts sentences that mention future meetings or follow-ups.
    """
    follow_keywords = ["next meeting", "meeting on", "follow up", "check in", "review on", "scheduled for"]
    items = []
    for line in text.split("."):
        if any(keyword in line.lower() for keyword in follow_keywords):
            items.append(line.strip())
    return items

def summarize_text(text):
    """
    Summarizes the transcript and returns formatted output
    with Meeting Summary, Action Items, and Follow-ups.
    """
    cleaned_text = preprocess_transcript(text)

    # Split long text into smaller chunks
    max_chunk = 900
    chunks = [cleaned_text[i:i + max_chunk] for i in range(0, len(cleaned_text), max_chunk)]

    summary = ""
    for chunk in chunks:
        out = summarizer_pipeline(chunk, max_length=200, min_length=60, do_sample=False)
        summary += out[0]['summary_text'].strip() + "\n\n"

    # Extract tasks & follow-ups from the *original transcript*, not summary
    action_items = extract_action_items(cleaned_text)
    followups = extract_followups(cleaned_text)

    # Format nicely
    formatted = "📝 Meeting Summary:\n" + summary.strip() + "\n\n"

    formatted += "✅ Action Items:\n"
    if action_items:
        for item in action_items:
            formatted += f"- {item}\n"
    else:
        formatted += "- No explicit action items found.\n"

    formatted += "\n📆 Follow-ups:\n"
    if followups:
        for f in followups:
            formatted += f"- {f}\n"
    else:
        formatted += "- No follow-ups mentioned.\n"

    return formatted
