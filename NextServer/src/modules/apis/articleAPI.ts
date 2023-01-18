import axios, { AxiosResponse } from 'axios'
import {context} from '@/components/admin/enums'
import { currentTime } from '@/components/admin/utils'
import { Article } from '@/modules/types'
import { author, client } from "@/modules/controllers"

export const article = {
    async Write(payload: Article){
        try{
            const response : AxiosResponse<any, Article[]> =
            await axios.post(`http://localhost:8000/article/register`, payload, {headers: {
                "Content-Type" : "application/json",
                Authorization: "JWT fefege...",
            }})
            if(response.data === "success"){
                alert(' 결과: API 내부 join 성공  ')
            }else{
                alert(' 결과: API 내부 join 실패  '+ JSON.stringify(response.data.msg))
            }
            
            return response
        }catch(err){
            console.log(` ${currentTime} : userSaga 내부에서 join 실패 `)
        }
    },
}
