import markovify

with open("model.json", encoding='utf-8') as model_json:
    model = markovify.Text.from_json(model_json.read())

    while True:
        print(model.make_sentence())
        input()