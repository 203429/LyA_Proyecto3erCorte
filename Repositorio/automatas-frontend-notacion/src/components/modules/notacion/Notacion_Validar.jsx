import React, { Component } from 'react';
import axios from 'axios';
import { NavLink } from "react-router-dom";

import './../../global/assets/css/styles.css';

function Notacion_Validar() {

    const get_data = () => {
        let answer_aux = document.getElementById('notacion').value
        let answer = answer_aux.split(' ').join('')

        const request_options = {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
        };
        var post_data = {
            Conjunto: answer
        }

        axios
            .post("http://127.0.0.1:8000/api/notacion/verificar", post_data, request_options)
            .then(response => {
                if ("Valido" === response.data.status) {
                    document.getElementById('incorrect1').style.display = "none"
                    document.getElementById('correct1').style.display = "block"
                } else {
                    document.getElementById('correct1').style.display = "none"
                    document.getElementById('incorrect1').style.display = "block"
                }
            })
            .catch((error) => {
                alert("Verifique los datos de ingreso")
            });
    }

    return (
        <>
            <div className='container mt-3'>

                <ul className="nav nav-tabs mb-3">
                    <li className="nav-item">
                        <NavLink to="/notacion/" className="nav-link">Regresar al menú</NavLink>
                    </li>
                    <li className="nav-item">
                        <NavLink to="/notacion/quiz" className="nav-link">Quiz</NavLink>
                    </li>
                    <li className="nav-item">
                        <NavLink to="/notacion/validar" aria-current="page" className="nav-link active">Validar</NavLink>
                    </li>
                </ul>

                <h1 className='fs-3 text-bold mb-3'>Validar</h1>

                <div class="card border-dark text-center mb-3">
                    <div class="card-header">
                        Introduzca un conjunto a validar:
                    </div>
                    <div class="card-body">
                        <h5 class="card-title fw-bold">Validar Conjunto</h5>
                        <p class="card-text">Se puede validar la notación de conjuntos.</p>
                        <div className="input-group mb-2">
                            <div className="form-floating">
                                <input type="text" className="form-control" id="notacion" placeholder="Escriba aquí" />
                                <label for="floatingInputGroup1">Escriba aquí</label>
                            </div>
                        </div>
                        <button className="btn btn-outline-success" type="button" id="button-addon1" onClick={get_data}>Validar</button>
                    </div>
                </div>
                <div class="alert alert-success fw-bolder" style={{ display: 'none' }} role="alert" id="correct1">
                    ✔ - Conjunto valido
                </div>
                <div class="alert alert-danger fw-bolder" style={{ display: 'none' }} role="alert" id="incorrect1">
                    X - Conjunto no valido
                </div>


            </div>

        </>
    )
}

export default Notacion_Validar;