import React, { useState, useEffect } from 'react';
import { Link, useNavigate } from 'react-router-dom';
import './barra-nav.css';

function BarraNav({ onLogout }) {
  const [isOpenNew, setIsOpenNew] = useState(false);
  const [isOpenBandeja, setIsOpenBandeja] = useState(false);
  const [role, setRole] = useState('');
  const navigate = useNavigate();

  useEffect(() => {
    // Obtiene el rol del usuario desde el localStorage
    const userRole = localStorage.getItem('role');
    setRole(userRole);
  }, []);

  // Función para alternar el estado del menú "Nuevo"
  const toggleMenuNew = () => setIsOpenNew(!isOpenNew);

  // Función para alternar el estado del menú "Bandeja de Proveídos"
  const toggleMenuBandeja = () => setIsOpenBandeja(!isOpenBandeja);

  return (
    <div className="navbar">
      <button className="menu-toggle" onClick={() => setIsOpenNew(!isOpenNew)}>
        {isOpenNew ? 'Cerrar' : 'Abrir'} Menú
      </button>
      <nav className={`nav-menu ${isOpenNew ? 'open' : ''}`}>
        <ul>
          <li className="dropdown">
            <button className="dropbtn" onClick={toggleMenuNew}>Nuevo</button>
            {isOpenNew && (
              <div className="dropdown-content">
                <Link to="/nuevo/hoja-de-ruta">Hoja de Ruta</Link>
                <Link to="/nuevo/documento">Documento</Link>
              </div>
            )}
          </li>
          <li className="dropdown">
            <button className="dropbtn" onClick={toggleMenuBandeja}>Bandeja de Proveídos</button>
            {isOpenBandeja && (
              <div className="dropdown-content">
                <Link to="/recepcion">Recepción</Link>
                <Link to="/pendientes">Pendientes</Link>
                <Link to="/enviados-pendientes">Enviados Pendientes</Link>
                <Link to="/archivados">Archivados</Link>
                <Link to="/proveidos">Proveídos</Link>
              </div>
            )}
          </li>
          {role === 'admin' || role === 'superadmin' ? (
            <li>
              <Link to="/bandeja-remitidos">Bandeja de Remitidos</Link>
            </li>
          ) : null}
          {role === 'superadmin' && (
            <li>
              <Link to="/gestion-usuarios">Gestión de Usuarios</Link>
            </li>
          )}
        </ul>
      </nav>

      <div className="logout-container">
        <button className="logout-btn" onClick={onLogout}>Cerrar sesión</button>
      </div>
    </div>
  );
}

export default BarraNav;
