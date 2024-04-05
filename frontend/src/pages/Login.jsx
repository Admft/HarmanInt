import React from 'react';
import Form from "../components/Form";
import { Link } from 'react-router-dom';
import "../styles/Login.css";
import logo from "../assets/HarmanIntLogo.jpg";
import gradientDesign from "../assets/gradiantDesign.png"; // Make sure this path is correct

function Login() {
  return (
    <div className="login-container" style={{ backgroundImage: `url(${gradientDesign})` }}>
      <div className="login-box">
        <div className="login-logo">
          <img src={logo} alt="Harman Logo" />
        </div>
        <div className="login-form">
          <Form route="/api/token/" method="login" />
          <div className="register-prompt">
            Don't have an account? 
            <br />
            <Link to="/Register" className="register-link">Register here</Link>
          </div>
        </div>
      </div>
    </div>
  );
}

export default Login;
