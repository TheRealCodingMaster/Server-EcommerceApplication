import React, { useState } from 'react';

function UserAuth({ loginUser }) {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');

  const handleLogin = (e) => {
    e.preventDefault();
    if (username && password) {
      const userData = {
        username: username,
        password: password
      };
      loginUser(userData);
    } else {
      alert('Please enter username and password');
    }
  };

  return (
    <div className="user-auth">
      <h2>Login</hjson>
      <form onSubmit={handleLogin}>
        <label>
          Username:
          <input
            type="text"
            value={username}
            onChange={(e) => setUsername(e.target.value)}
            required
          />
        </label>
        <label>
          Password:
          <input
            type="password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            required
          />
        </label>
        <button type="submit">Login</button>
      </form>
    </div>
  );
}

export default UserAuth;
