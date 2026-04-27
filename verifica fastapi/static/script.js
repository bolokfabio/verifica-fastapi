async function calcolaBMI() {

    const peso = document.getElementById("peso").value;  
    const altezza = document.getElementById("altezza").value;  
     if (!peso || !altezza) {  
        
        document.getElementById("risultato").innerText = "Inserisci i valori";
        return;  
        
    }

    const res = await fetch("/bmi", {  
       method: "POST",  
       headers: {
            "Content-Type": "application/x-www-form-urlencoded"
        },  

        body: `peso=${peso}&altezza=${altezza}`  
       
    });

    const dati = await res.json();  
    

    if (dati.errore) {  
        
        document.getElementById("risultato").innerText = dati.errore;
    } else {
        document.getElementById("risultato").innerText =
            "il tuo IMC è: " + dati.bmi + " - la tua categoria é: " + dati.categoria;
        
    }
}
document.getElementById("btn1").addEventListener("click", calcolaBMI);  