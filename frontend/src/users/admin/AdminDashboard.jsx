import React, { useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import BarraNav from '../../components/barra-nav/barra-nav'; // Importar el Navbar
import './admin.css';

function AdminDashboard() {
  const navigate = useNavigate();

  useEffect(() => {
    const role = localStorage.getItem('role'); // Obtén el rol del usuario desde localStorage

    if (role !== 'admin') {
      // Si el rol no es 'admin', redirige al login
      navigate('/login');
    }
  }, [navigate]);

  return (
    <div>
      <BarraNav /> {/* Incluir el Navbar */}
      <h1>Bienvenido al Dashboard de Administrador</h1>
      {/* Aquí va el contenido específico del dashboard admin */}
    </div>
  );
}

export default AdminDashboard;
