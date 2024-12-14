import React from 'react';
import { BrowserRouter as Router, Route, Routes, Link } from 'react-router-dom';



function Home(){
	return(
		<>
		<Link to="/Math">Go to Math</Link>
		<Link to="/Eng">Go to Eng</Link>
		</>
		)
}
export default Home;