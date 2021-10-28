import React, { useContext } from "react";
import { Context } from "../store/appContext";
import Card from "./card";
const CardContainerCharacters = props => {
	const { store, actions } = useContext(Context);
	return (
		<>
			<h1 className="text-danger">Characters</h1>
			<div
				className="scrolling-wrapper row flex-row flex-nowrap row-cols-1 row-cols-md-3 
"
				style={{ overflowX: "scroll", overflowY: "hidden", whiteSpace: "nowrap" }}>
				{store.listaPersonajes.map((item, index) => {
					return <Card key={item.uid} name={item.name} url={item.url} uid={item.uid} link="/character/" />;
				})}
			</div>
		</>
	);
};

export default CardContainerCharacters;
