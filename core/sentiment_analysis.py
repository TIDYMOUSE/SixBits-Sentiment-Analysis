#####################NOTES###################
# Following does require a lot of new dependencies
# Please do not install without wifi as torch, spacy and transformers are large modules


from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch.nn.functional as F
from transformers import pipeline
import spacy

### Dependencies
# pip install torch ~600mb
# pip install protobuf ~10mb
# pip install transformers
# pip install spacy
# pip install sentencepiece


### Use only analyze_senti by importing this file
### analyze_senti returns a dictionary of the following syntax:
"""
{
 'experience': {'positive ': 0.9906296, 'neutral': 0.006109544, 'negative': 0.0032608574}, 
 'restaurant': {'positive ': 0.9593607, 'neutral': 0.036665775, 'negative': 0.0039735525}, 
 'food': {'positive ': 0.6335722, 'neutral': 0.35276625, 'negative': 0.013661459},
 'service': {'positive ': 0.0034662876, 'neutral': 0.0019076067, 'negative': 0.9946261}
}
"""


example = "We had a great experience at the restaurant, food was okay, but the service was kinda bad"


def analyze_senti(sentence):
    absa_tokenizer = AutoTokenizer.from_pretrained("yangheng/deberta-v3-base-absa-v1.1")
    absa_model = AutoModelForSequenceClassification.from_pretrained("yangheng/deberta-v3-base-absa-v1.1")
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(sentence)
    aspects = []
    out = {}
    for token in doc:
        if token.pos_ == "NOUN":
            aspects.append(token.text)
    for aspect in aspects:
        inputs = absa_tokenizer(f"[CLS] {sentence} [SEP] {aspect} [SEP]", return_tensors="pt")
        outputs = absa_model(**inputs)
        probs = F.softmax(outputs.logits, dim=1)
        probs = probs.detach().numpy()[0]
        for prob, label in zip(probs, ["negative", "neutral", "positive"]):
            senti = {"positive ": probs[2], "neutral":probs[1], "negative" : probs[0] }
            out[aspect] = dict(senti)
    return out
    
#print(analyze_senti(sentence=example))
