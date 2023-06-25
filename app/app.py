from modelVoiture import ModelVoiture
from fastapi import FastAPI, HTTPException
from db import database

app = fastapi()

@app.get("/voiture")
def get_voitures():
    db = database()
    voitures = db.warehouse.find()
    res = []

    for voiture in voitures:
        data = {
            "immatriculation": voiture["immatriculation"],
            "marque": voiture["marque"],
            "modele": voiture["modele"],
            "prix": voiture["prix"],
            "color": voiture["color"],
        }
        res.append(data)
    return res

@app.post("/voiture")
def create_voiture(voiture: Voiture):
    db = database()
    

@app.get("/voiture/{immat}")

@app.put("/voiture/{immat}")

@app.delete("/voiture/{immat}")