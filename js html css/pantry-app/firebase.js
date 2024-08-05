// Import the functions you need from the SDKs you need
import { initializeApp } from "firebase/app";
import { getFirestore } from "firebase/firestore";
// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
// For Firebase JS SDK v7.20.0 and later, measurementId is optional
const firebaseConfig = {
  apiKey: "AIzaSyCnxI6qELyUYRrtyf_wd_IKvbagrbTZ1qk",
  authDomain: "pantry-app-90ba9.firebaseapp.com",
  projectId: "pantry-app-90ba9",
  storageBucket: "pantry-app-90ba9.appspot.com",
  messagingSenderId: "965004252398",
  appId: "1:965004252398:web:2811b6cf3e539ba6ef8fff",
  measurementId: "G-LN0QJYDXHL"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const firestore = getFirestore(app);

export {firestore}

