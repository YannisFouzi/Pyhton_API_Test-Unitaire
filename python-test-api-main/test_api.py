import requests


#---TEST N° 1---
Post = requests.post(
    "http://127.0.0.1:5000/movies",
    json={"genre": "Policier", "title": "Banlieue 13", "year": 2004},
).status_code
if Post == 201:
    print(Post, "Le test est passé")
else:
    print(Post, "Le test n'est pas passé")


#---TEST N° 2---
Get = requests.get("http://127.0.0.1:5000/movies/1").status_code
if Get == 200:
    print(Post, "Le test est passé")
else:
    print(Post, "Le test n'est pas passé")


#---TEST N° 3---
Put = requests.put(
    "http://127.0.0.1:5000/movies/3",
    json={"genre": "SF", "title": "Interstellar", "year": 2020},
).status_code
if Put == 200:
    print(Post, "Le test est passé")
else:
    print(Post, "Le test n'est pas passé")


#---TEST N° 4---
Delete = requests.delete("http://127.0.0.1:5000/movies/1").status_code
if Delete == 200:
    print(Post, "Le test est passé")
else:
    print(Post, "Le test n'est pas passé")
