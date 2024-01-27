import './App.css';
import React,{useState} from 'react';
import "bootstrap/dist/css/bootstrap.min.css"
//react-router
import {BrowserRouter as Router,Routes,Route,Link,useParams,Navigate,useNavigate} from "react-router-dom"

//toastify
import { ToastContainer } from 'react-toastify';
import "react-toastify/dist/ReactToastify.min.css"

//firebase
import { initializeApp } from "firebase/app";
import "firebase/auth"

//components
import Home from "./pages/Home"
import SignIn from "./pages/SignIn"
import Signup from "./pages/Signup"
import PagenotFound from "./pages/PagenotFound"
import {UserContext} from "./context/UserContext"
import Footer from './layout/Footer';
import Header from './layout/Header';
//importing firebase config
import firebaseConfig from './config/firebaseConfig';
//init firebase
initializeApp(firebaseConfig);

const App = () => {
  const [user,setUser]=useState(null)
  return (
    <Router>
      
      <ToastContainer></ToastContainer>
      <UserContext.Provider value={{user,setUser}}>
      <Header></Header>
        <Routes>
          <Route path='/' element={<Home/>} />
          <Route path='/signin' element={<SignIn/>} />
          <Route path='/signup' element={<Signup/>} />
          <Route path='*' element={<PagenotFound/>} />
        </Routes>
      </UserContext.Provider>
      <Footer></Footer>
    </Router>
  );
}

export default App;
