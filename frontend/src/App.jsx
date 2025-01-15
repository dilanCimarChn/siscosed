import React from 'react';
import { BrowserRouter as Router, Routes, Route, Navigate } from 'react-router-dom';
import BienvenidoLogin from './views/vlogin/bienvenido-login';
import VLogin from './views/vlogin/vlogin';
import NormalDashboard from './users/normal/NormalDashboard';
import AdminDashboard from './users/admin/AdminDashboard';
import SuperAdminDashboard from './users/superadmin/SuperAdminDashboard';

function App() {
  // Obtén el rol del usuario desde localStorage
  const userRole = localStorage.getItem('role');

  // Comprobamos si el usuario está autenticado y redirigimos
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
      </Routes>
    </Router>
  );
}

export default App;
