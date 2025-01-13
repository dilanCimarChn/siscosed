import React from 'react';
import './bienvenido-login.css';

function BienvenidoLogin() {
  return (
    <div className="login-background">
      <div className="login-container">
        <div className="logo-container">
          <h1 className="logo-text">SISCOSED</h1>
        </div>
        <button className="login-button">Inicia Sesión</button>
      </div>
    </div>
  );
}

export default BienvenidoLogin;
