import axios from "axios"
const server = `http://localhost:8000`
export const getnumber = req => axios.get(`${server}/dlearn/number?req=${req}`)
export const postnumber = req => axios.post(`${server}/dlearn/number`, req)
