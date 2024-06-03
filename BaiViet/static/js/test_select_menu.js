const selectBtn = document.querySelector(".select-btn");
const selectedcount = document.querySelector(".selected-count");
const arrow = document.querySelector(".arrow");
const selectItems = document.querySelector(".select-items");
const checkBoxes = document.querySelectorAll("input[type=checkbox]");
let selectedCount = 0;

selectBtn.addEventListener("click", () => {

    arrow.classList.toggle("active");
    selectItems.classList.toggle("active");

});


checkBoxes.forEach(box => {
    box.addEventListener("input", () => {
        if (box.checked)
            selectedcount.textContent = `${++selectedCount} Selected`;
        else {
            if (--selectedCount === 0)
                selectedcount.textContent = "Select Language";
            else
                selectedcount.textContent = `${selectedCount} Selected`;
        }

    })
});

