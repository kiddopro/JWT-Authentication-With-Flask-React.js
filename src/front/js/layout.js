import React from "react";
import { BrowserRouter, Route, Switch, Redirect } from "react-router-dom";
import ScrollToTop from "./component/scrollToTop";

import { Home } from "./pages/home";
import { Demo } from "./pages/demo";
import { Single } from "./pages/single";
import injectContext from "./store/appContext";
import Signup from "./pages/signup";
import Login from "./pages/login";
import LearnMoreCharacter from "./pages/learnMoreCharacter";
import LearnMorePlanet from "./pages/learnMorePlanet";

import { Navbar } from "./component/navbar";
import { Footer } from "./component/footer";

//create your first component
const Layout = () => {
	//the basename is used when your project is published in a subdirectory and not in the root of the domain
	// you can set the basename on the .env file located at the root of this project, E.g: BASENAME=/react-hello-webapp/
	const basename = process.env.BASENAME || "";
	const loginIn = localStorage.getItem("token");

	return (
		<div>
			<BrowserRouter basename={basename}>
				<ScrollToTop>
					<Navbar />
					<Switch>
						<Route exact path="/">
							{loginIn ? <Home /> : <Redirect to="/login" />}
						</Route>
						<Route exact path="/signup">
							<Signup />
						</Route>
						<Route exact path="/login">
							<Login />
						</Route>
						<Route exact path="/character/:id">
							{loginIn ? <LearnMoreCharacter /> : <Redirect to="/login" />}
						</Route>
						<Route exact path="/planet/:id">
							{loginIn ? <LearnMorePlanet /> : <Redirect to="/login" />}
						</Route>
						<Route>
							<h1>Not found!</h1>
						</Route>
					</Switch>
					<Footer />
				</ScrollToTop>
			</BrowserRouter>
		</div>
	);
};

export default injectContext(Layout);
