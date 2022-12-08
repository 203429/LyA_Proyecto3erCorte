import React, { useEffect, useState } from 'react'
import { axiosInstance } from '../../../helpers/axios';
import './../../global/assets/css/styles.css';

const Operaciones = () => {
    // const [resp, setResp] = useState("");
    const [cinta1, setCinta1] = useState('')
    const [cinta2, setCinta2] = useState('')
    const [operador, setOperador] = useState('0')

    // useEffect(() => {
    //     handleRequest();
    // }, []);

    useEffect(()=>{
        if (cinta1 === "" || cinta2 === "" || operador === "0" || operador === null){
            console.log("Boton desactivado")
            document.getElementById("btn-calcular").disabled = true
        }else{
            console.log("Boton activado")
            document.getElementById("btn-calcular").disabled = false
        }
    },[cinta1,cinta2,operador]);

    // const handleRequest = async () => {
    //     await axiosInstance.get('operaciones')
    //         .then(resp => setResp(resp.data))
    //         .catch(err => console.log('error: ', err))
    // };

    const validarOperacion = (e) => {
        if (e.target.value != "0"){
            setOperador(e.target.value)
            document.getElementById("msg-opr").textContent = ""
        }else{
            setOperador(null)
            document.getElementById("msg-opr").textContent = "Selecciona una operación válida"
        }
    }

    let expReg = /\s*{\s*([a-zA-Z0-9]((\s*,\s*[a-zA-Z0-9])*))?\s*}\s*/;
    const validarCinta = (e) => {
        if (e.target.value != null && e.target.value != "" && expReg.test(e.target.value)){
            e.target.id === "cinta1" ? setCinta1(e.target.value) : setCinta2(e.target.value)
            document.getElementById("msg-"+e.target.id).textContent = ""
        }else{
            if(expReg.test(e.target.value) === false && e.target.value != null && e.target.value != ""){
                document.getElementById("msg-"+e.target.id).textContent = "No cumple con una notación válida"
            }else{
                document.getElementById("msg-"+e.target.id).textContent = "Este campo es requerido"
            }
        }
        console.log(expReg.test(e.target.value))
    }

    return (
        <div className='container m-5'>
            <form>
                <div className='container mb-3'>
                    <div className='row'>
                        <div className="mb-3">
                            {operador === "5" ? <label className="form-label text-bold">Universo</label> : <label className="form-label text-bold">Conjunto A</label>}
                            <input type="text" className="form-control rounded-3 text-regular" id="cinta1" onChange={(e) => validarCinta(e)} onBlur={(e) => validarCinta(e)}/>
                            <p className='text-m-22 txt-error' id="msg-cinta1"></p>
                        </div>
                    </div>
                    <div className='row'>
                        <div className="mb-3">
                            {operador === "5" ? <label className="form-label text-bold">Conjunto A</label> : <label className="form-label text-bold">Conjunto B</label>}
                            <input type="text" className="form-control rounded-3 text-regular" id="cinta2" onChange={(e) => validarCinta(e)} onBlur={(e) => validarCinta(e)}/>
                            <p className='text-m-22 txt-error' id="msg-cinta2"></p>
                        </div>
                    </div>
                    <div className='row mb-3 align-items-end'>
                        <div className='col'>
                            <label className="form-label text-bold">Operación</label>
                            <select className="form-select form-select-md text-regular rounded-3" onChange={(e) => validarOperacion(e)} onBlur={(e) => validarOperacion(e)}>
                                <option value="0" selected>Selecciona una operación</option>
                                <option value="1">Unión</option>
                                <option value="2">Intersección</option>
                                <option value="3">Diferencia relativa</option>
                                <option value="4">Diferencia simétrica</option>
                                <option value="5">Complemento</option>
                            </select>
                            <p className='text-m-22 txt-error' id="msg-opr"></p>
                        </div>
                        <div className='col div-center'>
                            <button className="btn btn-primary btn-submit text-bold mb-3 rounded-3" id="btn-calcular">Calcular</button>
                        </div>
                    </div>
                </div>
            </form>
            {/* <div className='container mt-5'>
                <p className='text-bold' id='result'>Resultado:</p>
            </div> */}
        </div>
    )
}

export default Operaciones