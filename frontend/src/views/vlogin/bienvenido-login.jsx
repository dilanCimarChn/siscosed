import React from 'react';
import './bienvenido-login.css';
import { useNavigate } from 'react-router-dom';

function BienvenidoLogin() {
  const navigate = useNavigate(); // Hook para la navegación

  const handleLoginClick = () => {
    navigate('/login'); // Redirige a la página de login
  };

  return (
    <div className="login-background">
      <div className="login-container">
        <div className="logo-container">
          <h1 className="logo-text">SISCOSED</h1>
        </div>
        <button className="login-button" onClick={handleLoginClick}>
          Inicia Sesión
        </button>
      </div>
    </div>
  );
}

export default BienvenidoLogin;
