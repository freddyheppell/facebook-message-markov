import markovify

with open("model.json") as model_json:
    model = markovify.Text.from_json(model_json.read())

    for i in range(5):
        print(model.make_sentence())