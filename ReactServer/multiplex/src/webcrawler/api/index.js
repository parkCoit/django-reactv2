
const server = `http://localhost:8000`

const webcrawlerService = {
    naverMovie
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

async function naverMovie(){
    const res = await fetch(`${server}/webcrawler/naver`)
    .then(handleResponse)
    .then(data => JSON.stringify(data))
    .catch((error) => {
        alert('error :::: '+error);
    });
    alert('내부 1위영화 ::: '+res)
    return Promise.resolve(res);
}


export default webcrawlerService