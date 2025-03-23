document.addEventListener("DOMContentLoaded", function () {
    function toggleElements() {
        let taskDropdown = document.querySelector("select[name='tasks']");
        let numberInput = document.querySelector("input[name='user_number']");
        let numberLabel = document.getElementById("number_label");
        let submitButton = document.getElementById("submit_btn");

        if (taskDropdown.value === "summarization") {
            numberInput.style.display = "inline";
            numberLabel.style.display = "inline";
            numberInput.disabled = false;
            numberLabel.textContent = "Enter minimum length: ";
            submitButton.disabled = false;
        } else if (taskDropdown.value === "keywords") {
            numberInput.style.display = "inline";
            numberLabel.style.display = "inline";
            numberInput.disabled = false;
            numberLabel.textContent = "Count : ";
            submitButton.disabled = false;
        } else if (taskDropdown.value === "Q&A") {
            numberInput.style.display = "none";
            numberLabel.style.display = "none";
            submitButton.disabled = false;
        } else {
            numberInput.style.display = "none";
            numberLabel.style.display = "none";
            submitButton.disabled = true;
        }
    }
    document.querySelector("select[name='tasks']").addEventListener("change", toggleElements);
});
