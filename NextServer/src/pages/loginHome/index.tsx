import { NextPage } from "next"
import { useState, useEffect } from "react"
import { LoginHome } from "@/components/user"

interface Props{ article: string }

const LoginHomePage: NextPage<Props> = () => {
    const [loginUser, setLoginUser] = useState("")
    useEffect(() => {
        setLoginUser(JSON.stringify(localStorage.getItem("loginUser")))
      },[]);

    return (<div>로그인 정보 : {loginUser}  </div>)
}
export default LoginHomePage