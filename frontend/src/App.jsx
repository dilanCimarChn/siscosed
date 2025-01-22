import React from 'react';
import { BrowserRouter as Router, Routes, Route, Navigate } from 'react-router-dom';
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

function App() {
  const userRole = localStorage.getItem('role');

  const ProtectedRoute = ({ children, allowedRoles }) => {
    if (!userRole) {
      return <Navigate to="/login" />;
    }

    if (!allowedRoles.includes(userRole)) {
      return <Navigate to="/" />;
    }

    return children;
  };

  return (
    <Router>
      <Routes>
        <Route path="/" element={<BienvenidoLogin />} />
        <Route path="/login" element={<VLogin />} />

        {/* Protege las rutas basadas en el rol */}
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
        
        {/* Rutas de las vistas */}
        <Route path="/nuevo/hoja-de-ruta" element={<HojaDeRuta />} />
        <Route path="/nuevo/documento" element={<Documento />} />
        <Route path="/recepcion" element={<Recepcion />} />
        <Route path="/pendientes" element={<Pendientes />} />
        <Route path="/enviados-pendientes" element={<EnviadosPendientes />} />
        <Route path="/archivados" element={<Archivados />} />
        <Route path="/proveidos" element={<Proveidos />} />
        <Route path="/bandeja-remitidos" element={<BandejaRemitidos />} />
      </Routes>
    </Router>
  );
}

export default App;
