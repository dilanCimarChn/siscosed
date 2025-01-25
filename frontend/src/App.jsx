import React, { useState, useEffect } from 'react';
import { Routes, Route, Navigate, useLocation } from 'react-router-dom';
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
  const [userRole, setUserRole] = useState(localStorage.getItem('role'));
  const location = useLocation(); // Para detectar la URL actual

  useEffect(() => {
    setUserRole(localStorage.getItem('role'));
  }, [location.pathname]); // Detectar cambios en la ruta

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
    localStorage.removeItem('role');
    setUserRole(null);
    window.location.href = '/';
  };

  // Determina si se debe mostrar la barra de navegación
  const showNav = userRole && location.pathname !== "/" && location.pathname !== "/login";

  return (
    <div className="app-container">
      {/* Barra de navegación solo se muestra cuando el usuario está logueado y no está en las páginas de bienvenida ni login */}
      {showNav && (
        <div className="navbar-container">
          <BarraNav onLogout={handleLogout} />
        </div>
      )}

      <div className={showNav ? "views-container" : "full-screen-container"}>
        <Routes>
          <Route path="/" element={<BienvenidoLogin />} />
          <Route path="/login" element={<VLogin />} />
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
          {/* Otras rutas */}
          <Route path="/nuevo/hoja-de-ruta" element={<HojaDeRuta />} />
          <Route path="/nuevo/documento" element={<Documento />} />
          <Route path="/recepcion" element={<Recepcion />} />
          <Route path="/pendientes" element={<Pendientes />} />
          <Route path="/enviados-pendientes" element={<EnviadosPendientes />} />
          <Route path="/archivados" element={<Archivados />} />
          <Route path="/proveidos" element={<Proveidos />} />
          <Route path="/bandeja-remitidos" element={<BandejaRemitidos />} />
          <Route
            path="/gestion-usuarios"
            element={
              <ProtectedRoute allowedRoles={['superadmin']}>
                <GestionUser />
              </ProtectedRoute>
            }
          />
          <Route path="*" element={<Navigate to="/" />} />
        </Routes>
      </div>
    </div>
  );
}

export default App;
