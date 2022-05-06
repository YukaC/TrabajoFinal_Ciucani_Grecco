$( document ).ready(function() {
   $("#comments-form").submit(function(event) {
        event.preventDefault();
        if (sessionStorage.getItem('logged_in') == false) {
            alert("Debes estar logueado para poder comentar");
        }
        const username = sessionStorage.getItem("username");
        const comment_hour = new Date().toLocaleDateString('en-GB');
        const comment = $("#add-comment").val();
        const queryString = window.location.search;
        const urlParams = new URLSearchParams(queryString);
        $.ajax({
            type: "POST",
            url: "http://127.0.0.1:5000/subir-comentario",
            headers: {  'Access-Control-Allow-Origin': '*', 'Accept': 'application/json' },
            contentType: "application/x-www-form-urlencoded; charset=UTF-8",
            dataType: "json",
            data: { 
                film_id: urlParams.get('id'),
                username: username,
                comment_date: comment_hour,
                comment: comment,
            }
        })
            .done(function(comentario) {
                    alert ("Comentario agregado correctamente");

                    $('#comments-cont').append ('\
                    <div class="comment user-comment">\
                        <img src="./assets/images/user.png" class="avatar" alt="Profile Avatar">\
                        <div class="info">\
                            <span id="username" style="display: flex;">'+ comentario.usuario +'</span>\
                            <span id="comment-hour">'+ comentario.hora +'</span>\
                        </div>\
                    <p id="comment-user">'+ comentario.texto +'</p>\
                    ');
            })

            .fail(function(error) {
                alert ("Error al añadir Comentario");
            })
        });
});