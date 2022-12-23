import axios from "axios"
const server = `http://localhost:8000`
export const userLogin = req => axios.post(`${server}/blog/auth/login`, req)
export const userSignup = req => axios.post(`${server}/blog/auth/signup`, req)



const signUpService = {
    signUp2
}

function handleResponse(response){ 
    return response.text()
        .then(text =>{
            const data = text && JSON.parse(text)
            if(!response.ok){
                if(response.status === 401){
                    window.location.reload()
                }
                const error = (data && data.message) ||
                    response.statusText
                return Promise.reject(error)
            }
            return data
        })
}

async function signUp2(){
    const res = await fetch(`${server}/blog/auth/insertdummy`)
    .then(handleResponse)
    .then(data => JSON.stringify(data))
    .catch((error) => {
        alert('error :::: '+error);
    });
    alert('내부 1위영화 ::: '+res)
    return Promise.resolve(res);
}


export default signUpService



