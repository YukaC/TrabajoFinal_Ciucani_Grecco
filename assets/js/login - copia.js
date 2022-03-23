$( document ).ready(function() {
    $("#login-form").submit(function(event) {
        event.preventDefault();
       const username = $("#login-username").val();
       const password = $("#login-password").val();
       $.post('http://127.0.0.1:5000/login-user', {username:username, password:password})
            .done(function(user) {  
                alert ("Bienvenido ");
            })
            .fail(function(error) {
                alert ("Usuario o contraseña incorrectos");
            })
            .always(function() {
                
            });
    });
});