import { PayloadAction } from "@reduxjs/toolkit"
import { call, delay, put, takeLatest, takeLeading } from "redux-saga/effects"
import { joinRequest, joinSuccess, loginRequest, loginSuccess,
    userAction, articleAction } from '@/modules/slices';
import { User, Article } from '@/modules/types';
import { user, article } from '@/modules/controllers';
// import { user } from '@/modules/apis/userAPI';
// api 

export function* watchJoin(){
    yield takeLatest(joinRequest, (action: {payload: User}) => {
        
        try{
            const response: any = user.join(action.payload)
            put(joinSuccess(response.payload))
            window.location.href = '/user/login'
        }catch(error){
            put(userAction.joinFailure(error))
        }
    })
}

// export function* watchLogin(){
//     yield takeLatest(loginRequest, (action: {payload: User}) => {
        
//         try{
//             const response: any = user.login(action.payload)
//             put(loginSuccess({data: response.data}))
//             window.location.href = '/loginHome'
//         }catch(error){
//             put(userAction.joinFailure(error))
//         }
//     })
// }

export interface UserLoginInput{ email: string, password: string }
function* login(action: {payload: UserLoginInput}){
    const {loginSuccess, loginFailure } = userAction
    const param = action.payload
    try{
        alert(`2 사가 내부 : ${JSON.stringify(param)}` )
        const response: User = yield call(user.login, param)
        yield put(loginSuccess(response))
        window.location.href = ('/loginHome')
    }catch(error){
        put(userAction.loginFailure(error))
    }
}

export function* watchLogin(){
    const {loginRequest} = userAction
    yield takeLeading(loginRequest, login)
}

