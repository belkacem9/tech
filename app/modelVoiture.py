from pydantic import BaseModel, validator

class ModelVoiture(BaseModel):
    immatriculation: str
    marque: str
    modele:str
    prix:int
    couleur:str