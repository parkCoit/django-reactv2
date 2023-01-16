import { NextPage } from "next"
import { useEffect, useState } from "react";
import styled from 'styled-components';
interface Props{ article: string }

const LoginHomePage: NextPage<Props> = () => {
  const [user, setUser] = useState({
    userid : '',
    email : '',
    password : '',
    cpassword: '', 
    username : '',
    phone : '',
    birth : '',
    address : '',
    job : '',
    interests : '',
    token : '',
    created : '',
    modified : ''
  })

  useEffect(()=>{
    setUser(JSON.parse(localStorage.getItem("sessioin")||'{}'))
  },[])


  return (<>
        
      <Sheet >
        <thead>
          <Row>
            <Cell colSpan={2}><h6>회원정보</h6></Cell>
          </Row>
        </thead>
        <tbody>
          <Row>
            <Cell>
              <label htmlFor="email">이메일(ID)</label></Cell>
            <Cell> 
              {user.email}
            </Cell>
          </Row>
        <Row><Cell>
      <label htmlFor="password">비밀번호</label></Cell>
      <Cell>{user.password}
            </Cell>
          </Row>
         
          <Row>
            <Cell>
              <label htmlFor="username">이름(실명)</label>
            </Cell>
            <Cell>
            {user.username}
            </Cell>
          </Row>
          <Row>
            <Cell>
            <label htmlFor="phone">전화번호</label></Cell>
            <Cell>
            {user.phone}
            </Cell>
          </Row>
          <Row>
            <Cell>
            <label htmlFor="birth">생년월일</label> </Cell>
            <Cell>
              {user.birth}
            </Cell>
          </Row>
          <Row>
            <Cell><label htmlFor="address">주소</label></Cell>
            <Cell>{user.address}</Cell>
          </Row>
          <Row>
            <Cell>
            <label htmlFor="job">직업</label></Cell>
            <Cell>{user.job}
            </Cell>
          </Row>
          <Row>
            <Cell>
            <label htmlFor="interests">관심사항</label></Cell>
            <Cell>{user.interests}
            </Cell>
          </Row>
          
          <Row>
            <Cell colSpan={2}><button type="submit" >수정하기</button></Cell>
          </Row>
          
        </tbody>
      </Sheet>

      
    </>)

}

const Sheet = styled.table`
border: 1px solid black
width: 70%
`
const Row = styled.tr`
border: 1px solid black
`
const Cell = styled.td`
border: 1px solid black,
`
const Input = styled.input`
width: 100%
`

export default LoginHomePage