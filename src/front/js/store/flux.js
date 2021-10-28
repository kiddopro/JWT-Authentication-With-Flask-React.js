const getState = ({ getStore, getActions, setStore }) => {
	const URL_PERSONAJES = "https://www.swapi.tech/api/people?page=1&limit=100";

	const URL_PLANETAS = "https://www.swapi.tech/api/planets?page=1&limit=100";

	const URL_SERVIDOR = "https://3001-crimson-anaconda-eijs4bqk.ws-us18.gitpod.io/api/";

	return {
		store: {
			message: null,
			demo: [
				{
					title: "FIRST",
					background: "white",
					initial: "white"
				},
				{
					title: "SECOND",
					background: "white",
					initial: "white"
				}
			],
			listaPersonajes: [],
			listaPlanetas: [],
			favorites: [],
			character: {},
			planet: {}
		},
		actions: {
			loginUser: (e, p) => {
				var myHeaders = new Headers();
				myHeaders.append("Content-Type", "application/json");

				var raw = JSON.stringify({
					email: e,
					password: p
				});

				var requestOptions = {
					method: "POST",
					headers: myHeaders,
					body: raw,
					redirect: "follow"
				};

				fetch(URL_SERVIDOR + "login", requestOptions)
					.then(response => response.json())
					.then(result => {
						result.status = 200 ? localStorage.setItem("token", result.token) : console.log(result.msg);
					})
					.catch(error => console.log("error", error));
			},
			createUser: (e, p) => {
				var myHeaders = new Headers();
				myHeaders.append("Content-Type", "application/json");

				var raw = JSON.stringify({
					email: e,
					password: p
				});

				var requestOptions = {
					method: "POST",
					headers: myHeaders,
					body: raw,
					redirect: "follow"
				};

				fetch(URL_SERVIDOR + "signup", requestOptions)
					.then(response => response.json())
					.then(result => console.log(result))
					.catch(error => console.log("error", error));
			},

			getCharacter: id => {
				const store = getStore();
				fetch("https://www.swapi.tech/api/people/" + id)
					.then(res => res.json())
					.then(data => {
						setStore({ character: data.result });
					})
					.catch(err => err);
			},
			getPlanet: id => {
				fetch("https://www.swapi.tech/api/planets/" + id)
					.then(res => res.json())
					.then(data => {
						setStore({ planet: data.result }); //seteamos el valor del state planet con el objeto que se encuentra en la respuesta del json.result
					})
					.catch(err => err);
			},
			isActive: item => {
				const store = getStore();
				if (store.favorites.includes(item)) {
					return true;
				} else {
					return false;
				}
			},
			setFavorites: favorite => {
				const store = getStore();
				if (store.favorites.includes(favorite)) {
					getActions().removeFavorites(favorite);
				} else {
					setStore({ favorites: [...store.favorites, favorite] });
				}
			},
			removeFavorites: favorite => {
				const store = getStore();
				let newList = store.favorites.filter(elem => elem != favorite);
				setStore({ favorites: newList });
			},

			// Use getActions to call a function within a fuction
			exampleFunction: () => {
				getActions().changeColor(0, "green");
			},
			loadSomeData: () => {
				fetch(URL_PERSONAJES)
					.then(res => res.json())
					.then(response => {
						// store.actions.addPersonajes(response.results);

						setStore({ listaPersonajes: response.results });
					})
					.catch(err => err);

				fetch(URL_PLANETAS)
					.then(res => res.json())
					.then(data => {
						setStore({ listaPlanetas: data.results });
					})
					.catch();
			},

			getMessage: () => {
				// fetching data from the backend
				fetch(process.env.BACKEND_URL + "/api/hello")
					.then(resp => resp.json())
					.then(data => setStore({ message: data.message }))
					.catch(error => console.log("Error loading message from backend", error));
			},
			changeColor: (index, color) => {
				//get the store
				const store = getStore();

				//we have to loop the entire demo array to look for the respective index
				//and change its color
				const demo = store.demo.map((elm, i) => {
					if (i === index) elm.background = color;
					return elm;
				});

				//reset the global store
				setStore({ demo: demo });
			}
		}
	};
};

export default getState;
