import { useState } from 'react';
import React from 'react';
import BienvenidoLogin from './views/vlogin/bienvenido-login'; // Pantalla de bienvenida
import VLogin from './views/vlogin/vlogin'; // Pantalla de login
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import NormalDashboard from './users/normal/NormalDashboard'; // Dashboard normal
import AdminDashboard from './users/admin/AdminDashboard'; // Dashboard admin
import SuperAdminDashboard from './users/superadmin/SuperAdminDashboard'; // Dashboard superadmin

function App() {
  return (
    <Router>
      <Routes>
        {/* Ruta para la pantalla de bienvenida */}
        <Route path="/" element={<BienvenidoLogin />} />

        {/* Ruta para el login */}
        <Route path="/login" element={<VLogin />} />

        {/* Rutas para los dashboards de los diferentes roles */}
        <Route path="/users/normal" element={<NormalDashboard />} />
        <Route path="/users/admin" element={<AdminDashboard />} />
        <Route path="/users/superadmin" element={<SuperAdminDashboard />} />
      </Routes>
    </Router>
  );
}

export default App;
