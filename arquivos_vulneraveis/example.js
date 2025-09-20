// vulnerable_examples/example.js
function renderUserInput(userInput) {
    // Simulated XSS vulnerability: writing raw user input to the document
    document.write("Hello " + userInput);
}

renderUserInput('<img src=x onerror=alert(1)>');
