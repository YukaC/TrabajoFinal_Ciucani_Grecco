$(document).ready(function() {
      $.ajax({
          method: "GET",
          url: "http://127.0.0.1:5000/login-check",
          headers: {  'Access-Control-Allow-Origin': '*' },
          contentType: "application/json; charset=utf-8"  
      })
      .done(function(log) {
        if (log == "1"){
          sessionStorage.setItem("logged_In", "true");
          $('#login-button').hide();
          $('#logout-button').show();
          $('upload-button').show();
        }
        else{
          sessionStorage.setItem("logged_In", "false");
          $('#login-button').show();
          $('#logout-button').hide();
          $('#upload-button').hide();
        }

      });
});
