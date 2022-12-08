import React from 'react';
import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import NavBar from '../components/global/NavBar';
import Index from '../components/modules/conjunto_potencia/Index';
import Operaciones from '../components/modules/operaciones/operaciones';
import Notacion from '../components/modules/notacion/Notacion';
import NotacionQuiz from '../components/modules/notacion/Notacion_Quiz';
import NotacionValidar from '../components/modules/notacion/Notacion_Validar';

const AppRouter = () => {
    
    return (
        <>

            <div className='container-xxl pt-1'>
                <Router>
                <div className='row mb-5 pb-3'>
                        <NavBar />
                    </div>
                    <Routes>
                        {/* Agregar sus rutas aquí */}
                        <Route path='/potencia' element={<Index />} />
                        <Route path='/operaciones' element={<Operaciones />} />
                        <Route path='/notacion' element={<Notacion />} />
                        <Route path='/notacion/quiz' element={<NotacionQuiz />} />
                        <Route path='/notacion/validar' element={<NotacionValidar />} />
                    </Routes>
                </Router>
            </div>
        </>
    )
}

export default AppRouter
