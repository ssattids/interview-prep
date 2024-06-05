"""
A working hugging face classicfication model to train locally
"""
# log into hugging face
from huggingface_hub import login
login("your-hugging-face-token")
# %%
from datasets import Dataset
import pandas as pd
# %%
df_data = [
    {"text": "I love my dog", "label": "dog_love"},
    {"text": "I love my dog", "label": "dog_love"},
    {"text": "I love my dog", "label": "dog_love"},
    {"text": "I love my cat", "label": "cat_love"},
    {"text": "I love my cat", "label": "cat_love"},
    {"text": "I love my cat", "label": "cat_love"},
    {"text": "I love my pet", "label": "pet_love"},
    {"text": "I love my pet", "label": "pet_love"},
    {"text": "I don't care!", "label": "no_feeling"},
    {"text": "Meh - whateva", "label": "no_feeling"}
]
df = pd.DataFrame(df_data)
# %%
id2label = {i:genre for i, genre in enumerate(set(df['label']))}
id2label
# %%
label2id = {label:id for id, label in id2label.items()}
label2id
# %%
df.to_dict(orient='records')
# %%
data = []
for i in range(len(df)):
    title = f"text: {df.iloc[i]['text']}."

    data.append({
        'label': label2id[df.iloc[i]['label']],
        'text': title,
    })
data
# %%
dataset = Dataset.from_list(data)
# split the dataset
dataset = dataset.train_test_split(test_size=0.2)
dataset
# %%
# tokenize the text
from transformers import AutoTokenizer
tokenizer = AutoTokenizer.from_pretrained("distilbert/distilbert-base-uncased")
def preprocess_function(examples):
    return tokenizer(examples["text"], truncation=True)
modelling_data_tokenized = dataset.map(preprocess_function, batched=True)
# %%
# DataCollatorWithPadding the automates this padding process
from transformers import DataCollatorWithPadding
data_collator = DataCollatorWithPadding(tokenizer=tokenizer)
# %%
# load the model
from transformers import AutoModelForSequenceClassification, TrainingArguments, Trainer
model = AutoModelForSequenceClassification.from_pretrained(
    "distilbert/distilbert-base-uncased", num_labels=len(id2label), id2label=id2label, label2id=label2id
)
# %%
training_args = TrainingArguments(
    output_dir="my_awesome_model",
    use_mps_device=True,
    learning_rate=2e-5,
    per_device_train_batch_size=16,
    per_device_eval_batch_size=16,
    num_train_epochs=2,
    weight_decay=0.01,
    eval_strategy="epoch",
    save_strategy="epoch",
    load_best_model_at_end=True,
    push_to_hub=False,
)
# %%
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=modelling_data_tokenized['train'],
    eval_dataset=modelling_data_tokenized['test'],
    tokenizer=tokenizer,
    data_collator=data_collator,
    # compute_metrics=compute_metrics,
)
trainer.train()
# %%
# inference text
inference_text = ["I love my dog."]
inputs = tokenizer(inference_text, padding=True, return_tensors="pt")
# %%
# load the model
from transformers import AutoModelForSequenceClassification
import torch
model = AutoModelForSequenceClassification.from_pretrained("./my_awesome_model/checkpoint-1")
with torch.no_grad():
    logits = model(**inputs).logits
# %%
# get the predicted class
predicted_class_id = logits.argmax().item()
model.config.id2label[predicted_class_id]
# %%