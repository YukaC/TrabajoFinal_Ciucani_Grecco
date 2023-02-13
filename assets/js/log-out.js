$(document).ready(function() {
    document.getElementById("logout-button").onclick = function() {

        $.ajax({
            method: "POST",
            url: "http://127.0.0.1:5000/logout-user",
            headers: {  'Access-Control-Allow-Origin': '*' },
            contentType: "application/json; charset=utf-8"
        })

        .done(function(user) {
            
                    alert("Sesión Finalizada");
                    sessionStorage.setItem("logged_In", false);
                    sessionStorage.setItem('username', "");
                    window.location.reload();
        });

    }
});
