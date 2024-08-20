
var modal = document.getElementById("myModal");
var btn = document.getElementById("openModal");
var span = document.getElementsByClassName("close")[0];

btn.onclick = function () {
    modal.style.display = "block";
}

span.onclick = function () {
    modal.style.display = "none";
}

window.onclick = function (event) {
    if (event.target == modal) {
        modal.style.display = "none";
    }
}

// Save button functionality (Placeholder)
document.querySelector('.save-button').onclick = function () {
    alert('Form data saved!'); // Placeholder for save functionality
    modal.style.display = "none"; // Close modal after saving
}
