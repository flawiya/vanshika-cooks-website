/**
 * Vanshika Cooks - Official Client-Side JavaScript
 * Bilingual Recipe Platform (@vanshikacooks)
 */

document.addEventListener("DOMContentLoaded", function () {
    initMobileDrawer();
    initServingsScaler();
    initNewsletterForms();
    initShareButton();
});

/* ==========================================================================
   Mobile Drawer Navigation
   ========================================================================== */
function initMobileDrawer() {
    const mobileMenuBtn = document.getElementById("mobileMenuBtn");
    const drawerCloseBtn = document.getElementById("drawerCloseBtn");
    const mobileDrawer = document.getElementById("mobileDrawer");
    const drawerBackdrop = document.getElementById("drawerBackdrop");

    if (!mobileMenuBtn || !mobileDrawer) return;

    function openDrawer() {
        mobileDrawer.classList.add("open");
        if (drawerBackdrop) drawerBackdrop.classList.add("open");
        document.body.style.overflow = "hidden";
    }

    function closeDrawer() {
        mobileDrawer.classList.remove("open");
        if (drawerBackdrop) drawerBackdrop.classList.remove("open");
        document.body.style.overflow = "";
    }

    mobileMenuBtn.addEventListener("click", openDrawer);
    if (drawerCloseBtn) drawerCloseBtn.addEventListener("click", closeDrawer);
    if (drawerBackdrop) drawerBackdrop.addEventListener("click", closeDrawer);
}

/* ==========================================================================
   Recipe Servings Scaler (Math Scaling)
   ========================================================================== */
function initServingsScaler() {
    const recipeArticle = document.getElementById("recipeArticle");
    const servingsDisplay = document.getElementById("servingsDisplay");
    const decreaseBtn = document.getElementById("decreaseServings");
    const increaseBtn = document.getElementById("increaseServings");
    const amountElements = document.querySelectorAll(".ing-amount");

    if (!recipeArticle || !servingsDisplay || !decreaseBtn || !increaseBtn) return;

    const baseServings = parseInt(recipeArticle.dataset.baseServings, 10) || 4;
    let currentServings = baseServings;

    function formatAmount(val) {
        if (val <= 0) return 0;
        // Check if practically an integer
        if (Math.abs(val - Math.round(val)) < 0.05) {
            return Math.round(val);
        }
        // Round to 1 or 2 decimals
        return Number(val.toFixed(2));
    }

    function updateAmounts() {
        servingsDisplay.textContent = currentServings;
        const ratio = currentServings / baseServings;

        amountElements.forEach(el => {
            const orig = parseFloat(el.dataset.originalAmount);
            if (!isNaN(orig)) {
                const scaled = orig * ratio;
                el.textContent = formatAmount(scaled);
            }
        });
    }

    decreaseBtn.addEventListener("click", function () {
        if (currentServings > 1) {
            currentServings -= 1;
            updateAmounts();
        }
    });

    increaseBtn.addEventListener("click", function () {
        if (currentServings < 20) {
            currentServings += 1;
            updateAmounts();
        }
    });
}

/* ==========================================================================
   Share Recipe Button & Toast Notification
   ========================================================================== */
function initShareButton() {
    const shareBtn = document.getElementById("shareRecipeBtn");
    if (!shareBtn) return;

    shareBtn.addEventListener("click", async function () {
        const title = document.title;
        const url = window.location.href;

        if (navigator.share) {
            try {
                await navigator.share({
                    title: title,
                    text: "Check out this delicious recipe from Vanshika Cooks (@vanshikacooks)!",
                    url: url
                });
                return;
            } catch (err) {
                // Fallback to clipboard if cancelled or failed
            }
        }

        // Clipboard fallback
        navigator.clipboard.writeText(url).then(() => {
            const isHindi = document.body.classList.contains("lang-hi");
            const msg = isHindi ? "रेसिपी लिंक कॉपी हो गया!" : "Recipe link copied to clipboard!";
            showToast("🔗 " + msg);
        }).catch(() => {
            showToast("Failed to copy link.");
        });
    });
}

/* ==========================================================================
   Copy Kitchen Tip
   ========================================================================== */
function copyTipText(btn, title) {
    const card = btn.closest(".tip-card-expanded");
    if (!card) return;
    const desc = card.querySelector(".tip-desc").textContent;
    const textToCopy = `💡 Kitchen Tip from Vanshika Cooks (@vanshikacooks):\n${title}\n\n${desc}\n\nRead more at: ${window.location.origin}/tips`;

    navigator.clipboard.writeText(textToCopy).then(() => {
        const isHindi = document.body.classList.contains("lang-hi");
        const msg = isHindi ? "टिप कॉपी हो गई!" : "Tip copied to clipboard!";
        showToast("✨ " + msg);
    });
}

/* ==========================================================================
   Newsletter AJAX Handlers
   ========================================================================== */
function initNewsletterForms() {
    const homeForm = document.getElementById("homeNewsletterForm");
    const footerForm = document.getElementById("footerNewsletterForm");

    if (homeForm) {
        homeForm.addEventListener("submit", function (e) {
            e.preventDefault();
            const input = document.getElementById("homeNewsletterEmail");
            const alertBox = document.getElementById("homeNewsletterAlert");
            submitNewsletter(input.value, alertBox, homeForm);
        });
    }

    if (footerForm) {
        footerForm.addEventListener("submit", function (e) {
            e.preventDefault();
            const input = document.getElementById("newsletterEmail");
            const alertBox = document.getElementById("newsletterAlert");
            submitNewsletter(input.value, alertBox, footerForm);
        });
    }
}

function submitNewsletter(email, alertBox, formEl) {
    if (!email) return;

    fetch("/api/subscribe", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ email: email })
    })
    .then(res => res.json())
    .then(data => {
        if (alertBox) {
            alertBox.style.color = "#4ade80";
            alertBox.textContent = "✓ " + data.message;
        }
        formEl.reset();
        showToast("🎉 " + data.message);
    })
    .catch(() => {
        if (alertBox) {
            alertBox.style.color = "#f87171";
            alertBox.textContent = "Something went wrong. Please try again.";
        }
    });
}

/* ==========================================================================
   Toast Notification Generator
   ========================================================================== */
function showToast(message) {
    let container = document.getElementById("toastContainer");
    if (!container) {
        container = document.createElement("div");
        container.id = "toastContainer";
        container.className = "toast-container";
        document.body.appendChild(container);
    }

    const toast = document.createElement("div");
    toast.className = "toast";
    toast.innerHTML = message;
    container.appendChild(toast);

    setTimeout(() => {
        toast.style.opacity = "0";
        toast.style.transform = "translateX(100%)";
        toast.style.transition = "all 0.3s ease";
        setTimeout(() => toast.remove(), 300);
    }, 3500);
}
