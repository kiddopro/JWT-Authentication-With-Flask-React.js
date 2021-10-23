import React from "react";
import ButtonSignUp from "./buttonSignup";
import InputEmailSignup from "./emailSignup";
import TitleSignUp from "./titleSignup";
import InputPasswordSignUp from "./passwordSignup";

const Sign = () => {
	return (
		<>
			<TitleSignUp />
			<form>
				<InputEmailSignup />
				<InputPasswordSignUp />
				<ButtonSignUp />
			</form>
		</>
	);
};

export default Sign;
