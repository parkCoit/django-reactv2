import { useState, useEffect } from 'react';

const server = `http://localhost:8000`



export default function Join() {


    
    return (<>
        <h2>회원가입</h2>
        <form action="/send-data-here" method="post" >

          <label htmlFor="user_email">User Email:</label>
          <input type="text"  id="user_email" name="user_email" required minLength= {5} maxLength={20}/>

          <label htmlFor="password">Password:</label>
          <input type="text" id="password" name="password" required />

          <label htmlFor="user_name">user_name:</label>
          <input type="text" id="user_name" name="user_name" required />

          <label htmlFor="phone">phone:</label>
          <input type="text" id="phone" name="phone" required />

          <label htmlFor="birth">birth:</label>
          <input type="text" id="birth" name="birth" />

          <label htmlFor="address">address:</label>
          <input type="text" id="address" name="address" />

          <label htmlFor="job">job:</label>
          <input type="text" id="job" name="job" />

          <label htmlFor="lastuser_interests">user_interests:</label>
          <input type="text" id="user_interests" name="user_interests" />


          <button type="submit">Submit</button>
          </form> 
        </>)
}