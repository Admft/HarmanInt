import React from 'react';
import Form from "../components/Form";
import { Link } from 'react-router-dom';
import "../styles/Register.css"; // Import the correct CSS file
import logo from "../assets/HarmanIntLogo.jpg";
import backgroundwavesound from "../assets/backgroundwavesound.png"; // Ensure path is correct

function Register() {
  return (
    <div className="register-container" style={{ backgroundImage: `url(${backgroundwavesound})` }}>
      <div className="register-box">
        <div className="register-logo">
          <img src={logo} alt="Harman Logo" />
        </div>
        <div className="register-form">
          <Form route="/api/user/register/" method="register" />
          <div className="register-prompt">
            Already have an account?
            <br />
            <Link to="/Login" className="register-link">Log in here</Link>
          </div>
        </div>
      </div>
    </div>
  );
}

export default Register;
