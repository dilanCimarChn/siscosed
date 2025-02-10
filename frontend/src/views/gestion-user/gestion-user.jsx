import React, { useState, useEffect } from 'react';
import axios from 'axios';
import './gestion-user.css';

function GestionUser() {
  const [usuarios, setUsuarios] = useState([]);
  const [error, setError] = useState('');
  const [formData, setFormData] = useState({
    email: '',
    password: '',
    role: 'normal',
  });
  const [loading, setLoading] = useState(false);

  // Obtener usuarios al cargar el componente
  useEffect(() => {
    axios.get('http://127.0.0.1:8000/api/usuarios/')
      .then(response => {
        setUsuarios(response.data);
      })
      .catch(error => {
        console.error('Error al obtener usuarios:', error);
        setError('Error al obtener usuarios. Asegúrate de estar autenticado.');
      });
  }, []);

  // Manejar el cambio de valores en el formulario
  const handleInputChange = (e) => {
    const { name, value } = e.target;
    setFormData({ ...formData, [name]: value });
  };

  // Crear usuario
  const handleSubmit = (e) => {
    e.preventDefault();
    setLoading(true);

    axios.post('http://127.0.0.1:8000/api/usuarios/', formData)
      .then(response => {
        setUsuarios([...usuarios, response.data]);
        setFormData({ email: '', password: '', role: 'normal' });
        alert('Usuario creado exitosamente');
      })
      .catch(error => {
        console.error('Error al crear el usuario:', error);
        alert('Hubo un error al crear el usuario.');
      })
      .finally(() => {
        setLoading(false);
      });
  };

  // Cambiar estado del usuario
  const toggleUserStatus = (userId, currentStatus) => {
    axios.put(`http://127.0.0.1:8000/api/usuarios/${userId}/toggle_status/`)
      .then(response => {
        setUsuarios(usuarios.map(user =>
          user.id === userId ? { ...user, estado: currentStatus ? 0 : 1 } : user
        ));
      })
      .catch(error => {
        console.error('Error al actualizar el estado:', error);
        alert('Error al actualizar el estado');
      });
  };

  // Eliminar usuario
  const deleteUser = (userId) => {
    axios.delete(`http://127.0.0.1:8000/api/usuarios/${userId}/`)
      .then(response => {
        setUsuarios(usuarios.filter(user => user.id !== userId));
        alert('Usuario eliminado correctamente');
      })
      .catch(error => {
        console.error('Error al eliminar usuario:', error);
        alert('Error al eliminar el usuario');
      });
  };

  // Cambiar contraseña del usuario
  const changePassword = (userId) => {
    const newPassword = prompt('Ingrese la nueva contraseña:');
    if (newPassword) {
      axios.put(`http://127.0.0.1:8000/api/usuarios/${userId}/change_password/`, { password: newPassword })
        .then(response => {
          setUsuarios(usuarios.map(user =>
            user.id === userId ? { ...user, password: newPassword } : user
          ));
          alert('Contraseña actualizada exitosamente');
        })
        .catch(error => {
          console.error('Error al cambiar la contraseña:', error);
          alert('Error al cambiar la contraseña');
        });
    }
  };

  return (
    <div className="gestion-user">
      <h1>Gestión de Usuarios</h1>
      {error && <p style={{ color: 'red' }}>{error}</p>}
      <form onSubmit={handleSubmit} className="form-crear-usuario">
        <input
          type="email"
          name="email"
          placeholder="Correo electrónico"
          value={formData.email}
          onChange={handleInputChange}
          required
        />
        <input
          type="password"
          name="password"
          placeholder="Contraseña"
          value={formData.password}
          onChange={handleInputChange}
          required
        />
        <select
          name="role"
          value={formData.role}
          onChange={handleInputChange}
        >
          <option value="normal">Normal</option>
          <option value="admin">Admin</option>
          <option value="superadmin">SuperAdmin</option>
        </select>
        <button type="submit" disabled={loading}>
          {loading ? 'Creando...' : 'Crear Usuario'}
        </button>
      </form>

      <h2>Usuarios Registrados</h2>
      <ul className="lista-usuarios">
        {usuarios.map((usuario) => (
          <li key={usuario.id} className="card-usuario">
            <p>Email: {usuario.email}</p>
            <p>Rol: {usuario.rol}</p>
            <p>Contraseña: {usuario.password}</p>
            <p>Estado: {usuario.estado === 1 ? 'Activo' : 'Inactivo'}</p>
            <button
              className={usuario.estado === 1 ? 'btn-desactivar' : 'btn-activar'}
              onClick={() => toggleUserStatus(usuario.id, usuario.estado === 1)}
            >
              {usuario.estado === 1 ? 'Deshabilitar' : 'Habilitar'}
            </button>
            <button
              className="btn-eliminar"
              onClick={() => deleteUser(usuario.id)}
            >
              Eliminar
            </button>
            <button
              className="btn-cambiar-contrasena"
              onClick={() => changePassword(usuario.id)}
            >
              Cambiar Contraseña
            </button>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default GestionUser;
