import React, { useContext, useState } from "react";
import { Context } from "../store/appContext";

import TitleSignUp from "./titleSignup";

const SignupContainer = () => {
	const { actions, store } = useContext(Context);
	const [email, setEmail] = useState();
	const [password, setPassword] = useState();
	return (
		<>
			<TitleSignUp />
			<form>
				<div className="mb-3">
					<label htmlFor="exampleInputEmail1" className="form-label">
						Email address
					</label>
					<input
						type="email"
						className="form-control"
						id="exampleInputEmail1"
						aria-describedby="emailHelp"
						onChange={e => setEmail(e.target.value)}
					/>
					<div id="emailHelp" className="form-text">
						We ll never share your email with anyone else.
					</div>
				</div>
				<div className="mb-3">
					<label htmlFor="exampleInputPassword1" className="form-label">
						Password
					</label>
					<input
						type="password"
						className="form-control"
						id="exampleInputPassword1"
						onChange={e => setPassword(e.target.value)}
					/>
				</div>
				<div className="d-flex justify-content-between align-items-center">
					<button
						type="button"
						className="btn btn-outline-warning"
						onClick={() => actions.createUser(email, password)}>
						Crear
					</button>
					<a href="#">You already have an account?</a>
				</div>
			</form>
		</>
	);
};

export default SignupContainer;
