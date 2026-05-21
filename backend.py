from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/", response_class=HTMLResponse)
async def home():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Code Realme</title>
        <style>
            body{
                background:#0f172a;
                color:white;
                font-family:Arial;
                display:flex;
                justify-content:center;
                align-items:center;
                height:100vh;
                margin:0;
            }

            .box{
                background:#111827;
                padding:40px;
                border-radius:20px;
                text-align:center;
                width:400px;
                box-shadow:0 0 40px rgba(168,85,247,0.5);
            }

            h1{
                color:#facc15;
            }

            button{
                padding:15px 30px;
                border:none;
                border-radius:10px;
                background:#9333ea;
                color:white;
                cursor:pointer;
                font-size:18px;
            }

            button:hover{
                background:#7e22ce;
            }
        </style>
    </head>

    <body>
        <div class="box">
            <h1>CODE REALME NONSTOP</h1>
            <p>FastAPI Render Stable Version</p>

            <button onclick="testServer()">
                Test Server
            </button>

            <p id="status"></p>
        </div>

        <script>
            function testServer(){
                document.getElementById("status").innerHTML =
                "Server Running Perfectly";
            }
        </script>
    </body>
    </html>
    """
