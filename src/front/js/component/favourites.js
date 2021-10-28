import React, { useState, useContext } from "react";
import { Context } from "../store/appContext";

const Favourites = () => {
	const { store, actions } = useContext(Context);
	const dropdownContent = store.favorites.map((item, index) => {
		return (
			<li key={index} className="d-flex flex-row justify-content-between align-items-center">
				<a className="dropdown-item" href="#">
					{item}
				</a>
				<span className="dropdown-item text-end">
					<i
						className="fas fa-trash"
						style={{ cursor: "pointer" }}
						onClick={() => actions.removeFavorites(item)}
					/>
				</span>
			</li>
		);
	});
	const dropdownEmpty = (
		<li>
			<a className="dropdown-item text-center" href="#">
				{"( empty )"}
			</a>
		</li>
	);
	return (
		<div className="dropdown">
			<button
				className="btn btn-primary dropdown-toggle "
				type="button"
				id="dropdownMenuButton1"
				data-bs-toggle="dropdown"
				aria-expanded="false">
				{" Favorites "}
				<span className="border-0 rounded bg-secondary px-1 fw-bold">{store.favorites.length}</span>
			</button>
			<ul className="dropdown-menu" aria-labelledby="dropdownMenuButton1">
				{store.favorites.length > 0 ? dropdownContent : dropdownEmpty}
			</ul>
		</div>
	);
};

export default Favourites;
