import React, { useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import BarraNav from '../../components/barra-nav/barra-nav'; // Importar el Navbar
import './superadmin.css';

function SuperAdminDashboard() {
  const navigate = useNavigate();

  useEffect(() => {
    const role = localStorage.getItem('role'); // Obtén el rol del usuario desde localStorage

    if (role !== 'superadmin') {
      // Si el rol no es 'superadmin', redirige al login
      navigate('/login');
    }
  }, [navigate]);

  return (
    <div>
      <BarraNav /> {/* Incluir el Navbar */}
      <h1>Bienvenido al Dashboard de Superadministrador</h1>
      {/* Aquí va el contenido específico del dashboard superadmin */}
    </div>
  );
}

export default SuperAdminDashboard;
