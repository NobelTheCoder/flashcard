import React from "react";
import "bootstrap/dist/css/bootstrap.min.css";


function Home() {
  return (
    <div>
      {/* Navbar */}
      <nav className="navbar navbar-expand-lg navbar-light bg-info">
        <div className="container-fluid">
          <button
            className="btn btn-info text-white navbar-brand"
            style={{ border: "none", background: "none", padding: 0 }}
            onClick={() => window.location.href = "/"}
          >
            Home
          </button>

          <button
            className="btn btn-light ms-auto"
            style={{ borderRadius: "20px" }}
            onClick={() => window.location.href = "/push"}
          >
            Add
          </button>
        </div>
      </nav>

      {/* Centered List */}
      <div className="title-container mt-5">
        <h1 className="main-title">Welcome to the Learning Hub</h1>
        <div className="container text-center mt-4">
          <div className="row justify-content-center">
            <div className="col-md-6">
              <button
                className="btn btn-secondary w-100 mb-3"
                style={{ backgroundColor: "#17a2b8", borderColor: "#17a2b8" }}
                onClick={() => window.location.href = "/eng"}
              >
                English
              </button>
              <button
                className="btn btn-secondary w-100"
                style={{ backgroundColor: "#17a2b8", borderColor: "#17a2b8" }}
                onClick={() => window.location.href = "/math"}
              >
                Math
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}

export default Home;
