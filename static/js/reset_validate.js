var resetform = document.getElementById('r_form');
console.log(resetform);
resetform.onsubmit = function()
{
    var npassword = document.getElementById("npwd");
    var cpassword = document.getElementById("cpwd");
    var password_n = document.getElementById("n_pwd");
    var password_c = document.getElementById("c_pwd");
    password_n.style.display ="none";
    password_c.style.display ="none";

    if (npassword.value == "" && cpassword.value === npassword.value) {
        password_n.innerHTML = "empty password";
        password_n.style.display ="block";
        password_c.innerHTML = "empty confirmation password";
        password_c.style.display ="block";
        return false;
    }
    if (npassword.value == "") {
        password_n.style.display ="block";
        password_n.innerHTML = "empty password";
        return false;
    }
    if (cpassword.value == "") {
        password_c.style.display ="block";
        password_c.innerHTML = "enter confirmation password";
        return false;
    }
    
    return true;
    }
     