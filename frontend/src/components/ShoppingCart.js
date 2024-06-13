import React from 'react';

function ShoppingCart({ cartItems, removeFromCart }) {
  return (
    <div className="shopping-cart">
      <h2>Shopping Cart</h2>
      <ul>
        {cartItems.map(item => (
          <li key={item.id}>
            <div>
              <strong>{item.name}</strong> - ${item.price}
            </div>
            <button onClick={() => removeFromCart(item.id)}>Remove</button>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default ShoppingCart;
