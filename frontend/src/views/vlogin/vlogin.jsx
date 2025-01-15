import React, { useState } from 'react';
import './vlogin.css';

function VLogin() {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [error, setError] = useState('');
  const [showPassword, setShowPassword] = useState(false); // Estado para mostrar o esconder la contraseña

  const handleLogin = async () => {
    try {
      const response = await fetch('http://127.0.0.1:8000/api/login/', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ email, password }),
      });
      const data = await response.json();
      if (data.success) {
        alert(`Login exitoso. Rol: ${data.role}`);
        // Redirige según el rol
        if (data.role === 'normal') {
          window.location.href = '/users/normal/';
        } else if (data.role === 'admin') {
          window.location.href = '/users/admin/';
        } else if (data.role === 'superadmin') {
          window.location.href = '/users/superadmin/';
        }
      } else {
        setError(data.error);
      }
    } catch (error) {
      setError('Error en la conexión.');
    }
  };

  return (
    <div className="login-background">
      <div className="login-container">
        <label>Email</label>
        <input
          type="email"
          placeholder="Email"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
        />
        <label>Password</label>
        <input
          type={showPassword ? 'text' : 'password'} // Cambia el tipo entre "password" y "text"
          placeholder="Contraseña"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
        />
        <div className="show-password">
          <input
            type="checkbox"
            id="showPassword"
            checked={showPassword}
            onChange={(e) => setShowPassword(e.target.checked)}
          />
          <label htmlFor="showPassword">Mostrar contraseña</label>
        </div>
        <button className="login-button" onClick={handleLogin}>
          Ingresar
        </button>
        {error && <p style={{ color: 'red' }}>{error}</p>}
      </div>
    </div>
  );
}

export default VLogin;
