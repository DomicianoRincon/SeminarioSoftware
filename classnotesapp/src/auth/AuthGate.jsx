// src/auth/AuthGate.jsx
// Switches the whole app on the auth `status`. Sign-in is OPTIONAL in this
// course: the content is public, so a signed-out visitor gets the app as is.
// Only someone who chose to sign in is walked through the terms and profile
// screens before coming back. When Firebase isn't configured, status is
// 'ready' from the start → ungated.

import React from 'react';
import Box from '@mui/material/Box';
import CircularProgress from '@mui/material/CircularProgress';
import { useThemeMode } from '@/theme/ThemeContext';
import { useAuth } from './AuthContext';
import TermsScreen from './TermsScreen';
import ProfileForm from './ProfileForm';

const AuthGate = ({ children }) => {
  const { status } = useAuth();
  const { theme } = useThemeMode();

  if (status === 'loading') {
    return (
      <Box sx={{ minHeight: '100vh', display: 'flex', alignItems: 'center', justifyContent: 'center', background: theme.background }}>
        <CircularProgress sx={{ color: theme.accent }} />
      </Box>
    );
  }
  if (status === 'signed-out') return children;
  // Los términos van antes del perfil: primero se acepta, después se dan datos.
  if (status === 'need-terms') return <TermsScreen />;
  if (status === 'need-profile') return <ProfileForm />;
  return children;
};

export default AuthGate;
