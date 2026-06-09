import json

words = {
    frozenset(["tap", "telephone"]): ("tæp", "telifəun"),
    "travel": "trævl",
    ("hello", "world"): ("həˈləʊ", "wɜːld"),
    "moonlight": "muːn.laɪt",
    "sunshine": "ˈsʌn.ʃaɪn",
    ("why", "is", "so", "difficult"): ("waɪ", "ɪz", "səʊ", "ˈdɪfɪkəlt"),
    "adventure": "ədˈventʃər",
    "beautiful": "ˈbjuːtɪfl",
    frozenset(["spoon", "block"]): ("spu:n", "blɔk"),
    "bicycle": "baisikl",
    ("pilot", "fly"): ("pailət", "flai")
}

data_json = json.dumps(words, skipkeys=True)

print(data_json)