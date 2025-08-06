document.addEventListener('DOMContentLoaded', () => {
    function sendRequest(url) {
        fetch(url).catch(err => console.error('Request failed:', err));
    }

    // Swing Buttons
    const swingleftBtn = document.getElementById('swingleft-button');
    if (swingleftBtn) {
        swingleftBtn.addEventListener('mousedown', () => sendRequest('/leftswing/start'));
        swingleftBtn.addEventListener('mouseup', () => sendRequest('/stopwalk'));
        swingleftBtn.addEventListener('touchstart', () => sendRequest('/leftswing/start'));
        swingleftBtn.addEventListener('touchend', () => sendRequest('/stopwalk'));
    }

    const swingrightBtn = document.getElementById('swingright-button');
    if (swingrightBtn) {
        swingrightBtn.addEventListener('mousedown', () => sendRequest('/rightswing/start'));
        swingrightBtn.addEventListener('mouseup', () => sendRequest('/stopwalk'));
        swingrightBtn.addEventListener('touchstart', () => sendRequest('/rightswing/start'));
        swingrightBtn.addEventListener('touchend', () => sendRequest('/stopwalk'));
    }

    // Moonwalk Button
    const moonwalkBtn = document.getElementById('moonwalk-button');
    if (moonwalkBtn) {
        moonwalkBtn.addEventListener('click', () => sendRequest('/startmoonwalk'));
    }

    // Steps Button
    const stepsBtn = document.getElementById('steps-button');
    if (stepsBtn) {
        stepsBtn.addEventListener('click', () => sendRequest('/startsteps'));
    }

    // Walk Control Buttons
    const walkleftBtnForward = document.getElementById('walkleftForward-button');
    if (walkleftBtnForward) {
        walkleftBtnForward.addEventListener('click', () => sendRequest('/walkleftForward'));
    }

    const walkrightBtnForward = document.getElementById('walkrightForward-button');
    if (walkrightBtnForward) {
        walkrightBtnForward.addEventListener('click', () => sendRequest('/walkrightForward'));
    }

    const walkleftBtnBack = document.getElementById('walkleftBack-button');
    if (walkleftBtnBack) {
        walkleftBtnBack.addEventListener('click', () => sendRequest('/walkleftBack'));
    }

    const walkrightBtnBack = document.getElementById('walkrightBack-button');
    if (walkrightBtnBack) {
        walkrightBtnBack.addEventListener('click', () => sendRequest('/walkrightBack'));
    }

    // Walk Buttons
    const walkBtn = document.getElementById('walk-button');
    if (walkBtn) {
        walkBtn.addEventListener('click', () => sendRequest('/startwalk'));
    }

    const stopwalkBtn = document.getElementById('stopwalk-button');
    if (stopwalkBtn) {
        stopwalkBtn.addEventListener('click', () => sendRequest('/stopwalk'));
    }

    const balerinaBtn = document.getElementById('balerina-button');
    if (balerinaBtn) {
        balerinaBtn.addEventListener('click', () => sendRequest('/startbalerina'));
    }

    const weirdBtn = document.getElementById('weird-button');
    if (weirdBtn) {
        weirdBtn.addEventListener('click', () => sendRequest('/startweird'));
    }

    const waddleBtn = document.getElementById('waddle-button');
    if (waddleBtn) {
        waddleBtn.addEventListener('click', () => sendRequest('/startwaddle'));
    }

    const boogieBtn = document.getElementById('boogie-button');
    if (boogieBtn) {
        boogieBtn.addEventListener('click', () => sendRequest('/startboogie'));
    }

    const drinkBtn = document.getElementById('drink-button');
    if (drinkBtn) {
        drinkBtn.addEventListener('click', () => sendRequest('/startdrink'));
    }
});