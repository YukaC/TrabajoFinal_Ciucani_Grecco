$( document ).ready(function() {
    $.ajax({
        method: "GET",
        url: "http://127.0.0.1:5000/peliculas",
        headers: {  'Access-Control-Allow-Origin': '*' },
        contentType: "application/json; charset=utf-8"
    })
        .done(function(films) {
            console.log(films)
            
            $.each(films, function(index, film) {
                $('#movies-grid').append('\
                <div class="movie-card">\
                <div class="card-head">\
                  <a href="./pelicula.html">\
                  <img src="http://127.0.0.1:5000/static/'+film.id+'.jpg" alt="" class="card-img">\
                  <div class="card-overlay">\
                    <div class="rating">\
                      <img src= "assets/images/star.png">\
                      <span>'+film.score+'</span>\
                    </div>\
                    <div class="play">\
                      <img src= "assets/images/play-movie.png">\
                    </div>\
                  </div>\
                  </a>\
                </div>\
                <div class="card-body">\
                  <h3 class="card-title">'+film.name+'</h3>\
                  <div class="card-info">\
                    <span class="genre">'+film.g1_name+'/'+film.g2_name +'</span>\
                    <span class="year">'+film.year+'</span>\
                  </div>\
                </div>\
              </div>')

            });
        });

});