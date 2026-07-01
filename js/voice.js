
/* voice.js - Voice input and speech search support */
export function initializeVoice() {
    const voiceToggle = document.querySelector('#voiceSearch');
    const Recognition = window.SpeechRecognition || window.webkitSpeechRecognition;
    if (!voiceToggle || !Recognition) return;

    const recognition = new Recognition();
    recognition.lang = 'en-US';
    recognition.interimResults = false;
    recognition.maxAlternatives = 1;

    voiceToggle.addEventListener('click', () => {
        recognition.start();
    });

    recognition.addEventListener('result', (event) => {
        const query = event.results[0][0].transcript;
        const input = document.querySelector('#searchInput');
        if (input) {
            input.value = query;
            input.dispatchEvent(new Event('input'));
        }
    });
}
