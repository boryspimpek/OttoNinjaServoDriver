document.addEventListener('DOMContentLoaded', () => {
    function sendRequest(url) {
        fetch(url).catch(err => console.error('Request failed:', err));
    }

    const leftBtn = document.getElementById('left-button');
    const rightBtn = document.getElementById('right-button');
    const moonwalkBtn = document.getElementById('moonwalk-button');
    const stepsBtn = document.getElementById('steps-button');
    const walkleftBtnForward = document.getElementById('walkleftForward-button');
    const walkrightBtnForward = document.getElementById('walkrightForward-button');
    const walkleftBtnBack = document.getElementById('walkleftBack-button');
    const walkrightBtnBack = document.getElementById('walkrightBack-button');
    const walkBtn = document.getElementById('walk-button');
    const stopwalkBtn = document.getElementById('stopwalk-button');

    if (leftBtn) {
        leftBtn.addEventListener('mousedown', () => sendRequest('/leftswing/start'));
        leftBtn.addEventListener('mouseup', () => sendRequest('/stopwalk'));
        leftBtn.addEventListener('touchstart', () => sendRequest('/leftswing/start'));
        leftBtn.addEventListener('touchend', () => sendRequest('/stopwalk'));
    }

    if (rightBtn) {
        rightBtn.addEventListener('mousedown', () => sendRequest('/rightswing/start'));
        rightBtn.addEventListener('mouseup', () => sendRequest('/stopwalk'));
        rightBtn.addEventListener('touchstart', () => sendRequest('/rightswing/start'));
        rightBtn.addEventListener('touchend', () => sendRequest('/stopwalk'));
    }

    if (moonwalkBtn) {
        moonwalkBtn.addEventListener('click', () => sendRequest('/startmoonwalk'));
    }

    if (stepsBtn) {
        stepsBtn.addEventListener('click', () => sendRequest('/startsteps'));
    }

    if (walkleftBtnForward) {
        walkleftBtnForward.addEventListener('click', () => sendRequest('/walkleftForward'));
    }

    if (walkrightBtnForward) {
        walkrightBtnForward.addEventListener('click', () => sendRequest('/walkrightForward'));
    }

    if (walkleftBtnBack) {
        walkleftBtnBack.addEventListener('click', () => sendRequest('/walkleftBack'));
    }

    if (walkrightBtnBack) {
        walkrightBtnBack.addEventListener('click', () => sendRequest('/walkrightBack'));
    }

    if (walkBtn) {
        walkBtn.addEventListener('click', () => sendRequest('/startwalk'));
    }
    if (stopwalkBtn) {
        stopwalkBtn.addEventListener('click', () => sendRequest('/stopwalk'));
    }

});
