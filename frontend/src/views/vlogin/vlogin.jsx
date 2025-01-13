import React from 'react';
import './vlogin.css';

function VLogin() {
  return (
    <div className="login-background">
      <div className="login-container">
        <div className="login-form">
          <label>Email</label>
          <input type="email" placeholder="Email" />
          <label>Password</label>
          <input type="password" placeholder="Contraseña" />
          <button className="login-button">Ingresar</button>
        </div>
      </div>
    </div>
  );
}

export default VLogin;
