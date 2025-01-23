import React, { useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import BarraNav from '../../components/barra-nav/barra-nav'; // Barra de navegación
import './normal.css';

function NormalDashboard() {
  const navigate = useNavigate();

  useEffect(() => {
    const role = localStorage.getItem('role');
    if (role !== 'normal') {
      navigate('/login');
    }
  }, [navigate]);

  return (
    <div className="dashboard-container">
      <h1>Bienvenido al Dashboard de Usuario Normal</h1>
      {/* Aquí va el contenido específico del dashboard normal */}
    </div>
  );
}

export default NormalDashboard;
