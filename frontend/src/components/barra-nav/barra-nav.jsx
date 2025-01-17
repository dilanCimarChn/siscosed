import React, { useState } from 'react';
import { Link } from 'react-router-dom';
import './barra-nav.css';

function BarraNav() {
  const [isOpen, setIsOpen] = useState(false);

  const toggleMenu = () => setIsOpen(!isOpen);

  return (
    <div className="navbar">
      <button className="menu-toggle" onClick={toggleMenu}>
        {isOpen ? 'Cerrar' : 'Abrir'} Menú
      </button>
      <nav className={`nav-menu ${isOpen ? 'open' : ''}`}>
        <ul>
          <li>
            <Link to="/nuevo/hoja-de-ruta">Hoja de Ruta</Link>
          </li>
          <li>
            <Link to="/nuevo/documento">Documento</Link>
          </li>
          <li>
            <div className="dropdown">
              <button className="dropbtn">Bandeja de Proveídos</button>
              <div className="dropdown-content">
                <Link to="/recepcion">Recepción</Link>
                <Link to="/pendientes">Pendientes</Link>
                <Link to="/enviados-pendientes">Enviados Pendientes de Recepción</Link>
                <Link to="/archivados">Archivados</Link>
                <Link to="/proveidos">Proveídos</Link>
              </div>
            </div>
          </li>
          <li>
            <Link to="/bandeja-remitidos">Bandeja de Remitidos</Link>
          </li>
        </ul>
      </nav>
    </div>
  );
}

export default BarraNav;
