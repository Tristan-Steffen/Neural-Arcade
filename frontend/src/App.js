// src/App.js
import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Menu from './components/Menu';
import HomePage from './pages/HomePage';
import TicTacToePage from './pages/TicTacToePage';
import ConnectFourPage from './pages/ConnectFourPage';
import GameOfLifePage from './pages/GameOfLifePage';
import './App.css';

function App() {
    return (
        <Router>
            <div className="App">
                <Menu />
                <div className="content">
                    <Routes>
                        <Route path="/" element={<HomePage />} />
                        <Route path="/tic-tac-toe" element={<TicTacToePage />} />
                        <Route path="/connect-four" element={<ConnectFourPage />} />
                        <Route path="/game-of-life" element={<GameOfLifePage />} />
                    </Routes>
                </div>
            </div>
        </Router>
    );
}

export default App;
