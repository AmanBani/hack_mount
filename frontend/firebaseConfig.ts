import { initializeApp } from "firebase/app";
import { getAuth, createUserWithEmailAndPassword } from "firebase/auth";
import { getFirestore, collection, addDoc } from "firebase/firestore";
// Import the functions you need from the SDKs you need


const firebaseConfig = {
  apiKey: "AIzaSyAijjcGx5YK0mQUs38q9HVGCWxz7CWxiIQ",
  authDomain: "mount-2189a.firebaseapp.com",
  projectId: "mount-2189a",
  storageBucket: "mount-2189a.firebasestorage.app",
  messagingSenderId: "672519677782",
  appId: "1:672519677782:web:7f01cebd1f79d1df75d8f7",
  measurementId: "G-NLVXN5SGC4"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
export const auth = getAuth(app);
export const db = getFirestore(app);