import React, { useState, useEffect } from 'react';
import './App.css';
import ProductList from './components/ProductList';
import ShoppingCart from './components/ShoppingCart';
import UserAuth from './components/UserAuth';

function App() {
  const [products, setProducts] = useState([]);
  const [cartItems, setCartItems] = useState([]);
  const [loggedInUser, setLoggedInUser] = useState(null);

  // Fetch products from backend on component mount
  useEffect(() => {
    fetch('/products')
      .then(response => response.json())
      .then(data => setProducts(data))
      .catch(error => console.error('Error fetching products:', error));
  }, []);

  // Add item to cart
  const addToCart = (product) => {
    setCartItems([...cartItems, product]);
  };

  // Remove item from cart
  const removeFromCart = (productId) => {
    const updatedCart = cartItems.filter(item => item.id !== productId);
    setCartItems(updatedCart);
  };

  // Login user
  const loginUser = (userData) => {
    fetch('/login', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(userData),
    })
    .then(response => {
      if (response.ok) {
        setLoggedInUser(userData.username);
      } else {
        alert('Invalid username or password');
      }
    })
    .catch(error => console.error('Error logging in:', error));
  };

  // Logout user
  const logoutUser = () => {
    setLoggedInUser(null);
  };

  return (
    <div className="App">
      <header className="App-header">
        <h1>Welcome to Ecommerce App</h1>
        {loggedInUser ? (
          <p>Hello, {loggedInUser}! <button onClick={logoutUser}>Logout</button></p>
        ) : (
          <UserAuth loginUser={loginUser} />
        )}
      </header>

      <main className="App-main">
        <section className="App-section">
          <ProductList products={products} addToCart={addToCart} />
        </section>

        <section className="App-section">
          <ShoppingCart cartItems={cartItems} removeFromCart={removeFromCart} />
        </section>
      </main>

      <footer className="App-footer">
        <p>&copy; 2024 Ecommerce App. All rights reserved.</p>
      </footer>
    </div>
  );
}

export default App;
