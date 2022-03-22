$( document ).ready(function() {
    const queryString = window.location.search;
    const urlParams = new URLSearchParams(queryString);
    $.ajax({
        method: "GET",
        url: "http://127.0.0.1:5000/comentarios",
        headers: {  'Access-Control-Allow-Origin': '*' },
        contentType: "application/json; charset=utf-8"
    })
        .done(function(pelicula) {

            $each(pelicula, function(index, comentario) {
                $('#comments-cont').append('\
                <img src="./assets/images/user.png" class="avatar" alt="Profile Avatar">\
                <div class="info">\
                    <span id="username" style="display: flex;"></span>\
                    <span id="comment-hour"></span>\
                </div>\
                <p id="comment-user"></p>')
            });
        });
    });