import React, { useState, useEffect } from 'react';
import axios from 'axios';
import './GameOfLife.css';

const BASE_URL = 'http://localhost:5000';

const GameOfLife = () => {
    const [board, setBoard] = useState([]);
    const [rows, setRows] = useState(10); // Initial number of rows
    const [columns, setColumns] = useState(10); // Initial number of columns

    useEffect(() => {
        resetGame();
    }, []);

    const resetGame = async () => {
        try {
            const response = await axios.post(`${BASE_URL}/gameoflife-reset`, { rows, columns });
            setBoard(response.data.board);
        } catch (error) {
            console.error('Error resetting the game:', error);
        }
    };

    const setCell = async (row, column) => {
        try {
            const response = await axios.post(`${BASE_URL}/gameoflife-set`, { row, column });
            setBoard(response.data.board);
        } catch (error) {
            console.error('Error setting cell state:', error);
        }
    };

    const stepGame = async () => {
        try {
            const response = await axios.post(`${BASE_URL}/gameoflife-step`);
            setBoard(response.data.board);
        } catch (error) {
            console.error('Error advancing the game:', error);
        }
    };

    const renderBoard = () => {
        return board.map((row, rowIndex) => (
            <div key={rowIndex} className="row">
                {row.map((cell, colIndex) => (
                    <div
                        key={colIndex}
                        className={`cell ${cell ? 'alive' : 'dead'}`}
                        onClick={() => setCell(rowIndex, colIndex)}
                    ></div>
                ))}
            </div>
        ));
    };

    return (
        <div>
            <div>
                <div>
                    <label>
                        Rows:
                        <input
                            type="range"
                            min="1"
                            max="30"
                            value={rows}
                            onChange={(e) => setRows(parseInt(e.target.value))}
                        />
                    </label>
                    <label>
                        Columns:
                        <input
                            type="range"
                            min="1"
                            max="40"
                            value={columns}
                            onChange={(e) => setColumns(parseInt(e.target.value))}
                        />
                    </label>
                </div>
                <div style={{ display: 'flex' }}>
                    <button className='reset-button' onClick={resetGame}>Reset</button>
                    <button className='reset-button' onClick={stepGame}>Next Step</button>
                </div>
            </div>
            <div className="board">{renderBoard()}</div>
        </div>
    );
};

export default GameOfLife;
