const btnSignUp = document.querySelector('.btn-signup')
const pre_load = document.querySelector('.preload')


/** ------- preloa function */
function preload() {
    pre_load.style.opacity = "0";

    setTimeout(() => {
        pre_load.style.display = 'none';
    }, 500)
}



/**------------------ scroll rev */
ScrollReveal().reveal('.container', { delay: 150 });
