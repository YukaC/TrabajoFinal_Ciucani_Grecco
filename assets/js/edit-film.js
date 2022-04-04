$( document ).ready(function() {
    $('#title-page').text("Editar Pelicula");
    const queryString = window.location.search;
    const urlParams = new URLSearchParams(queryString);
    $.ajax({
        method: "GET",
        url: "http://127.0.0.1:5000/peliculas/"+urlParams.get('id'),
        headers: {  'Access-Control-Allow-Origin': '*' },
        contentType: "application/json; charset=utf-8"
    })
        .done(function(pelicula) {
            $("#add-sinopsis").val(pelicula.sinopsis);
            $("#add-nombre-pelicula").val(pelicula.nombre);
            $("#add-genero").val(pelicula.genero);
            $("#add-director").val(pelicula.director);
            $("#add-duracion").val(pelicula.duracion);
            $("#add-year").val(pelicula.year);
            $("#add-score").val(pelicula.score);


        });

        $("#film-form").submit(function(event) {
            event.preventDefault();
            alert ("ejecuta");
            const nombre_pelicula = $("#add-nombre-pelicula").val();
            const sinopsis = $("#add-sinopsis").val();
            const genero = $("#add-genero").val();
            const genero2 = $("#add-genero2").val();
            const director = $("#add-director").val();
            const director2 = $("#add-director2").val();
            const duracion = $("#add-duracion").val();
            const year = $("#add-year").val();
            const score = $("#add-score").val();
    
            $.ajax({
                type: "POST",
                url: "http://127.0.0.1:5000/editar-pelicula+"+urlParams.get('id'),
                headers: {  'Access-Control-Allow-Origin': '*', 'Accept': 'application/json' },
                contentType: "application/x-www-form-urlencoded; charset=UTF-8",
                dataType: "json",
                data: { 
                    nombre_pelicula: nombre_pelicula,
                    sinopsis: sinopsis,
                    genero: genero,
                    genero2: genero2,
                    director: director,
                    director2: director2,
                    duracion: duracion,
                    year: year,
                    score: score,
                }
            })
                .done(function(pelicula) {
                        alert ("Pelicula editada correctamente");
                })
                .fail(function(error) {
                    alert ("Error al editar la pelicula");
                })
                .always(function() {
                    
                });
    
        });

    });