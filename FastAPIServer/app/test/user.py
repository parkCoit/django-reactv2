from fastapi import APIRouter
from fastapi.responses import HTMLResponse


test_router = APIRouter()


@test_router.get("/login")
async def login():
    return HTMLResponse(content="""
    <form action="http://localhost:8000/users/login" method="post" style="width: 300px; margin: 50px auto;" >
  <div class="imgcontainer">
    <img src="img_avatar2.png" alt="Avatar" class="avatar">
  </div>

  <div class="container">
    <label for="uname"><b>Email</b></label>
    <input type="text" placeholder="Enter Username" name="uname" required>

    <label for="psw"><b>Password</b></label>
    <input type="password" placeholder="Enter Password" name="psw" required>

    <button type="submit">Login</button>
    
  </div>

  
</form>
    """)