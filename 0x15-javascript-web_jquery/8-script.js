$.getJSON(
  'https://swapi-api.alx-tools.com/api/films/?format=json',
  function (data) {
    data.results.forEach(function (movie) {
      $('<li>').text(movie.title).appendTo('UL#list_movies');
    });
  }
);
