$( document ).ready(function() {
    $.ajax({
        method: "GET",
        url: "http://127.0.0.1:5000/random",
        headers: {  'Access-Control-Allow-Origin': '*' },
        contentType: "application/json; charset=utf-8"
    })
        .done(function(pelicula) {
            $('#title-span').text(pelicula.nombre);
            $('#year-span').text(pelicula.year);
            $('#duration-span').text(pelicula.duracion);
            $('#gender-span').text(pelicula.genero + "/" + pelicula.genero2 );
            $('#score-span').text(pelicula.score);
            $('#img-banner').attr('src','http://127.0.0.1:5000/static/'+pelicula.id+'-banner.jpg');
            $('#link-film').attr('href','./pelicula.html?id='+pelicula.id);
        });

});