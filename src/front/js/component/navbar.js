// import React from "react";
// import { Link } from "react-router-dom";

// export const Navbar = () => {
// 	return (
// 		<nav className="navbar navbar-light bg-light">
// 			<div className="container">
// 				<Link to="/">
// 					<span className="navbar-brand mb-0 h1">React Boilerplate</span>
// 				</Link>
// 				<div className="ml-auto">
// 					<Link to="/demo">
// 						<button className="btn btn-primary">Check the Context in action</button>
// 					</Link>
// 				</div>
// 			</div>
// 		</nav>
// 	);
// };

import React from "react";
import { Link } from "react-router-dom";
import Favourites from "./favourites";

export const Navbar = () => {
	return (
		<nav className="navbar navbar-light bg-light mb-3">
			<div className="container">
				<Link to="/">
					<span className="navbar-brand mb-0 h1">
						<img
							src="https://www.freepnglogos.com/uploads/star-wars-logo-31.png"
							style={{ width: "70px" }}
						/>
					</span>
				</Link>
				<Favourites />
				{/* <div> */}
				{/* <Link to="/demo"> */}
				{/* <div className="dropdown">
					<button
						className="btn btn-secondary dropdown-toggle"
						type="button"
						id="dropdownMenuButton1"
						data-bs-toggle="dropdown"
						aria-expanded="false">
						Favourites
					</button>
					<ul className="dropdown-menu" aria-labelledby="dropdownMenuButton1">
						<li>
							<a className="dropdown-item" href="#">
								(empty)
							</a>
						</li>
					</ul>
				</div> */}
				{/* </Link> */}
				{/* </div> */}
			</div>
		</nav>
	);
};
