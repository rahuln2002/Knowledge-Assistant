document.addEventListener("DOMContentLoaded", function () {
    function toggleElements() {
        let taskDropdown = document.querySelector("select[name='tasks']");
        let numberInput = document.getElementById("number");
        let numberLabel = document.getElementById("number_label");
        let questionInput = document.getElementById("question");
        let questionLabel = document.getElementById("question_label");
        let submitButton = document.getElementById("submit_btn");

        numberInput.style.display = "none";
        numberLabel.style.display = "none";
        questionInput.style.display = "none";
        questionLabel.style.display = "none";
        submitButton.disabled = true;

        if (taskDropdown.value === "summarization") {
            numberLabel.textContent = "Enter minimum length: ";
            numberInput.style.display = "inline";
            numberLabel.style.display = "inline";
            submitButton.disabled = false;
        } else if (taskDropdown.value === "keywords") {
            numberLabel.textContent = "Count: ";
            numberInput.style.display = "inline";
            numberLabel.style.display = "inline";
            submitButton.disabled = false;
        } else if (taskDropdown.value === "Q&A") {
            questionInput.style.display = "inline";
            questionLabel.style.display = "inline";
            submitButton.disabled = false;
        }
    }

    function updateCount() {
        let textArea = document.getElementById("user_text");
        let countDisplay = document.getElementById("charCount");

        if (textArea) {
            let remaining = 5000 - textArea.value.length;
            countDisplay.textContent = `${remaining} characters remaining`;
        }
    }

    function showLoading() {
        document.getElementById("loading").style.display = "block";
    }

    function hideLoading() {
        document.getElementById("loading").style.display = "none";
    }

    document.querySelector("select[name='tasks']").addEventListener("change", toggleElements);
    document.getElementById("user_text").addEventListener("input", updateCount);
    
    // Show loading on form submission
    document.getElementById("textForm").addEventListener("submit", function () {
        showLoading();
    });

    toggleElements();
    updateCount();
});