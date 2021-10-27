import React, { useState, useContext } from "react";
import TitleLogin from "./titleLogin";
import { Context } from "../store/appContext";



const LoginContainer = () => {

    const [email, setEmail] = useState()
    const [password, setPassword] = useState()
    const { actions, store } = useContext(Context);

    return (
        <>
            <TitleLogin />
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
                <button
                    type="button"
                    className="btn btn-outline-warning"
                    onClick={() => actions.loginUser(email, password)}>
                    Crear
                </button>
            </form>
        </>
    )
}


export default LoginContainer