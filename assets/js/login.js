$( document ).ready(function() {

    $("#login-form").submit(function(event) {
        event.preventDefault();
        const username = $("#login-username").val();
        const password = $("#login-password").val();
        if (username == "" || password == "") {
            alert("Debe completar todos los campos");
        }
        else {
        $.ajax({
            type: "POST",
            url: "http://127.0.0.1:5000/login-user",
            headers: {  'Access-Control-Allow-Origin': '*', 'Accept': 'application/json' },
            contentType: "application/x-www-form-urlencoded; charset=UTF-8",
            dataType: "json",
            data: { 
                username: username,
                password: password
            }
        })
            .done(function(user) { 
                sessionStorage.setItem("logged_In", true); 
                alert ("Bienvenido ");
                sessionStorage.setItem('username', $("#login-username").val());
                window.location = './index.html';
            })
            .fail(function(error) {
                sessionStorage.setItem("logged_In", false);
                sessionStorage.setItem('username', "");
                alert ("Usuario o contraseña incorrectos");
            })
        }
    });
});