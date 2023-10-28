// Function to handle opening and closing modals with animation
function handleModal(modal, action) {
    if (action === 'open') {
        modal.style.display = 'block';
        modal.querySelector('.modal-content').style.transform = 'scale(1.1)';
        setTimeout(() => {
            modal.querySelector('.modal-content').style.transform = 'scale(1)';
        }, 1);
    } else if (action === 'close') {
        modal.querySelector('.modal-content').style.transform = 'scale(0.9)';
        setTimeout(() => {
            modal.style.display = 'none';
        }, 300);
    }
}

// Function to populate days and months in the select dropdown
function populateDateFields() {
    populateDays();
    populateMonths();

    function populateDays() {
        const daySelect = document.getElementById('day');
        for (let i = 1; i <= 31; i++) {
            const option = document.createElement('option');
            option.value = option.text = i;
            daySelect.appendChild(option);
        }
    }

    function populateMonths() {
        const months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"];
        const monthSelect = document.getElementById('month');
        months.forEach((month, index) => {
            const option = document.createElement('option');
            option.value = index + 1;
            option.text = month;
            monthSelect.appendChild(option);
        });
    }
}

// Event listener to handle actions when document is fully loaded
document.addEventListener('DOMContentLoaded', function () {
    const registrationModal = document.getElementById("registrationModal");
    const loginPopup = document.getElementById("loginPopup");
    const navbar = document.getElementById('navbar');

    document.getElementById("registerBtn").onclick = () => handleModal(registrationModal, 'open');
    document.getElementById("loginBtn").onclick = function () {
        handleModal(loginPopup, 'open');
        navbar.style.pointerEvents = "none";
    
    };

    Array.from(document.getElementsByClassName("close")).forEach(closeBtn => {
        closeBtn.onclick = function (event) {
            handleModal(event.target.closest('.modal'), 'close');
            navbar.style.pointerEvents = "auto";
        };
    });

    window.onclick = function (event) {
        if (event.target === registrationModal || event.target === loginPopup) {
            handleModal(event.target, 'close');
            navbar.style.pointerEvents = "auto";
        }
    };

    populateDateFields();
});

