import React, { useState, useEffect, useContext } from "react";
import { Link } from "react-router-dom";
import Sign from "../component/sign";

import { Context } from "../store/appContext";

const Signup = () => {
	return (
		<div className="container">
			<div className="title text-center m-3 text-info">
				<h1>Sign up</h1>
			</div>
			<Sign />
		</div>
	);
};

export default Signup;
