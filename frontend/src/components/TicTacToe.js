// src/TicTacToe.js
import React, { useState, useEffect } from 'react';
import axios from 'axios';
import '../styles/TicTacToe.css';

const TicTacToe = () => {
    const [board, setBoard] = useState(Array(9).fill(null));
    const [winner, setWinner] = useState(null);
    const [currentPlayer, setCurrentPlayer] = useState(1);

    useEffect(() => {
        resetGame();
    }, []);

    const resetGame = async () => {
        try {
            const response = await axios.post('http://localhost:5000/reset');
            setBoard(response.data);
            setWinner(null);
            setCurrentPlayer(1);
        } catch (error) {
            console.error('Error resetting the game:', error);
        }
    };

    const handleClick = async (index) => {
        console.log(winner);
        if (board[index] || winner !== null) return;
        console.log("click");
        try {
            const response = await axios.post('http://localhost:5000/move', { position: index });
            console.log(response)
            setBoard(response.data.board);
            setWinner(response.data.winner);
            setCurrentPlayer((prevPlayer) => (prevPlayer === 1 ? 2 : 1));
        } catch (error) {
            console.error('Invalid move:', error);
        }
    };

    const renderSquare = (index) => (
        <button className="square" onClick={() => handleClick(index)}>
            {board[index] === 1 ? 'X' : board[index] === 2 ? 'O' : ''}
        </button>
    );

    const status = winner === -1 ? `Next player: ${currentPlayer === 1 ? 'X' : 'O'}` :
        winner === 0 ? 'Draw!' :
        `Winner: ${winner === 1 ? 'X' : 'O'}`;

    return (
        <div>
            <div className="status">{status}</div>
            <div className="board-row">
                {renderSquare(0)}
                {renderSquare(1)}
                {renderSquare(2)}
            </div>
            <div className="board-row">
                {renderSquare(3)}
                {renderSquare(4)}
                {renderSquare(5)}
            </div>
            <div className="board-row">
                {renderSquare(6)}
                {renderSquare(7)}
                {renderSquare(8)}
            </div>
            <button onClick={resetGame}>Reset</button>
        </div>
    );
};

export default TicTacToe;
