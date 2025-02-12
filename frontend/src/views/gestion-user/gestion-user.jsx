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
    nombres: '',
    apellidoPaterno: '',
    apellidoMaterno: '',
    grado: '',
    fuerza: '',
    regimiento: '',
    carnetMilitar: '',
    fotoPerfil: '',
    ci: '',
    expedido: 'La Paz',
    fechaNacimiento: '',
    sexo: 'Masculino',
    estadoCivil: '',
    telefono: '',
    celular: '',
    domicilio: '',
    tipoLicencia: '',
    codigoSeguro: '',
    codigoBiometrico: '',
    id_cargo: '',
    id_dependencia_cargo: '',
    id_area: '',
    cfgConductoRegular: '',
    cfgNuevoInforme: '',
    cfgAccesoRutas: 0,
  });
  const [loading, setLoading] = useState(false);
  const [showPassword, setShowPassword] = useState(false);
  const [editUser, setEditUser] = useState(null);

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

  // Crear o editar usuario
  const handleSubmit = (e) => {
    e.preventDefault();
    setLoading(true);

    if (editUser) {
      // Editar usuario
      axios.put(`http://127.0.0.1:8000/api/usuarios/${editUser.id}/update_user/`, formData)
        .then(response => {
          const updatedUsers = usuarios.map(user =>
            user.id === editUser.id ? response.data : user
          );
          setUsuarios(updatedUsers);
          alert('Usuario actualizado exitosamente');
          setEditUser(null);
        })
        .catch(error => {
          console.error('Error al editar el usuario:', error);
          alert('Hubo un error al editar el usuario.');
        });
    } else {
      // Crear usuario
      axios.post('http://127.0.0.1:8000/api/usuarios/', formData)
        .then(response => {
          setUsuarios([...usuarios, response.data]);
          alert('Usuario creado exitosamente');
        })
        .catch(error => {
          console.error('Error al crear el usuario:', error);
          alert('Hubo un error al crear el usuario.');
        });
    }
    setLoading(false);
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

  // Editar un usuario
  const handleEditUser = (user) => {
    setFormData({ ...user });
    setEditUser(user);
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
        <div className="password-container">
          <input
            type={showPassword ? 'text' : 'password'}
            name="password"
            placeholder="Contraseña"
            value={formData.password}
            onChange={handleInputChange}
            required
          />
          <span onClick={() => setShowPassword(!showPassword)} className="password-icon">
            {showPassword ? (
              <i className="material-icons">visibility_off</i>
            ) : (
              <i className="material-icons">visibility</i>
            )}
          </span>
        </div>

        <input
          type="text"
          name="nombres"
          placeholder="Nombres"
          value={formData.nombres}
          onChange={handleInputChange}
        />
        <input
          type="text"
          name="apellidoPaterno"
          placeholder="Apellido Paterno"
          value={formData.apellidoPaterno}
          onChange={handleInputChange}
        />
        <input
          type="text"
          name="apellidoMaterno"
          placeholder="Apellido Materno"
          value={formData.apellidoMaterno}
          onChange={handleInputChange}
        />
        <input
          type="text"
          name="grado"
          placeholder="Grado"
          value={formData.grado}
          onChange={handleInputChange}
        />
        <input
          type="text"
          name="fuerza"
          placeholder="Fuerza"
          value={formData.fuerza}
          onChange={handleInputChange}
        />
        <input
          type="text"
          name="regimiento"
          placeholder="Regimiento"
          value={formData.regimiento}
          onChange={handleInputChange}
        />
        <input
          type="text"
          name="carnetMilitar"
          placeholder="Carnet Militar"
          value={formData.carnetMilitar}
          onChange={handleInputChange}
        />
        <input
          type="text"
          name="fotoPerfil"
          placeholder="Foto de Perfil"
          value={formData.fotoPerfil}
          onChange={handleInputChange}
        />
        <input
          type="number"
          name="ci"
          placeholder="Carnet de Identidad (CI)"
          value={formData.ci}
          onChange={handleInputChange}
        />
        <select
          name="expedido"
          value={formData.expedido}
          onChange={handleInputChange}
        >
          <option value="La Paz">La Paz</option>
          <option value="Tarija">Tarija</option>
          <option value="Santa Cruz">Santa Cruz</option>
          <option value="Cochabamba">Cochabamba</option>
        </select>
        <input
          type="date"
          name="fechaNacimiento"
          value={formData.fechaNacimiento}
          onChange={handleInputChange}
        />
        <input
          type="text"
          name="sexo"
          value={formData.sexo}
          onChange={handleInputChange}
        />
        <input
          type="text"
          name="estadoCivil"
          value={formData.estadoCivil}
          onChange={handleInputChange}
        />
        <input
          type="text"
          name="telefono"
          value={formData.telefono}
          onChange={handleInputChange}
        />
        <input
          type="text"
          name="celular"
          value={formData.celular}
          onChange={handleInputChange}
        />
        <input
          type="text"
          name="domicilio"
          value={formData.domicilio}
          onChange={handleInputChange}
        />
        <input
          type="text"
          name="tipoLicencia"
          value={formData.tipoLicencia}
          onChange={handleInputChange}
        />
        <input
          type="text"
          name="codigoSeguro"
          value={formData.codigoSeguro}
          onChange={handleInputChange}
        />
        <input
          type="text"
          name="codigoBiometrico"
          value={formData.codigoBiometrico}
          onChange={handleInputChange}
        />
        <input
          type="number"
          name="id_cargo"
          value={formData.id_cargo}
          onChange={handleInputChange}
        />
        <input
          type="number"
          name="id_dependencia_cargo"
          value={formData.id_dependencia_cargo}
          onChange={handleInputChange}
        />
        <input
          type="number"
          name="id_area"
          value={formData.id_area}
          onChange={handleInputChange}
        />
        <input
          type="number"
          name="cfgConductoRegular"
          value={formData.cfgConductoRegular}
          onChange={handleInputChange}
        />
        <input
          type="number"
          name="cfgNuevoInforme"
          value={formData.cfgNuevoInforme}
          onChange={handleInputChange}
        />
        <input
          type="number"
          name="cfgAccesoRutas"
          value={formData.cfgAccesoRutas}
          onChange={handleInputChange}
        />
        <button type="submit" disabled={loading}>
          {loading ? 'Creando...' : editUser ? 'Actualizar Usuario' : 'Crear Usuario'}
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
            <button
              className="btn-editar"
              onClick={() => handleEditUser(usuario)}
            >
              Editar
            </button>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default GestionUser;
