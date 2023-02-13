$( document ).ready(function() {
    $("#delete-button").click(function(event) {
        const queryString = window.location.search;
        const urlParams = new URLSearchParams(queryString);
        $.ajax({
            method: "DELETE",
            url:"http://127.0.0.1:5000/eliminar-pelicula/"+urlParams.get('id'),
            headers: {  'Access-Control-Allow-Origin': '*' },
            contentType: "application/json; charset=utf-8"
        })
            .done(function() {
                alert ("Pelicula eliminada correctamente");
                window.location.href = "index.html";
            })
            .fail(function() {
                alert ("Error al eliminar la pelicula, no se puede eliminar una pelicula con comentarios");
            });
    });
});