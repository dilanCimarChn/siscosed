import React, { useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import './normal.css';

function NormalDashboard() {
  const navigate = useNavigate();

  useEffect(() => {
    const role = localStorage.getItem('role'); // Obtén el rol del usuario desde localStorage

    if (role !== 'normal') {
      // Si el rol no es 'normal', redirige al login
      navigate('/login');
    }
  }, [navigate]);

  return (
    <div>
      <h1>Bienvenido al Dashboard de Usuario Normal</h1>
      {/* Aquí va el contenido específico del dashboard normal */}
    </div>
  );
}

export default NormalDashboard;
