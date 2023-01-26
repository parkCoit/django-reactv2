import { PayloadAction } from "@reduxjs/toolkit"
import { call, delay, put, takeLatest } from "redux-saga/effects"
import { writeRequest, writeSuccess, writeFailure, articleAction } from '@/modules/slices';
import { Article } from '@/modules/types';
import { article } from '@/modules/controllers';


export function* userWrite(){
    yield takeLatest(writeRequest, (action: {payload: Article}) => {
        
        try{
            const response: any = article.Write(action.payload)
            // put(loginSuccess(response.data))
            window.location.href = '/write'
        }catch(error){
            put(articleAction.writeFailure(error))
        }
    })
}