import React, { useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import BarraNav from '../../components/barra-nav/barra-nav'; // Barra de navegación
import './superadmin.css';

function SuperAdminDashboard() {
  const navigate = useNavigate();

  useEffect(() => {
    const role = localStorage.getItem('role');
    if (role !== 'superadmin') {
      navigate('/login');
    }
  }, [navigate]);

  return (
    <div className="dashboard-container">
      <h1>Bienvenido al Dashboard de Superadministrador</h1>
      {/* Aquí va el contenido específico del dashboard superadmin */}
    </div>
  );
}

export default SuperAdminDashboard;
