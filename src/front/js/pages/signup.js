import React, { useState, useEffect, useContext } from "react";
import { Link } from "react-router-dom";
import Sign from "../component/signupContainer";

import { Context } from "../store/appContext";

const Signup = () => {
	return (
		<div className="container">
			<Sign />
		</div>
	);
};

export default Signup;
