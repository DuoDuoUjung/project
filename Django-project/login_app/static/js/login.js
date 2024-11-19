document.addEventListener('DOMContentLoaded', () => {
    const toggleInput = (id, inputId) => {
        const element = document.getElementById(id);
        const input = document.getElementById(inputId);
        
        element.addEventListener('click', () => {
            element.classList.add('hidden');
            input.classList.remove('hidden');
            input.focus();
        });
    };

    toggleInput('account-text', 'account-input');
    toggleInput('password-text', 'password-input');

    const form = document.querySelector('form');
    form.addEventListener('submit', (e) => {
        const accountInput = document.getElementById('account-input');
        const passwordInput = document.getElementById('password-input');

        accountInput.value = ''; 
        passwordInput.value = '';  
        
        const passwordRegex = /^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$/;
        if (!passwordRegex.test(password)) {
            e.preventDefault(); 
            passwordInput.setCustomValidity('密碼至少要包含一個英文字母和一個數字，且最少 8 個字元');
            passwordInput.reportValidity(); 
            return;
        } else {
            passwordInput.setCustomValidity(''); 
        }
    });
});