import axios from "axios"
const server = `http://localhost:8000`
export const mplexMoviesFakeFaces = req => axios.get(`${server}/mplex/moives/fake_faces`, req)