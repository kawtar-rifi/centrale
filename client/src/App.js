import React from 'react';
import logo from './logo.svg';
import './App.css';
import Superagent from 'superagent'
import Rater from 'react-rater' /* https://react.rocks/example/react-rater */
import 'react-rater/lib/react-rater.css'

function App() {

  //const movie_titles = ["Top Gun","Zorro","James Bond"];
  const movies_array = [{title:"Top Gun", date:1986 , note_moyenne:5, actor:"Tom Cruise"},
  {title:"Zorro", date:"?", note_moyenne:4},{title:"James Bond",actor:"Sean Connery",date:1990, note_moyenne:4}];
  //[{'title':"Top Gun", 'date':1986},{'title':"Zorro", 'date':"?"},{'title':"James Bond",'date':1990}];
  const [movie, setMovie] = React.useState(null);
  const [recommendation, setRecommendation] = React.useState(null);

  function LireInfo(obj) {
  if (obj)
        document.getElementById("idText").value=[obj.title, obj.date, obj.producer, obj.actor];
  else
        document.getElementById("idText").value="Pas de film";
  }
  function LireInfoFilm(obj) {
  if (obj)
        document.getElementById("idText2").value = String(obj);
  else
        document.getElementById("idText2").value="Pas de recommandation possible";
  }


  return (
    <div className="App">

      <header className="App-header">
      <img src={logo} className="App-logo" alt="logo" />
      <h1>Movie Guide</h1>
      <div/> {/* ne pas supprimer permet de gérer la présentation du bandeau titre (logo tout à gauche et titre centré)*/}
      </header>

      <div className="BandeNoire"/>

      <body className="App-body">

        <div ClassName="A_remplir">
          <label for="userid"> Renseignez vos noms et prénoms :</label>
          <div ClassName = "ligne">
            <input type="text" id="id_input_prenom" placeholder="Prénom"/>
            <input type="text" id="id_input_nom" placeholder="Nom"/>
            <button onClick={() =>
            Superagent
            .get(`http://localhost:8000/application/users/${document.getElementById('id_input_nom').value}/${document.getElementById('id_input_prenom').value}`)
            .then(response => {setRecommendation(response.body.best_movie);LireInfoFilm(recommendation)})}>Recommendation</button>
          </div>
        </div>

        <input type="text" id="idText2" size="50" value="pas de valeur" />

        <div ClassName = "ligne">
          <label for="site-search">Search for a movie :</label>
          <input type="search" id="site-search" name="q" aria-label="Search through site content" placeholder="Movie Title"/>
          <button onClick={() =>
           Superagent
           .get(`http://localhost:8000/application/movie/${document.getElementById('site-search').value}`)
           .then(response => {setMovie(response.body.movie);LireInfo(movie)})}>Search</button>
        </div>

        <input type="text" id="idText" size="50" value="pas de valeur" />


        <h2 fontsize="15px"> Films recommandés :</h2>
        <table>
          <thead>
            <tr>
              <th> Title</th>
              <th> Producer</th>
              <th> Date</th>
              <th> Main Actor</th>
              <th> Moyenne </th>
              <th> Noter ce film ! </th>
            </tr>
          </thead>
          <tbody>
            {movies_array.map(movie=> <tr>
                                        <td> {movie.title} </td>
                                        <td> {movie.producer} </td>
                                        <td> {movie.date} </td>
                                        <td> {movie.actor} </td>
                                        <td> <Rater rating={movie.note_moyenne} total={5} interactive={false} /> </td>
                                        <td> <Rater total={5} onRate={null} interactive={true} /> </td>
                                      </tr>)}
          </tbody>
        </table>


        <h2 fontsize="15px"> Tous les films :</h2>
        <table>
          <thead>
            <tr>
              <th> Title</th>
              <th> Producer</th>
              <th> Date</th>
              <th> Main Actor</th>
              <th> Moyenne </th>
              <th> Noter ce film ! </th>
            </tr>
          </thead>
          <tbody>
            {movies_array.map(movie=> <tr>
                                        <td> {movie.title} </td>
                                        <td> {movie.producer} </td>
                                        <td> {movie.date} </td>
                                        <td> {movie.actor} </td>
                                        <td> <Rater rating={movie.note_moyenne} total={5} interactive={false} /> </td>
                                        <td> <Rater total={5} onRate={null} interactive={true} /> </td>
                                      </tr>)}
          </tbody>
        </table>
      </body>

      <footer className="App-footer">
        <p> © Copyright Tanguy Houette, Kawtar Rifi, Victor Gauthier</p>
      </footer>

    </div>
  );
}

export default App;
