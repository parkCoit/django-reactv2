import { Route, Routes } from "react-router-dom"
import {Counter, Footer, Navigation2 } from "common"
import {Login, SignUp, UserList } from "uat"
import {Schedule} from "../../todos"
import {Stroke2} from "stroke"
import {Iris2} from "dlearn/iris"
import {Number} from "dlearn/number"
import {KospiSamsung} from "dlearn/aitrader"
import {NaverMovie} from "webcrawler"
import {SamsungReport, NaverReview, KoreanClassify} from 'nlp'

import fashion from 'images/fashion.png'


const Home = () =>{
    const imgSize = {minWidth: 500, minHeight : 600}
    return (<>
        <table style={{ width: "1200px", height: "550px", margin: "0 auto", border: "1px solid black"}}>
            <thead>
                <tr style={{ width: "20%",height: "80%",  border: "1px solid black"}}>
                    <td style={{ width: "100%", border: "1px solid black"}}>
                    <Navigation2/>
                    </td>
                </tr>
                </thead>
            <tbody>
                <tr style={{ width: "20%",height: "80%",  border: "1px solid black"}}>
                    <td style={{ width: "100%", border: "1px solid black"}}>
                    <Routes>
                        <Route path="/counter" element={<Counter/>} ></Route>
                        <Route path="/home" element={<h3>스케줄러</h3>} ></Route>
                        <Route path="/todos" element={<Schedule/>} ></Route>
                        <Route path="/auth/signup" element={<SignUp/>} ></Route>
                        <Route path="/auth/login" element={<Login/>} ></Route>
                        <Route path="/auth/userlist" element={<UserList/>} ></Route>
                        <Route path="/stroke" element={<Stroke2/>} ></Route>
                        <Route path="/iris" element={<Iris2/>} ></Route>
                        <Route path="/number" element={<Number/>} ></Route>
                         <Route path="/navermovie" element={<NaverMovie/>} ></Route>
                         <Route path="/nlp/samsung-report" element={<SamsungReport/>} ></Route>
                         <Route path="/nlp/imdb" element={<NaverReview/>} ></Route>
                         <Route path="/nlp/korean-classify" element={<KoreanClassify/>} ></Route>
                         <Route path="/dlearn/kospi-sansung" element={<KospiSamsung/>} ></Route>
                    </Routes>
                    
                    </td>
                </tr>
                
                <tr>
                    <td>
                        <img  src={fashion} alt='개' className={imgSize}/>
                    </td>
                </tr>
                <tr style={{ width: "100%", height: "20%", border: "1px solid black"}}>
                    <td style={{ width: "100%", border: "1px solid black"}}>
                        <Footer/>
                    </td>
                </tr>
            </tbody>
        </table>
    
        </>)
}

export default Home