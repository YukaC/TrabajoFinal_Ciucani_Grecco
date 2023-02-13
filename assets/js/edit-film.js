$( document ).ready(function() {
    $('#title-page').text("Editar Pelicula");
    const queryString = window.location.search;
    const urlParams = new URLSearchParams(queryString);
    $.ajax({
        method: "GET",
        url: "http://127.0.0.1:5000/mostrar-pelicula/"+urlParams.get('id'),
        headers: {  'Access-Control-Allow-Origin': '*' },
        contentType: "application/json; charset=utf-8"
    })
        .done(function(pelicula) {
            $("#edit-sinopsis").val(pelicula.sinopsis);
            $("#edit-nombre-pelicula").val(pelicula.nombre);
            $("#edit-genero").val(pelicula.genero);
            $("#edit-genero2").val(pelicula.genero2);
            $("#edit-director").val(pelicula.director);
            $("#edit-director2").val(pelicula.director2);
            $("#edit-duracion").val(pelicula.duracion);
            $("#edit-year").val(pelicula.year);
            $("#edit-score").val(pelicula.score);
        });

        $("#film-form").submit(function(event) {
            event.preventDefault();
            const nombre_pelicula = $("#edit-nombre-pelicula").val();
            const sinopsis = $("#edit-sinopsis").val();
            const genero = $("#edit-genero").val();
            const genero2 = $("#edit-genero2").val();
            const director = $("#edit-director").val();
            const director2 = $("#edit-director2").val();
            const duracion = $("#edit-duracion").val();
            const year = $("#edit-year").val();
            const score = $("#edit-score").val();
    
            $.ajax({
                type: "POST",
                url: "http://127.0.0.1:5000/editar-pelicula/"+urlParams.get('id'),
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