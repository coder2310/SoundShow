
const input = document.querySelector('.password-input');

const error = document.querySelector('.error-message');
const timeout = null;

const showError = message =>{
    error.style.color = "#C91E1E";
    error.style.display = 'block';
    error.innerHTML = message;
};

const showPass = message => {
    error.style.color = '#119822';
    error.innerHTML = message;
}
const validatePassword = password => {
    const lowerRegex = new RegExp('^(?=.*[a-z]');
    const upperRegex = new RegExp('^(?=.*[A-Z]');
    const special = new RegExp('^(?=.*[!@#$%&]');
    const digits = new RegExp('^(?=.*[0-9]');
    if (password.length < 8){
        showError("Pass word to short");
    }
    else if (!lowerRegex.test(password)){
        showError("Must include at least one lower case");
    }
    else if (!upperRegex.test(password)){
        showError("Must include at least one upper case");

    }
    else if (!special.test(password)){
        showError("Must include at least one special");

    }
    else if (!digits.test(password)){
        showError("Must include at least one digit");
    }
    else{
        showPass("Valid password");
    }


}



    input.addEventListener('keyup', e => {

        const password = e.target.value;
        clearTimeout(timeout);
        timeout = setTimeout(() =>validatePassword(input.value), 400);
  
    });

