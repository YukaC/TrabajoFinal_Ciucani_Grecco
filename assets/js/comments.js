$( document ).ready(function() {
    const queryString = window.location.search;
    const urlParams = new URLSearchParams(queryString);
    $.ajax({
        method: "GET",
        url: "http://127.0.0.1:5000/peliculas/"+urlParams.get('id')+"/comentarios",
        headers: {  'Access-Control-Allow-Origin': '*' },
        contentType: "application/json; charset=utf-8"
    })
        .done(function(comentarios) {
            $.each(comentarios, function(index, comentario) {
            $('#comments-cont').append ('\
            <div class="comment user-comment">\
                <img src="./assets/images/user.png" class="avatar" alt="Profile Avatar">\
                <div class="info">\
                    <span id="username" style="display: flex;">'+ comentario.usuario +'</span>\
                    <span id="comment-hour">'+ comentario.hora +'</span>\
                </div>\
              <p id="comment-user">'+ comentario.texto +'</p>\
              ');
            
            });
        });    
});