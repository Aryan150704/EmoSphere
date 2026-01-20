from transformers import pipeline

# Lightweight summarizer
summarizer = pipeline(
    "summarization",
    model="sshleifer/distilbart-cnn-12-6"
)

def get_summary(text):
    summary = summarizer(text, max_length=120, min_length=30, do_sample=False)
    return summary[0]["summary_text"]
