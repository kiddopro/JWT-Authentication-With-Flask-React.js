import React from "react";

const InputEmailSignup = () => {
	return (
		<div className="mb-3">
			<label htmlFor="exampleInputEmail1" className="form-label">
				Email address
			</label>
			<input type="email" className="form-control" id="exampleInputEmail1" aria-describedby="emailHelp" />
			<div id="emailHelp" className="form-text">
				We ll never share your email with anyone else.
			</div>
		</div>
	);
};

export default InputEmailSignup;
