import { all, fork } from "redux-saga/effects"
import{
    watchJoin, watchLogin, watchLogout
} from "./userSaga"

import {
    userWrite
} from "./articleSaga"

export default function* rootSaga(){
    yield all([ fork(watchJoin), fork(watchLogin), fork(watchLogout), fork(userWrite) ])
}