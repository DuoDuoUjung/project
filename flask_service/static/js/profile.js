// 打開模态框
function openModal() {
  document.getElementById("avatarModal").style.display = "block";
}

// 關閉模态框
function closeModal() {
  document.getElementById("avatarModal").style.display = "none";
}

// 選擇頭像並應用
function selectAvatar(imageSrc) {
  document.getElementById("profileimg").src = imageSrc;
  closeModal();
}

// 點擊模态框外部區域時關閉模态框
window.onclick = function (event) {
  const modal = document.getElementById("avatarModal");
  if (event.target == modal) {
    closeModal();
  }
};

//點擊控制
document.addEventListener("DOMContentLoaded", () => {
  const toggleInput = (id, inputId) => {
    const element = document.getElementById(id);
    const input = document.getElementById(inputId);

    element.addEventListener("click", () => {
      element.classList.add("hidden");
      input.classList.remove("hidden");
      input.focus();
    });
  };

  toggleInput("account-text", "account-input");
  toggleInput("name-text", "name-input");
  toggleInput("email-text", "email-input");
  toggleInput("password-text", "password-input");
  toggleInput("birth-text", "birth-input");

  const form = document.querySelector("form");
  form.addEventListener("submit", (e) => {
    const emailInput = document.getElementById("email-input");
    const passwordInput = document.getElementById("password-input");

    const email = emailInput.value;
    const password = passwordInput.value;

    if (!email.includes("@")) {
      e.preventDefault();
      emailInput.setCustomValidity('信箱必須包含 "@"');
      emailInput.reportValidity();
      return;
    } else {
      emailInput.setCustomValidity("");
    }

    const passwordRegex = /^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$/;
    if (!passwordRegex.test(password)) {
      e.preventDefault();
      passwordInput.setCustomValidity("密碼至少要包含一個英文字母和一個數字，且最少 8 個字元");
      passwordInput.reportValidity();
      return;
    } else {
      passwordInput.setCustomValidity("");
    }
  });
});
