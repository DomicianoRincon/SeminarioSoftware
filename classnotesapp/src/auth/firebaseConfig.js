// src/auth/firebaseConfig.js
//
// Per-course Firebase web-app config. This is PUBLIC information, not a secret:
// the apiKey is just a project identifier. Real security is enforced by
// Firestore security rules + the "Authorized domains" list in the Firebase
// console (Authentication → Settings). So it is safe to commit these values.
//
// Curso: Seminario de Ingeniería de Software — SIN proyecto Firebase todavía.
// Mientras el apiKey sea un REPLACE_*, Firebase no se inicializa y la app es un
// visor público sin botón de inicio de sesión. Al pegar aquí la config de un
// proyecto propio del curso (no reusar el de otro curso) aparece el inicio de
// sesión opcional, y con él la analítica y el asistente de IA.

export const firebaseConfig = {
  apiKey: 'REPLACE_WITH_API_KEY',
  authDomain: 'REPLACE_WITH_PROJECT_ID.firebaseapp.com',
  projectId: 'REPLACE_WITH_PROJECT_ID',
  storageBucket: 'REPLACE_WITH_PROJECT_ID.appspot.com',
  messagingSenderId: 'REPLACE_WITH_SENDER_ID',
  appId: 'REPLACE_WITH_APP_ID',
};

// Short identifier for this course, saved on every student record.
export const courseId = 'seminario';

// The gate is active only once a real apiKey is present.
export const isFirebaseConfigured =
  typeof firebaseConfig.apiKey === 'string' &&
  firebaseConfig.apiKey.length > 0 &&
  !firebaseConfig.apiKey.startsWith('REPLACE');
