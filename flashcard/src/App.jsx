import React, { useState } from "react";
import axios from "axios";

const UploadForm = () => {
  const [question, setQuestion] = useState("");
  const [answer, setAnswer] = useState("");
  const [file, setFile] = useState(null);
  const [responseMessage, setResponseMessage] = useState("");

  const handleFileChange = (e) => {
    setFile(e.target.files[0]);
  };

  const handleSubmit = async (e) => {
    e.preventDefault();

    if (!question || !answer) {
      alert("Please fill all the fields.");
      return;
    }

    const formData = new FormData();
    formData.append("question", question);
    formData.append("answer", answer);
    if (file) {
      formData.append("file", file);
    }

    try {
      const response = await axios.post("http://127.0.0.1:8000/upload", formData, {
        headers: {
          "Content-Type": "multipart/form-data",
        },
      });

      if (file) {
        setResponseMessage("imgav: OK");
      } else {
        setResponseMessage("imgav: BAD");
      }
      alert(response.data.message);
      console.log(response.data);
    } catch (error) {
      console.error("Error uploading file:", error);
      alert("Failed to upload file.");
    }
  };

  return (
    <div style={{ margin: "20px" }}>
      <h2>Upload Question and Answer with Optional File</h2>
      <form onSubmit={handleSubmit}>
        <div>
          <label>Question:</label>
          <input
            type="text"
            value={question}
            onChange={(e) => setQuestion(e.target.value)}
            required
          />
        </div>
        <div>
          <label>Answer:</label>
          <input
            type="text"
            value={answer}
            onChange={(e) => setAnswer(e.target.value)}
            required
          />
        </div>
        <div>
          <label>File (Optional):</label>
          <input type="file" onChange={handleFileChange} />
        </div>
        <button type="submit">Upload</button>
      </form>
      <div>
        <p>{responseMessage}</p>
      </div>
    </div>
  );
};

export default UploadForm;
