import React, { useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import BarraNav from '../../components/barra-nav/barra-nav'; // Barra de navegación
import './admin.css';

function AdminDashboard() {
  const navigate = useNavigate();

  useEffect(() => {
    const role = localStorage.getItem('role');
    if (role !== 'admin') {
      navigate('/login');
    }
  }, [navigate]);

  return (
    <div className="dashboard-container">
      <h1>Bienvenido al Dashboard de Administrador</h1>
      {/* Aquí va el contenido específico del dashboard admin */}
    </div>
  );
}

export default AdminDashboard;
