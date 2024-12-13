import React, { useState, useEffect } from "react";
import axios from "axios";
import "bootstrap/dist/css/bootstrap.min.css";
import "./GET.css";

function GET() {
  const [currentBlock, setCurrentBlock] = useState(null);
  const [currentIndex, setCurrentIndex] = useState(0);
  const [isFlipped, setIsFlipped] = useState(false);
  const [error, setError] = useState(null);

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

  useEffect(() => {
    fetchBlock(currentIndex);
  }, [currentIndex]);

  const handleFlip = () => {
    setIsFlipped(!isFlipped);
  };

  const handleNext = () => {
    setIsFlipped(false);
    setCurrentIndex((prevIndex) => prevIndex + 1);
  };

  const handlePrevious = () => {
    setIsFlipped(false);
    setCurrentIndex((prevIndex) => Math.max(0, prevIndex - 1));
  };

  return (
    <div className="container mt-5 text-center">
      <h1>Flashcard App</h1>

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
  );
}

export default GET;
