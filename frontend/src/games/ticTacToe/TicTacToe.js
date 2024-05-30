// src/TicTacToe.js
import React, { useState, useEffect } from 'react';
import axios from 'axios';
import './TicTacToe.css';

const TicTacToe = () => {
    const [board, setBoard] = useState(Array(9).fill(null));
    const [winner, setWinner] = useState(null);
    const [currentPlayer, setCurrentPlayer] = useState(1);
    const [status, setStatus] = useState('Next player: X');

    useEffect(() => {
        resetGame();
    }, []);

    // Base URL for the backend
    const BASE_URL = 'http://localhost:5000';

    const resetGame = async () => {
        try {
            const response = await axios.post(`${BASE_URL}/tictactoe-reset`);
            setBoard(response.data);
            setWinner(null);
            setCurrentPlayer(response.data.currentPlayer);
        } catch (error) {
            console.error('Error resetting the game:', error);
        }
    };

    const handleClick = async (index) => {
        if (board[index] || winner !== null) return;
        try {
            const response = await axios.post(`${BASE_URL}/tictactoe-move`, { position: index });
            console.log(response.data);
            setBoard(response.data.board);
            setWinner(response.data.winner);
            setCurrentPlayer((prevPlayer) => (prevPlayer === 1 ? -1 : 1));
        } catch (error) {
            console.error('Invalid move:', error);
        }
    };

    useEffect(() => {
        changestatus();
    }, [winner, currentPlayer]);

    const renderSquare = (index) => (
        <button className="square" onClick={() => handleClick(index)}>
            {board[index] === 1 ? 'X' : board[index] === -1 ? 'O' : ''}
        </button>
    );

    function changestatus () {
        if (winner === null) {
            if (currentPlayer === 1) {
                setStatus('Next player: O');
            } else {
                setStatus('Next player: X');
            }
        } else if (winner === 0) {
            setStatus('Draw!');
        } else if (winner === 1) {
            setStatus('Winner: X');
        } else if (winner === -1) {
            setStatus('Winner: O');
        }
    }

    return (
        <div>
            <div className="status">{status}</div>
            <div className="row">
                {renderSquare(0)}
                {renderSquare(1)}
                {renderSquare(2)}
            </div>
            <div className="row">
                {renderSquare(3)}
                {renderSquare(4)}
                {renderSquare(5)}
            </div>
            <div className="row">
                {renderSquare(6)}
                {renderSquare(7)}
                {renderSquare(8)}
            </div>
            <button className='square reset-button' onClick={resetGame}>Reset</button>
        </div>
    );
};

export default TicTacToe;
