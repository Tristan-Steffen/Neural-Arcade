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
                <li><Link to="/game-of-life">Game of Life</Link></li>
                <li><Link to="/minesweeper">Minesweeper</Link></li>
                <li><Link to="/sudoku">Sudoku</Link></li>
                <li><Link to="/snake">Snake</Link></li>
                <li><Link to="/chess">Chess</Link></li>
            </ul>
        </div>
    );
};

export default Menu;
