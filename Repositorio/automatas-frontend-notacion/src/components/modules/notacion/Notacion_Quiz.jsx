import React, { Component } from 'react';
import axios from 'axios';
import { NavLink } from "react-router-dom";
import './../../global/assets/css/styles.css';

class Notacion_Quiz extends Component {
    constructor() {
        super()
        this.state = {
            preguntas: [],
            p2: [],
            p4: [],
            aciertos: 0,
            calif: 0
        }
        this.split_text = this.split_text.bind(this)
        this.get_data = this.get_data.bind(this)
    }

    componentDidMount() {
        axios
            .get("http://127.0.0.1:8000/api/notacion/quiz", {
                headers: {
                    'Content-Type': 'application/json',
                },
            })
            .then(res => {
                this.setState({ preguntas: res.data })
                this.split_text()
            })
            .catch(error => {
                console.log(error);
            })
    }

    split_text = () => {
        let p2_aux = this.state.preguntas.p2
        let p4_aux = this.state.preguntas.p4
        try {
            let p2 = p2_aux.split("|")
            let p4 = p4_aux.split("|")
            this.setState({ p2: p2, p4: p4 })
        } catch (err) {
            return
        }
    }

    get_data = async () => {
        let data
        const request_options = {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
        };

        let aciertos = 0

        let respuesta0_aux = document.getElementById('pregunta0').value
        let respuesta0 = respuesta0_aux.split(' ').join('')

        let respuesta1_aux = document.getElementById('pregunta1').value
        let respuesta1 = respuesta1_aux.split(' ').join('')

        let respuesta2 = document.querySelector('input[name="flexRadioDefault1"]:checked').value

        let respuesta3_aux = document.getElementById('pregunta3').value
        let respuesta3 = respuesta3_aux.split(' ').join('')

        let respuesta4 = document.querySelector('input[name="flexRadioDefault2"]:checked').value

        let respuesta5_aux = document.getElementById('pregunta5').value
        let respuesta5 = respuesta5_aux.split(' ').join('')

        if (respuesta0 === null || respuesta0 === undefined || respuesta0 === "" ||
            respuesta1 === null || respuesta1 === undefined || respuesta1 === "" ||
            respuesta3 === null || respuesta3 === undefined || respuesta3 === "" ||
            respuesta5 === null || respuesta5 === undefined || respuesta5 === "") {
            alert("No puedes dejar campos vacios")
            return
        }

        // PREGUNTA 1
        var post_data = {
            Conjunto: respuesta0
        }

        await axios
            .post("http://127.0.0.1:8000/api/notacion/verificar", post_data, request_options)
            .then((response) => {
                data = response.data.status
            })
            .catch((error) => {
                console.log(error)
            });

        if (data === "Valido") {
            document.getElementById('p0c').style.display = "block"
            aciertos++
        } else {
            document.getElementById('p0i').style.display = "block"
        }

        // PREGUNTA 2
        var post_data = {
            Conjunto: respuesta1
        }

        await axios
            .post("http://127.0.0.1:8000/api/notacion/verificar", post_data, request_options)
            .then((response) => {
                data = response.data.Cardinalidad
            })
            .catch((error) => {
                console.log(error)
            });

        if (data === this.state.preguntas.p1) {
            document.getElementById('p1c').style.display = "block"
            aciertos++
        } else {
            document.getElementById('p1i').style.display = "block"
        }

        // PREGUNTA 3

        if (respuesta2 === this.state.p2[this.state.p2[3] - 1]) {
            document.getElementById('p2c').style.display = "block"
            aciertos++
        } else {
            document.getElementById('p2i').style.display = "block"
        }

        // PREGUNTA 4
        var post_data = {
            Conjunto: respuesta3
        }

        await axios
            .post("http://127.0.0.1:8000/api/notacion/verificar", post_data, request_options)
            .then((response) => {
                data = response.data.Cardinalidad
            })
            .catch((error) => {
                console.log(error)
            });

        if (data === this.state.preguntas.p3) {
            document.getElementById('p3c').style.display = "block"
            aciertos++
        } else {
            document.getElementById('p3i').style.display = "block"
        }

        // PREGUNTA 5
        if (respuesta4 === this.state.p4[this.state.p4[3] - 1]) {
            document.getElementById('p4c').style.display = "block"
            aciertos++
        } else {
            document.getElementById('p4i').style.display = "block"
        }

        // PREGUNTA 6
        var post_data = {
            Conjunto: respuesta5
        }

        await axios
            .post("http://127.0.0.1:8000/api/notacion/verificar", post_data, request_options)
            .then((response) => {
                data = response.data.Cardinalidad
            })
            .catch((error) => {
                console.log(error)
            });

        if (data === this.state.preguntas.p5) {
            document.getElementById('p5c').style.display = "block"
            aciertos++
        } else {
            document.getElementById('p5i').style.display = "block"
        }

        document.getElementById('reinicio').style.display = "block"
        document.getElementById('enviar').style.display = "none"
        let calif = (aciertos / 6) * 100
        calif=Math.round(calif)
        this.setState({ aciertos: aciertos, calif: calif })

        document.getElementById('resumen').style.display = "block"
    }

