import React from 'react';
import axios from 'axios';
import './../../global/assets/css/styles.css';
import { NavLink } from "react-router-dom";
import validate_logo from './assets/imgs/validate.png'
import quiz_logo from './assets/imgs/quiz.png'

function Notacion() {
  return (
    <div className='container mt-3' style={{ width: 'auto' }}>
        <h1 className='fs-3 text-bold mb-3'>Notación</h1>
        <h2 className='text-m-23 text-regular text-center mb-4'>Selecciona una opción:</h2>

        <div className="row row-cols-md-4 g-4 justify-content-center">

          <div className="col">
            <div className="card h-100" style={{ width: 16 + 'rem' }}>
              <img src={quiz_logo} className="card-img-top" alt="image" />
              <div className="card-body align-items-center text-center">
                <h5 className="card-title text-m-23 text-bold">Quiz</h5>
                <p className="card-text">En este apartado se practica mediante un examen la notación de conjuntos.</p>
                <NavLink to="/notacion/quiz" className="btn btn-primary btn-submit text-bold mb-1 rounded-3">Iniciar</NavLink>
              </div>
            </div>
          </div>

          <div className="col">
            <div className="card h-100" style={{ width: 16 + 'rem' }}>
              <img src={validate_logo} className="card-img-top" alt="image" />
              <div className="card-body align-items-center text-center">
                <h5 className="card-title text-m-23 text-bold">Validar</h5>
                <p className="card-text">En este apartado se valida la notación de conjuntos.</p>
                <NavLink to="/notacion/validar" className="btn btn-primary btn-submit text-bold mb-1 mt-5 rounded-3">Iniciar</NavLink>
              </div>
            </div>
          </div>
          
        </div>

    </div>
  );
}

export default Notacion