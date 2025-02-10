import React, { useState } from 'react';  
import './vlogin.css';

function VLogin() {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [error, setError] = useState('');
  const [showPassword, setShowPassword] = useState(false);

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
        
        // Guarda el rol del usuario en el localStorage
        localStorage.setItem('role', data.role);

        // Redirige al dashboard correspondiente según el rol
        switch(data.role) {
          case 'normal':
            window.location.href = '/users/normal/';
            break;
          case 'admin':
            window.location.href = '/users/admin/';
            break;
          case 'superadmin':
            window.location.href = '/users/superadmin/';
            break;
          default:
            setError('Rol no reconocido');
            break;
        }
      } else {
        setError(data.error || 'Error desconocido');
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
          type={showPassword ? 'text' : 'password'}
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
