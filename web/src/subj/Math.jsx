import React, { useState, useEffect } from "react";
import axios from "axios";
import "bootstrap/dist/css/bootstrap.min.css";
import "./Math.css";

function Math() {
  const [currentBlock, setCurrentBlock] = useState(null);
  const [currentIndex, setCurrentIndex] = useState(0);
  const [isFlipped, setIsFlipped] = useState(false);
  const [error, setError] = useState(null);
  const [totalBlocks, setTotalBlocks] = useState(0);

  const fetchBlock = async (index) => {
    try {
      const response = await axios.get(`http://127.0.0.1:8000/get/${index}`);
      setCurrentBlock(response.data);
      setError(null);
    } catch (err) {
      setError("Block not found. Please check the question number.");
      setCurrentBlock(null);
    }
  };

  const fetchTotalBlocks = async () => {
    try {
      const response = await axios.get("http://127.0.0.1:8000/total_blocks");
      setTotalBlocks(response.data.total_blocks);
    } catch (err) {
      setError("Failed to fetch the total number of blocks.");
    }
  };

  useEffect(() => {
    fetchBlock(currentIndex);
  }, [currentIndex]);

  useEffect(() => {
    fetchTotalBlocks();
  }, []);

  const handleFlip = () => {
    setIsFlipped(!isFlipped);
  };

  const handleNext = () => {
    if (currentIndex + 1 >= totalBlocks) {
      setError("No available questions.");
      return;
    }
    setIsFlipped(false);
    setCurrentIndex((prevIndex) => prevIndex + 1);
  };

  const handlePrevious = () => {
    setIsFlipped(false);
    setCurrentIndex((prevIndex) => Math.max(0, prevIndex - 1));
  };

  return (
    <div>
      {/* Navbar */}
      <nav className="navbar navbar-expand-lg navbar-light bg-info">
        <div className="container-fluid">
          <a className="navbar-brand text-white" href="#">Home</a>
          <button className="btn btn-light ms-auto" style={{ borderRadius: "20px" }} onClick={() => window.location.href = "/push"}>Add</button>
        </div>
      </nav>

      {/* Title */}
      <div className="title-container">
        <h1 className="main-title">Mathematic</h1>
      </div>

      {/* Main Content */}
      <div className="container mt-3 text-center">
        {error && <div className="alert alert-danger">{error}</div>}

        {currentBlock ? (
          <div
            className={`flashcard ${isFlipped ? "flipped" : ""}`}
            onClick={handleFlip}
          >
            <div className="flashcard-inner">
              <div className="flashcard-front">
                <h3>Question</h3>
                <p>{currentBlock.question}</p>
                <button className="btn btn-primary mt-3">Show Answer</button>
              </div>
              <div className="flashcard-back">
                <h3>Answer</h3>
                <p>{currentBlock.answer}</p>
                <button className="btn btn-primary mt-3">Show Question</button>
              </div>
            </div>
          </div>
        ) : (
          <div className="alert alert-info">Loading...</div>
        )}

        <div className="navigation mt-4">
          {currentIndex > 0 && (
            <button className="btn btn-secondary me-3" onClick={handlePrevious}>
              &lt; Previous
            </button>
          )}
          <button className="btn btn-secondary" onClick={handleNext}>
            Next &gt;
          </button>
        </div>
      </div>
    </div>
  );
}

export default Math;
