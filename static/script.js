"use strict";

function verificationMdp(mdp){
    return mdp === "windaube";
}

// Gestion des LEDs 

const ledColorClasses = ["rouge", "vert", "bleu", "jaune", "blanc", "rose", "violet", "orange"];
let currentLedIndex = null;

function setLedColor(ledIndex, colorClass){
    const led = document.getElementById(`led${ledIndex}`);
    if (!led) return;

    led.classList.remove(...ledColorClasses);
    led.classList.add(colorClass);

    const hiddenInput = document.querySelector(`input[name="led${ledIndex}"]`);
    if (hiddenInput) {
        hiddenInput.value = colorClass;
    }
}

function openColorPicker(ledIndex) {
    currentLedIndex = ledIndex;
    const picker = document.getElementById("colorPicker");
    if (!picker) return;

    picker.classList.add("active");
}

function closeColorPicker() {
    currentLedIndex = null;
    const picker = document.getElementById("colorPicker");
    if (!picker) return;

    picker.classList.remove("active");
}

function initMasterLedButtons() {
    const buttons = document.querySelectorAll(".master-button[data-led]");
    if (!buttons.length) return;

    buttons.forEach((button) => {
        const ledIndex = Number(button.dataset.led);
        if (!ledIndex) return;
        button.addEventListener("click", () => openColorPicker(ledIndex));
    });
}

function initColorPicker() {
    const picker = document.getElementById("colorPicker");
    if (!picker) return;

    picker.querySelectorAll(".color-option").forEach((button) => {
        button.addEventListener("click", () => {
            const color = button.dataset.color;
            if (currentLedIndex !== null) {
                setLedColor(currentLedIndex, color);
            }
            closeColorPicker();
        });
    });

    const cancel = picker.querySelector(".color-cancel");
    if (cancel) {
        cancel.addEventListener("click", closeColorPicker);
    }

    picker.addEventListener("click", (event) => {
        if (event.target === picker) {
            closeColorPicker();
        }
    });
}

function initLedFormSubmit() {
    const form = document.getElementById("ledForm");
    if (!form) return;

    form.addEventListener("submit", async (event) => {
        event.preventDefault();

        const formData = new FormData(form);
        try {
            const response = await fetch(form.action, {
                method: form.method,
                body: formData,
            });

            if (!response.ok) {
                console.error("Erreur de soumission du formulaire", response.status);
                return;
            }

            // Optionnel : utilises les données renvoyées par le serveur
            const text = await response.text();
            console.log("Réponse du serveur :", text);

            // Optionnel : afficher un retour visuel à l'utilisateur
            // alert("Configuration enregistrée !");
        } catch (error) {
            console.error("Erreur réseau lors de la soumission du formulaire", error);
        }
    });
}

//Menu de connexion

function initLoginPage() {
    const btnConfirm = document.getElementById("btnConfirm");
    if (!btnConfirm) return;

    btnConfirm.addEventListener("click", function(event){
        let motsDePasse = document.getElementById("mdp").value;
        let message = document.getElementById("message");
        if(verificationMdp(motsDePasse)){

            // message d'accès
            message.innerText = "Accès autorisé :)";
            message.classList.add("access");
            document.querySelectorAll("*[name=mdp]").forEach(function(e){
                e.classList.add("cache");
            })
            document.getElementById("btnStart").classList.remove("cache");

        }else{
            document.getElementById("message").innerText = "Accès non autorisé :|";
            document.getElementById("message").classList.add("no-access");
        }
    });
}

window.addEventListener("DOMContentLoaded", () => {
    initLoginPage();
    initMasterLedButtons();
    initColorPicker();
    initLedFormSubmit();
});
