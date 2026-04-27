from fastapi import FastAPI, Form  # importo FastAPI e Form per prendere dati dal frontend
from fastapi.responses import FileResponse  # serve per inviare il file HTML
from fastapi.staticfiles import StaticFiles  # serve per usare cartella static
import pandas as pd 

app = FastAPI()  
df = pd.read_excel("/workspaces/verifica-fastapi/imc.xlsx")
app.mount("/static", StaticFiles(directory="static"), name="static")  


@app.get("/")  
def home():
    return FileResponse("static/index.html")  
   



@app.post("/bmi") 
def calcola_bmi(peso: float = Form(...), altezza: float = Form(...)):
   

    if peso <= 0 or altezza <= 0:  
         return {"errore": "Valori non validi"}  
        

    bmi = peso / (altezza ** 2)  
    

    if bmi < 18.5:
        valutazione = -1  
    elif bmi > 25:  
        valutazione = 1  
    else:  
        valutazione = 0 

    if valutazione == -1:
        categoria = "sottopeso"
    elif valutazione == 1 :
        categoria = "sovrapeso"
    else:
        categoria = "normopeso"
    
    return {
        "bmi": bmi,  
        "categoria": categoria  

    
    
    } 
    
@app.post("/bmi_pandas") 
def calcola_bmi(peso: float = Form(...), altezza: float = Form(...)):
   

    if peso <= 0 or altezza <= 0:  
         return {"errore": "Valori non validi"}  
        

    bmi = peso / (altezza ** 2)  
    

    if bmi < 18.5:
        valutazione = -1  
    elif bmi > 25:  
        valutazione = 1  
    else:  
        valutazione = 0 

    if valutazione == -1:
        categoria = "sottopeso"
    elif valutazione == 1 :
        categoria = "sovrapeso"
    else:
        categoria = "normopeso"
    
    return {
        "bmi": bmi,  
        "categoria": categoria  

    
    
    } 
    