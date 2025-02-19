"use client";

import React, { useState } from "react";
import "../styles/create_account.css";

const CreateAccount = () => {
  const [formData, setFormData] = useState({
    username: "",
    email: "",
    password: "",
    confirmPassword: "",
  });

  const handleChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    console.log("Form submitted:", formData);
  };

  return (
    <div>
      <div className="main-header">
        <h1>Create Account</h1>
      </div>
      <form className="input-grp" onSubmit={handleSubmit}>
        <label htmlFor="username">Username:</label>
        <input type="text" name="username" value={formData.username} onChange={handleChange} />
        <br /><br />

        <label htmlFor="email">Email:</label>
        <input type="text" name="email" value={formData.email} onChange={handleChange} />
        <br /><br />

        <label htmlFor="password">Password:</label>
        <input type="password" name="password" value={formData.password} onChange={handleChange} />
        <br /><br />

        <label htmlFor="confirmPassword">Confirm Password:</label>
        <input type="password" name="confirmPassword" value={formData.confirmPassword} onChange={handleChange} />
        <br /><br />

        <input type="submit" value="Submit" />
      </form>
    </div>
  );
};

export default CreateAccount;
