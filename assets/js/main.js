$( document ).ready(function() {
    $.ajax({
        method: "GET",
        url: "http://127.0.0.1:5000/ultimas-peliculas",
        headers: {  'Access-Control-Allow-Origin': '*' },
        contentType: "application/json; charset=utf-8"
    })
        .done(function(peliculas) {
            
            $.each(peliculas, function(index, pelicula) {
                $('#movies-grid').append('\
                <div class="movie-card">\
                <div class="card-head">\
                  <a href="./pelicula.html?id='+pelicula.id+'">\
                  <img src="http://127.0.0.1:5000/static/'+pelicula.id+'.jpg" alt="" class="card-img">\
                  <div class="card-overlay">\
                    <div class="rating">\
                      <img src= "assets/images/star.png">\
                      <span>'+pelicula.score+'</span>\
                    </div>\
                    <div class="play">\
                      <img src= "assets/images/play-movie.png">\
                    </div>\
                  </div>\
                  </a>\
                </div>\
                <div class="card-body">\
                  <h3 class="card-title">'+pelicula.nombre+'</h3>\
                  <div class="card-info">\
                    <span class="genre">'+pelicula.genero+'/'+pelicula.genero2 +'</span>\
                    <span class="year">'+pelicula.year+'</span>\
                  </div>\
                </div>\
              </div>')

            });
        });

});