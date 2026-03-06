"use strict";

function verificationMdp(mdp){
    return mdp === "windaube";
}

document.getElementById("btnConfirm").addEventListener("click", function(event){
    let motsDePasse = document.getElementById("mdp").value;
    let message = document.getElementById("message");
    if(verificationMdp(motsDePasse)){

        // message d'accès
        message.innerText = "accès autorisée :)";
        message.classList.add("access");
        document.querySelectorAll("*[name=mdp]").forEach(function(e){
            e.classList.add("cacher");
        })
        document.getElementById("btnStart").classList.remove("cacher");

    }else{
        document.getElementById("message").innerText = "accès non autorisée :|";
        document.getElementById("message").classList.add("no-access");
    }
})