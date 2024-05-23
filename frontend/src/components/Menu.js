// src/components/Menu.js
import React from 'react';
import { Link } from 'react-router-dom';
import '../styles/Menu.css';

const Menu = () => {
    return (
        <div className="menu">
            <h2>Spiele</h2>
            <ul>
                <li><Link to="/">Home</Link></li>
                <li><Link to="/tic-tac-toe">Tic Tac Toe</Link></li>
                <li><Link to="/connect-four">Vier Gewinnt</Link></li>
            </ul>
        </div>
    );
};

export default Menu;
