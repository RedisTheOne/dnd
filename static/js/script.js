function run(){
var list = document.getElementById('list')

fetch('https://jsonplaceholder.typicode.com/users')
.then(resp => resp.json())
.then(data => {
    console.log(data)
    data.forEach((d) => {
        list.innerHTML += "Username: " + d.username + "<br>Email: " + d.email + "<br>Phone Number: " + d.phone + "<br> ---- <br>"
    })
})

}


run()