import "./App.css";
import "bootstrap/dist/css/bootstrap.css";
import { useState } from "react";

function App() {
    const [title, setTitle] = useState("");
    const [genre, setGenre] = useState("");

    return (
        <div className="App">
            <form
                onSubmit={(e) => {
                    e.preventDefault();
                    console.log(`tytuł: ${title}; rodzaj: ${genre}`);
                }}
            >
                <div className="form-group">
                    <label htmlFor="title">Tytuł filmu</label>
                    <input
                        type="text"
                        id="title"
                        name="title"
                        className="form-control"
                        value={title}
                        onChange={(e) => setTitle(e.target.value)}
                    />
                </div>
                <div className="form-group">
                    <label htmlFor="genre">Rodzaj</label>
                    <select
                        name="genre"
                        id="genre"
                        className="form-control"
                        value={genre}
                        onChange={(e) => setGenre(e.target.value)}
                    >
                        <option value=""></option>
                        <option value="1">Komedia</option>
                        <option value="2">Obyczajowy</option>
                        <option value="3">Sensacyjny</option>
                        <option value="4">Horror</option>
                    </select>
                </div>
                <button type="submit" className="btn btn-primary">
                    Dodaj
                </button>
            </form>
        </div>
    );
}

export default App;
