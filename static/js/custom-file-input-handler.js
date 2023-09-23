// This JS will update the label of the file input with the chosen file name
document.addEventListener("DOMContentLoaded", function() {
    // Your JS code here
    var fileInput = document.querySelector('.custom-file-input');
    if (fileInput) {  // Check if element exists
        fileInput.addEventListener('change', function (e) {
            var fileName = document.getElementById("customFile").files[0].name;
            var nextSibling = e.target.nextElementSibling;
            nextSibling.innerText = fileName;
        });
    }
});
