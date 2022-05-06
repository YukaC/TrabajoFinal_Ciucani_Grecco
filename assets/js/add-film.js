$( document ).ready(function() {
    $('#title-page').text("Subir Pelicula");
    $("#film-form").submit(function(event) {
        event.preventDefault();
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
            url: "http://127.0.0.1:5000/subir-pelicula",
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
                    alert ("Pelicula subida correctamente");
            })
            .fail(function(error) {
                alert ("Error al subir pelicula");
            })
            .always(function() {
                
            });

    });
});