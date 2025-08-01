document.addEventListener('DOMContentLoaded', () => {
    function sendRequest(url) {
        fetch(url).catch(err => console.error('Request failed:', err));
    }

    const leftBtn = document.getElementById('left-button');
    const rightBtn = document.getElementById('right-button');
    const moonwalkBtn = document.getElementById('moonwalk-button');
    const danceBtn = document.getElementById('dance-button');
    const walkleftBtn = document.getElementById('walkleft-button');
    const walkrightBtn = document.getElementById('walkright-button');

    if (leftBtn) {
        leftBtn.addEventListener('mousedown', () => sendRequest('/leftswing/start'));
        leftBtn.addEventListener('mouseup', () => sendRequest('/stopswing'));
        leftBtn.addEventListener('touchstart', () => sendRequest('/leftswing/start'));
        leftBtn.addEventListener('touchend', () => sendRequest('/stopswing'));
    }

    if (rightBtn) {
        rightBtn.addEventListener('mousedown', () => sendRequest('/rightswing/start'));
        rightBtn.addEventListener('mouseup', () => sendRequest('/stopswing'));
        rightBtn.addEventListener('touchstart', () => sendRequest('/rightswing/start'));
        rightBtn.addEventListener('touchend', () => sendRequest('/stopswing'));
    }

    if (moonwalkBtn) {
        moonwalkBtn.addEventListener('click', () => sendRequest('/moonwalk'));
    }

    if (danceBtn) {
        danceBtn.addEventListener('click', () => sendRequest('/dance'));
    }

    if (walkleftBtn) {
        walkleftBtn.addEventListener('click', () => sendRequest('/walkleft'));
    }

    if (walkrightBtn) {
        walkrightBtn.addEventListener('click', () => sendRequest('/walkright'));
    }

});
