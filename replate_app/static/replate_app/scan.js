// Add event listeners to each tab button to change the heading
var btns = [document.getElementById('cam-btn'), document.getElementById('file-btn'), document.getElementById('text-btn')];
var sections = [document.getElementById('cam-section'), document.getElementById('file-section'), document.getElementById('text-section')];

// Focus the first one
for (var i = 0; i < btns.length; i++) {
    if (btns[i].offsetParent !== null) {
        btns[i].classList.add("active");
        sections[i].classList.add("active", "show");
        break;
    }
}

// Get a list of all the file upload areas (the camera and file upload tabs)
var fileUploads = document.querySelectorAll('.file-upload');
var AllFileInputs = document.querySelectorAll('.custom-file-input');

fileUploads.forEach(file => {
    // For file input areas
    var fileInput = file.querySelector('.custom-file-input');
    var fileLabel = file.querySelector('.custom-file-label');
    
    // For submit/cancel buttons
    var submitArea = file.querySelector('.submit-area');
    var submitBtn = file.querySelector('.submit-button');
    var cancelBtn = file.querySelector('.cancel-button');

    // For loading area
    var loadingArea = file.querySelector('.loading-area');

    // Hide the submti and loading areas at the start
    submitArea.style.display = loadingArea.style.display = "none";

    // Show submit box and filename when file is selected
    fileInput.addEventListener('change', async (e) => {
        fileLabel.innerHTML = fileInput.files[0].name; // show filename
        submitArea.style.display = "flex"; // show submit area
        console.log(fileInput.files[0])
        // Clear other file inputs
        fileUploads.forEach((upload, index) => {
            if (upload.classList.contains("active") == false && upload.classList.contains("show") == false) {
                console.log(upload, index)
                upload.querySelector(".custom-file-input").value = '';
                var uploadLabel = upload.querySelector(".custom-file-label");
                uploadLabel.innerHTML = uploadLabel.dataset.default;
            }
        });
    });

    // Show loading box, hide submit area, disable other tabs
    submitBtn.addEventListener('click', () => {
        submitArea.style.display = "none";
        loadingArea.style.display = "flex";

        // Disable the file upload + other tabs
        fileInput.parentElement.style.display = "none";
        fileInput.parentElement.style.display = "none";
        for (var i = 0; i < btns.length; i++) {
            if ((btns[i].classList.contains("active")) === false) {
                btns[i].classList.add("disabled");
            }
        }
    })

    // Delete file list and hide submit area when cancel is clicked
    cancelBtn.addEventListener('click', () => {
        submitArea.style.display = "none";
        fileInput.value = '';
        fileLabel.innerHTML = fileLabel.dataset.default;
    })
});