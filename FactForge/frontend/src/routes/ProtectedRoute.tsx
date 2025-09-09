import React from "react";
import { Navigate, Outlet } from "react-router-dom";

export default function ProtectedRoute({ isAuthed }: { isAuthed: boolean }) {
  return isAuthed ? <Outlet /> : <Navigate to="/login" replace />;
}
