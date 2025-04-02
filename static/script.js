document.addEventListener("DOMContentLoaded", function () {
    function toggleElements() {
        let taskDropdown = document.querySelector("select[name='tasks']");
        let numberInput = document.querySelector("input[name='user_number']");
        let numberLabel = document.getElementById("number_label");
        let questionInput = document.querySelector("input[name='user_question']");
        let questionLabel = document.getElementById("question_label");
        let submitButton = document.getElementById("submit_btn");

        if (taskDropdown.value === "summarization") {
            numberInput.style.display = "inline";
            numberLabel.style.display = "inline";
            numberInput.disabled = false;
            numberLabel.textContent = "Enter minimum length: ";
            questionInput.style.display = "none";
            questionLabel.style.display = "none";
            submitButton.disabled = false;
        } else if (taskDropdown.value === "keywords") {
            numberInput.style.display = "inline";
            numberLabel.style.display = "inline";
            numberInput.disabled = false;
            numberLabel.textContent = "Count: ";
            questionInput.style.display = "none";
            questionLabel.style.display = "none";
            submitButton.disabled = false;
        } else if (taskDropdown.value === "Q&A") {
            numberInput.style.display = "none";
            numberLabel.style.display = "none";
            questionInput.style.display = "inline";
            questionLabel.style.display = "inline";
            submitButton.disabled = false;
        } else {
            numberInput.style.display = "none";
            numberLabel.style.display = "none";
            questionInput.style.display = "none";
            questionLabel.style.display = "none";
            submitButton.disabled = true;
        }
    }

    function updateCount() {
        let textArea = document.getElementById("user_text");
        let countDisplay = document.getElementById("charCount");
        let remaining = 5000 - textArea.value.length;
        countDisplay.textContent = remaining + " characters remaining";
    }

    document.querySelector("select[name='tasks']").addEventListener("change", toggleElements);
    document.getElementById("user_text").addEventListener("input", updateCount);

    toggleElements();
    updateCount();
});