import React, { useState, useEffect } from 'react';
import axios from 'axios';
import '../styles/ConnectFour.css';

const BASE_URL = 'http://localhost:5000';

const ConnectFour = () => {
    const [board, setBoard] = useState(Array(6).fill(Array(7).fill(0)));
    const [winner, setWinner] = useState(null);
    const [currentPlayer, setCurrentPlayer] = useState(1);

    useEffect(() => {
        resetGame();
    }, []);

    const resetGame = async () => {
        try {
            const response = await axios.post(`${BASE_URL}/connectfour-reset`);
            setBoard(response.data.board);
            setWinner(null);
            setCurrentPlayer(response.data.currentPlayer);
        } catch (error) {
            console.error('Error resetting the game:', error);
        }
    };

    const makeMove = async (col) => {
        if (winner !== null) return;

        try {
            const response = await axios.post(`${BASE_URL}/connectfour-move`, { column: col });
            setBoard(response.data.board);
            console.log(response.data)
            setWinner(response.data.winner);
            setCurrentPlayer(response.data.currentPlayer);
        } catch (error) {
            console.error('Error making a move:', error);
        }
    };

    const renderBoard = () => {
        return board.map((row, rowIndex) => (
            <div key={rowIndex} className="row">
                {row.map((cell, colIndex) => (
                    <div key={colIndex} className="cell" onClick={() => makeMove(colIndex)}>
                        {cell === 1 ? 'X' : cell === 2 ? 'O' : ''}
                    </div>
                ))}
            </div>
        ));
    };

    return (
        <div>
            <div className="board">{renderBoard()}</div>
            {winner !== null && <h2>Winner: Player {winner}</h2>}
            <button onClick={resetGame}>Reset</button>
        </div>
    );
};

export default ConnectFour;