    render() {
        return (
            <div className='container mt-3'>

                <ul className="nav nav-tabs mb-3">
                    <li className="nav-item">
                        <NavLink to="/notacion/" className="nav-link">Regresar al menú</NavLink>
                    </li>
                    <li className="nav-item">
                        <NavLink to="/notacion/quiz" aria-current="page" className="nav-link active">Quiz</NavLink>
                    </li>
                    <li className="nav-item">
                        <NavLink to="/notacion/validar" className="nav-link">Validar</NavLink>
                    </li>
                </ul>

                <h1 className='fs-3 text-bold mb-3'>Quiz</h1>

                <div class="card text-bg-secondary text-center mb-4">
                    <div class="card-header">
                        Pregunta 1
                    </div>
                    <div class="card-body">
                        <h5 class="card-title">Indique la respuesta correcta</h5>
                        <p class="card-text">Escriba un conjunto valido.</p>
                        <input type="text" className="form-control mb-3" id="pregunta0" placeholder="Escriba su respuesta aquí" />
                    </div>
                </div>
                <div class="alert alert-success" style={{ display: 'none' }} role="alert" id="p0c">
                    ✔ Respuesta correcta
                </div>
                <div class="alert alert-danger" style={{ display: 'none' }} role="alert" id="p0i">
                    X Respuesta incorrecta
                </div>

                <div class="card text-bg-secondary text-center mb-4">
                    <div class="card-header">
                        Pregunta 2
                    </div>
                    <div class="card-body">
                        <h5 class="card-title">Indique la respuesta correcta</h5>
                        <p class="card-text">Escriba un conjunto con cardinalidad {this.state.preguntas.p1}. Tome en cuenta la notación de conjuntos.</p>
                        <input type="text" className="form-control mb-3" id="pregunta1" placeholder="Escriba su respuesta aquí" />
                    </div>
                </div>
                <div class="alert alert-success" style={{ display: 'none' }} role="alert" id="p1c">
                    ✔ Respuesta correcta
                </div>
                <div class="alert alert-danger" style={{ display: 'none' }} role="alert" id="p1i">
                    X Respuesta incorrecta
                </div>


                <div class="card text-bg-secondary text-center mb-4">
                    <div class="card-header">
                        Pregunta 3
                    </div>
                    <div class="card-body">
                        <h5 class="card-title">Seleccione la respuesta correcta</h5>
                        <p class="card-text">De los siguientes conjuntos, indique el erroneo.</p>
                        <div class="form-check" style={{ display: 'none' }}>
                            <input class="form-check-input" type="radio" name="flexRadioDefault1" id="flexRadioDefault0" value="0" checked />
                            <label class="form-check-label" for="flexRadioDefault0">
                                0
                            </label>
                        </div>
                        <div class="form-check">
                            <input class="form-check-input" type="radio" name="flexRadioDefault1" id="flexRadioDefault1" value={this.state.p2[0]} />
                            <label class="form-check-label" for="flexRadioDefault1">
                                {this.state.p2[0]}
                            </label>
                        </div>
                        <div class="form-check">
                            <input class="form-check-input" type="radio" name="flexRadioDefault1" id="flexRadioDefault2" value={this.state.p2[1]} />
                            <label class="form-check-label" for="flexRadioDefault2">
                                {this.state.p2[1]}
                            </label>
                        </div>
                        <div class="form-check">
                            <input class="form-check-input" type="radio" name="flexRadioDefault1" id="flexRadioDefault3" value={this.state.p2[2]} />
                            <label class="form-check-label" for="flexRadioDefault3">
                                {this.state.p2[2]}
                            </label>
                        </div>
                    </div>
                </div>
                <div class="alert alert-success" style={{ display: 'none' }} role="alert" id="p2c">
                    ✔ Respuesta correcta
                </div>
                <div class="alert alert-danger" style={{ display: 'none' }} role="alert" id="p2i">
                    X Respuesta incorrecta
                </div>

                <div class="card text-bg-secondary text-center mb-4">
                    <div class="card-header">
                        Pregunta 4
                    </div>
                    <div class="card-body">
                        <h5 class="card-title">Indique la respuesta correcta</h5>
                        <p class="card-text">Escriba un conjunto con cardinalidad {this.state.preguntas.p3}. Tome en cuenta la notación de conjuntos.</p>
                        <input type="text" className="form-control mb-3" id="pregunta3" placeholder="Escriba su respuesta aquí" />
                    </div>
                </div>
                <div class="alert alert-success" style={{ display: 'none' }} role="alert" id="p3c">
                    ✔ Respuesta correcta
                </div>
                <div class="alert alert-danger" style={{ display: 'none' }} role="alert" id="p3i">
                    X Respuesta incorrecta
                </div>

                <div class="card text-bg-secondary text-center mb-4">
                    <div class="card-header">
                        Pregunta 5
                    </div>
                    <div class="card-body">
                        <h5 class="card-title">Seleccione la respuesta correcta</h5>
                        <p class="card-text">De los siguientes conjuntos, indique cuál tiene una notación correcta.</p>
                        <div class="form-check" style={{ display: 'none' }}>
                            <input class="form-check-input" type="radio" name="flexRadioDefault2" id="flexRadioDefault00" value="0" checked />
                            <label class="form-check-label" for="flexRadioDefault00">
                                0
                            </label>
                        </div>
                        <div class="form-check">
                            <input class="form-check-input" type="radio" name="flexRadioDefault2" id="flexRadioDefault5" value={this.state.p4[0]} />
                            <label class="form-check-label" for="flexRadioDefault5">
                                {this.state.p4[0]}
                            </label>
                        </div>
                        <div class="form-check">
                            <input class="form-check-input" type="radio" name="flexRadioDefault2" id="flexRadioDefault6" value={this.state.p4[1]} />
                            <label class="form-check-label" for="flexRadioDefault6">
                                {this.state.p4[1]}
                            </label>
                        </div>
                        <div class="form-check">
                            <input class="form-check-input" type="radio" name="flexRadioDefault2" id="flexRadioDefault7" value={this.state.p4[2]} />
                            <label class="form-check-label" for="flexRadioDefault7">
                                {this.state.p4[2]}
                            </label>
                        </div>
                    </div>
                </div>
                <div class="alert alert-success" style={{ display: 'none' }} role="alert" id="p4c">
                    ✔ Respuesta correcta
                </div>
                <div class="alert alert-danger" style={{ display: 'none' }} role="alert" id="p4i">
                    X Respuesta incorrecta
                </div>

                <div class="card text-bg-secondary text-center mb-4">
                    <div class="card-header">
                        Pregunta 6
                    </div>
                    <div class="card-body">
                        <h5 class="card-title">Indique la respuesta correcta</h5>
                        <p class="card-text">Escriba un conjunto con cardinalidad {this.state.preguntas.p5}. Tome en cuenta la notación de conjuntos.</p>
                        <input type="text" className="form-control mb-3" id="pregunta5" placeholder="Escriba su respuesta aquí" />
                    </div>
                </div>
                <div class="alert alert-success" style={{ display: 'none' }} role="alert" id="p5c">
                    ✔ Respuesta correcta
                </div>
                <div class="alert alert-danger" style={{ display: 'none' }} role="alert" id="p5i">
                    X Respuesta incorrecta
                </div>

                <button className="btn btn-primary btn-submit text-bold mb-3 rounded-3" style={{ width: 100 + '%', display: 'block' }} id="enviar" onClick={this.get_data}>Enviar respuestas</button>

                <div class="alert alert-primary mt-5" style={{ display: 'none' }} role="alert" id="resumen">
                    <h4 class="alert-heading">Resumen del Quiz!</h4>
                    <hr />
                    <p class="mb-0">Aciertos: {this.state.aciertos}</p>
                    <p class="mb-2">Calificación final: {this.state.calif}</p>

                    <button type="button" class="btn btn-danger" id='reinicio' style={{ display: 'none' }} onClick={() => window.location.reload()}>Cargar otro Quiz</button>
                </div>

            </div>
        )
    }
}

export default Notacion_Quiz;