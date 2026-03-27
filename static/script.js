"use strict";

function verificationMdp(mdp) {
    return mdp === "windaube";
}

// Gestion des LEDs 

const ledColorClasses = ["rouge", "vert", "bleu", "jaune", "blanc", "rose", "violet", "orange"];
let currentLedIndex = null;

function setLedColor(ledIndex, colorClass) {
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

//Menu de connexion

function initLoginPage() {
    const btnConfirm = document.getElementById("btnConfirm");
    if (!btnConfirm) return;

    btnConfirm.addEventListener("click", function (event) {
        let motsDePasse = document.getElementById("mdp").value;
        let message = document.getElementById("message");
        if (verificationMdp(motsDePasse)) {
            message.innerText = "Accès autorisé :)";
            message.classList.add("access");
            setTimeout(() => message.classList.add("animate-in"), 10);

            document.querySelectorAll("*[name=mdp]").forEach(function (e) {
                e.classList.add("cache");
            });

            const btnMaster = document.getElementById("master");
            const btnPlayer = document.getElementById("player");

            btnMaster.classList.remove("hidden");
            btnPlayer.classList.remove("hidden");

            setTimeout(() => btnMaster.classList.add("animate-in"), 50);
            setTimeout(() => btnPlayer.classList.add("animate-in"), 160);

        } else {
            document.getElementById("message").innerText = "Accès non autorisé :|";
            document.getElementById("message").classList.add("no-access");
        }
    });
}

window.addEventListener("DOMContentLoaded", () => {
    initLoginPage();
    initMasterLedButtons();
    initColorPicker();
});