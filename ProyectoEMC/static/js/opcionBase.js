
document.addEventListener("DOMContentLoaded", function () {
    const menuItems = document.querySelectorAll(".menu ul li a");

    const currentUrl = window.location.pathname;

    menuItems.forEach(item => {
        if (item.getAttribute("href") === currentUrl) {
            item.classList.add("active");
        }
    });
});

