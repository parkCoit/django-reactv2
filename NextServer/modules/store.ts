import { configureStore, AnyAction, CombinedState, combineReducers} from '@reduxjs/toolkit'
import { createWrapper } from 'next-redux-wrapper'
import reducer from '@/modules/counter/counterSlice'
import logger from 'redux-logger'
import { HYDRATE } from "next-redux-wrapper"
import createSagaMiddleware from "@redux-saga/core"
const sagaMiddleware = createSagaMiddleware()

const isDev = process.env.NODE_ENV === 'development'

const makestore = () =>
    configureStore({
        reducer,
        middleware: getDefaultMiddleware =>
            isDev ? getDefaultMiddleware().concat(logger) : getDefaultMiddleware(),
        devTools: isDev
    });

export const wrapper = createWrapper(makestore, {
    debug: isDev
}) ;

const store = makestore();

export type AppState = ReturnType<typeof store.getState>;
export type AppDispatch = typeof store.dispatch;

export default store;