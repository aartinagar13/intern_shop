$(document).ready(function() {
    $('l_page').validate({
        rules:{
            user:{
                email:true,
                required:true,
            },
            pwd:{
                required:true,
                maxlength:6,
                minlength:4,
            },
        },
        messages:{
            user:{
            email:"must be in this format'abc@domain.xyz'",
            required:"shouldn't be empty"
            },
            pwd:{
                required:"Please provide password,can't be empty",
                maxlength:"not more then 6digits/letters",
                minlength:"please provide atleast 4 digits/letters"
            }
      }
    }) 
    return false;
})
return true;
