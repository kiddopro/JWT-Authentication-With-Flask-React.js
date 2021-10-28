import React, { useContext } from "react";
import PropTypes from "prop-types";
import { Context } from "../store/appContext";
import { Link } from "react-router-dom";

const Card = props => {
	const { store, actions } = useContext(Context);
	const isActive = { color: "#000", backgroundColor: "#ffc107", borderColor: "#ffc107" };
	return (
		<div className="card" style={{ width: "auto", display: "inline-block", margin: "10px" }}>
			<img className="card-img-top" src="https://via.placeholder.com/400x200" alt="Card image cap" />
			<div className="card-body">
				<h5 className="card-title">{props.name}</h5>
				<p className="card-text">{props.url}</p>
				<div className="d-flex justify-content-between">
					<Link to={props.link + props.uid}>
						<button type="button" className="btn btn-outline-primary">
							Learn More!
						</button>
					</Link>
					<button
						type="button"
						className="btn btn-outline-warning"
						style={actions.isActive(props.name) ? isActive : {}}
						onClick={() => actions.setFavorites(props.name)}>
						<i className="far fa-heart" />
					</button>
				</div>
			</div>
		</div>
	);
};

Card.propTypes = {
	name: PropTypes.string,
	url: PropTypes.string,
	uid: PropTypes.string,
	link: PropTypes.string
};

export default Card;
