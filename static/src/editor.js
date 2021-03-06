// Get the compiled markdown container
var compiled = document.querySelector('#compiled-markdown');

// Listen for changes to inputs and textareas
document.addEventListener('input', function (event) {

	// Only run if the change happened in the #editor
	if (!event.target.matches('#editor')) return;

	compiled.innerHTML = marked(event.target.value, { sanitize: true });

}, false);
