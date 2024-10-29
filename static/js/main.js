/*===== LOGIN SHOW and HIDDEN =====*/

const signUp = document.getElementById('sign-up'),
    signIn = document.getElementById('sign-in'),
    loginIn = document.getElementById('login-in'),
    loginUp = document.getElementById('login-up'),
    seller_register = document.getElementById('login-up-seller'),
    sing_up_seller = document.getElementById('sign-up-seller');


   
    
function func(){
    
    // remove
    loginIn.classList.remove('block')
    seller_register.classList.remove('none')

    //ADD
    loginIn.classList.toggle('none')
    seller_register.classList.toggle('block')

}

    function func2(){
        
        // remove
        loginIn.classList.remove('none')
        seller_register.classList.remove('block')
    
        //ADD
        loginIn.classList.toggle('block')
        seller_register.classList.toggle('none')

    }
   



    
signUp.addEventListener('click', ()=>{
    // Remove classes first if they exist
    loginIn.classList.remove('block')
    loginUp.classList.remove('none')

    // Add classes
    loginIn.classList.toggle('none')
    loginUp.classList.toggle('block')
})

signIn.addEventListener('click', ()=>{
    // Remove classes first if they exist
    loginIn.classList.remove('none')
    loginUp.classList.remove('block')

    // Add classes
    loginIn.classList.toggle('block')
    loginUp.classList.toggle('none')
})



 


