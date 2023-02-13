$( document ).ready(function() {

    if (sessionStorage.getItem("logged_In") == "true"){
        $("#edit-button").show();
    }
    else{
        $("#edit-button").hide();
        $(".navbar").show();
        $("#delete-button").hide();
    }
    const queryString = window.location.search;
    const urlParams = new URLSearchParams(queryString);
    $.ajax({
        method: "GET",
        url: "http://127.0.0.1:5000/peliculas/"+urlParams.get('id'),
        headers: {  'Access-Control-Allow-Origin': '*' },
        contentType: "application/json; charset=utf-8"
    })
        .done(function(pelicula) {
            $('#title-page').text("Ver " +pelicula.nombre);
            $('#p-nombre').html(pelicula.nombre);
            $('#p-año').html("Año: " + pelicula.year);
            $('#p-duracion').html("Duracion: " +pelicula.duracion);
            $('#p-genero').html("Genero: " + pelicula.genero + "/" + pelicula.genero2 );
            if (pelicula.director2 == null){
                $('#p-director').html("Director: " + pelicula.director);
            }
            else{
                $('#p-director').html("Directores: " + pelicula.director + "/" + pelicula.director2);
            }
            $('#p-sinopsis').html("Sinopsis: " + pelicula.sinopsis);
            $('#p-score').html("Puntuación: " + pelicula.score);
            $('#p-img').attr('src','http://127.0.0.1:5000/static/'+pelicula.id+'.jpg') 

            $('#edit-button-link').attr('href','edit-film.html?id='+pelicula.id);
        });
    });