def original_url(id=None):
    if id is None:
        return "https://xkcd.com/info.0.json"
    else:
        return "https://xkcd.com/" + id + "/info.0.json"

def explain(id=None):
    if id is None:
        return "https://www.explainxkcd.com"
    else:
        return "https://www.explainxkcd.com/" + id

def tw(id=None):
    if id is None:
        return "https://xkcd.tw"
    else:
        return "https://xkcd.tw/" + id