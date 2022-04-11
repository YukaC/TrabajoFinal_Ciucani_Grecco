$(document).ready(function() {
    if (sessionStorage.getItem("logged_In") == "true"){
        $('#login-button').hide();
        $('#logout-button').show();
        $('upload-button').show();
      }
      else{
        $('#login-button').show();
        $('#upload-button').hide();
        $('#logout-button').hide();
      }
    
      let a = document.getElementById("logout-button"); // Encuentra el elemento "a" con el id "logout-button" en el sitio
      a.onclick = logout; // Agrega función onclick al elemento

      function logout(evento) {
        alert("Sesión Finalizada");
        sessionStorage.setItem("logged_In", false);
        window.location.reload();
      }
});
