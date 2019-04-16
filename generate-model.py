import markovify

with open("corpus.txt", encoding='utf-8') as f:
    text = f.read()

    text_model = markovify.NewlineText(text)

    model_json = text_model.to_json()

    with open("model.json", "w+", encoding='utf-8') as model:
        model.write(model_json)