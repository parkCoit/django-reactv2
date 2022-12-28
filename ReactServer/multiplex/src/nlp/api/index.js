
const server = `http://localhost:8000`

const Services = {
    samsung, naverReview
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

async function samsung(){
    const res = await fetch(`${server}/nlp/samsung-report`)
    .then(handleResponse)
    .then(data => JSON.stringify(data))
    .catch((error) => {
        alert('error :::: '+error);
    });
    alert('삼성 리포트 ::: '+res)
    return Promise.resolve(res);
}

async function naverReview(req){
    const requestOption = {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify(req)
    }
    alert(`사용자 이름 : ${JSON.stringify(req)}`)
    const res = await fetch(`${server}/nlp/imdb`, requestOption )
    .then(handleResponse)
    .then(data => JSON.stringify(data))
    .catch((error) => {
        alert('error :::: '+error);
    });
    alert('문장  ::: '+res)
    return Promise.resolve(res);
}



export default Services


