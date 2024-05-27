//alert("hii")
var mainform = document.getElementById('m_form');
//alert(mainform);
mainform.onsubmit = function()
{ 
    var username = document.getElementById("user");
    //alert(username);
    var password = document.getElementById("pwd");
    var username_s = document.getElementById("u_user");
    var password_s = document.getElementById("u_pwd");
    username_s.style.display ="none";
    //alert(username_s);
    password_s.style.display ="none";
    
    if (username.value == "" && password.value == "") {
        username_s.innerHTML = "empty username";
        username_s.style.display ="block";
        //alert(username_s);
        password_s.innerHTML = "empty password";
        password_s.style.display ="block";
        return false;
    }
    if (username.value == "") {
        username_s.style.display ="block";
        username_s.innerHTML = "empty username";
        return false;
    }
    if (password.value == "") {
        password_s.style.display ="block";
        password_s.innerHTML = "empty password";
        return false;
    }
    //if (username.value.match == "^[a-z]+[\._]?[a-z 0-9]+[@]\w+[.]\w{2,3}$" && password.value.match == "^ /0-9/g") {
    //    return false;
    //}
    //if (username.value.match== "^[a-z]+[\._]?[a-z 0-9]+[@]\w+[.]\w{2,3}$") {
    //   username_s.innerHTML = "must be in this format'abc@domain.xyz";
    //    return false;
    //}
    //if (password.value.match == "^ /0-9/g") {
    //   password_s.innerHTML = "must contain 6 digits";
    //    return false;
    // }
    //if (username.value != "" && password.value != "") {
      //  return false;
   // }
    alert("ckecking");
    return true; 
}
