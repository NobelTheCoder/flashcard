import React, { useState } from "react";
import axios from "axios";
import "bootstrap/dist/css/bootstrap.min.css";

function App() {
    const [formData, setFormData] = useState({ question: "", answer: "" });
    const [response, setResponse] = useState(null);
    const [error, setError] = useState(null);

    const handleChange = (e) => {
        const { name, value } = e.target;
        setFormData({ ...formData, [name]: value });
    };

    const handleSubmit = async (e) => {
        e.preventDefault();
        setError(null);
        setResponse(null);

        try {
            const res = await axios.post("http://127.0.0.1:8000/add/", formData);
            setResponse(res.data.message);
        } catch (err) {
            setError(err.response?.data?.detail || "An error occurred");
        }
    };

    return (
        <div
            className="d-flex justify-content-center align-items-center vh-100"
            style={{ backgroundColor: "#e0f7fa" }}
        >
            <div className="card p-4 shadow" style={{ width: "400px" }}>
                <h3 className="text-center text-primary mb-4">Add Q&A</h3>
                <form onSubmit={handleSubmit}>
                    <div className="mb-3">
                        <label htmlFor="question" className="form-label text-primary">
                            Question
                        </label>
                        <input
                            type="text"
                            id="question"
                            name="question"
                            className="form-control"
                            value={formData.question}
                            onChange={handleChange}
                            required
                        />
                    </div>
                    <div className="mb-3">
                        <label htmlFor="answer" className="form-label text-primary">
                            Answer
                        </label>
                        <input
                            type="text"
                            id="answer"
                            name="answer"
                            className="form-control"
                            value={formData.answer}
                            onChange={handleChange}
                            required
                        />
                    </div>
                    <button
                        type="submit"
                        className="btn btn-primary w-100"
                        style={{ backgroundColor: "#00796b", borderColor: "#00796b" }}
                    >
                        Submit
                    </button>
                </form>
                {response && <div className="alert alert-success mt-3">{response}</div>}
                {error && <div className="alert alert-danger mt-3">{error}</div>}
            </div>
        </div>
    );
}

export default App;
