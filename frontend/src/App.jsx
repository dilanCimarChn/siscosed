import React, { useState, useEffect } from 'react';
import { BrowserRouter as Router, Routes, Route, Navigate } from 'react-router-dom';
import BarraNav from './components/barra-nav/barra-nav'; // Barra de navegación
import BienvenidoLogin from './views/vlogin/bienvenido-login';
import VLogin from './views/vlogin/vlogin';
import NormalDashboard from './users/normal/NormalDashboard';
import AdminDashboard from './users/admin/AdminDashboard';
import SuperAdminDashboard from './users/superadmin/SuperAdminDashboard';
import HojaDeRuta from './views/hoja-de-ruta/HojaDeRuta';
import Documento from './views/documento/Documento';
import Pendientes from './views/pendientes/Pendientes';
import EnviadosPendientes from './views/enviados-pendientes/EnviadosPendientes';
import Archivados from './views/archivados/Archivados';
import Proveidos from './views/proveidos/Proveidos';
import BandejaRemitidos from './views/bandeja-remitidos/BandejaRemitidos';
import Recepcion from './views/recepcion/Recepcion';
import GestionUser from './views/gestion-user/gestion-user';

function App() {
  const [userRole, setUserRole] = useState(localStorage.getItem('role'));  // Verifica si el usuario está logueado

  useEffect(() => {
    setUserRole(localStorage.getItem('role'));
  }, []);

  const ProtectedRoute = ({ children, allowedRoles }) => {
    if (!userRole) {
      return <Navigate to="/login" />;
    }

    if (!allowedRoles.includes(userRole)) {
      return <Navigate to="/" />;
    }

    return children;
  };

  const handleLogout = () => {
    localStorage.removeItem('role'); // Elimina el rol del localStorage
    setUserRole(null);  // Actualiza el estado para reflejar que el usuario ha hecho logout
    window.location.href = '/'; // Redirige a bienvenido
  };

  return (
    <Router>
      <div className="app-container">
        {/* Solo muestra la barra de navegación si el usuario tiene un rol (está logueado) */}
        {userRole && (
          <div className="navbar-container">
            <BarraNav onLogout={handleLogout} /> {/* Barra de navegación */}
          </div>
        )}

        {/* Contenedor para las vistas de login y bienvenida */}
        <div className={userRole ? "views-container" : "full-screen-container"}>
          <Routes>
            <Route path="/" element={<BienvenidoLogin />} />
            <Route path="/login" element={<VLogin />} />

            {/* Rutas protegidas por rol */}
            <Route
              path="/users/normal/"
              element={
                <ProtectedRoute allowedRoles={['normal']}>
                  <NormalDashboard />
                </ProtectedRoute>
              }
            />
            <Route
              path="/users/admin/"
              element={
                <ProtectedRoute allowedRoles={['admin']}>
                  <AdminDashboard />
                </ProtectedRoute>
              }
            />
            <Route
              path="/users/superadmin/"
              element={
                <ProtectedRoute allowedRoles={['superadmin']}>
                  <SuperAdminDashboard />
                </ProtectedRoute>
              }
            />

            {/* Rutas de vistas */}
            <Route path="/nuevo/hoja-de-ruta" element={<HojaDeRuta />} />
            <Route path="/nuevo/documento" element={<Documento />} />
            <Route path="/recepcion" element={<Recepcion />} />
            <Route path="/pendientes" element={<Pendientes />} />
            <Route path="/enviados-pendientes" element={<EnviadosPendientes />} />
            <Route path="/archivados" element={<Archivados />} />
            <Route path="/proveidos" element={<Proveidos />} />
            <Route path="/bandeja-remitidos" element={<BandejaRemitidos />} />

            {/* Ruta de Gestión de Usuarios, solo accesible por superadmin */}
            <Route
              path="/gestion-usuarios"
              element={
                <ProtectedRoute allowedRoles={['superadmin']}>
                  <GestionUser />
                </ProtectedRoute>
              }
            />
          </Routes>
        </div>
      </div>
    </Router>
  );
}

export default App;
