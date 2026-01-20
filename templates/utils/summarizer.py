from transformers import BartForConditionalGeneration, BartTokenizer

tokenizer = BartTokenizer.from_pretrained("facebook/bart-large-cnn")
model = BartForConditionalGeneration.from_pretrained("facebook/bart-large-cnn")

def generate_summary(scores, text):
    top3 = sorted(scores.items(), key=lambda x: x[1], reverse=True)[:3]
    prefix = "Emotions: " + ", ".join([f"{e}({round(s*100)}%)" for e, s in top3])
    full_input = prefix + " Text: " + text

    inputs = tokenizer([full_input], truncation=True, return_tensors="pt")
    summary_ids = model.generate(
        inputs["input_ids"],
        max_length=100,
        num_beams=4,
        early_stopping=True
    )

    return tokenizer.decode(summary_ids[0], skip_special_tokens=True)
