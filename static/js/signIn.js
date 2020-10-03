if(localStorage.getItem('USERNAME'))
    window.location.href = '/astronaut';

const signInBtn = document.getElementById('signInBtn');
const usernameInput = document.getElementById('usernameInputText');
const passwordInput = document.getElementById('passwordInputText');

signInBtn.addEventListener('click', () => {
    const username = usernameInput.value;
    const password = passwordInput.value;
    fetch('/api/signin', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({username, password})
    })
        .then(res => res.json())
        .then(data => {
            if(!data.status)
                alert("User doesn't exist.")
            else {
                localStorage.setItem('USERNAME', username);
                window.location.href = '/astronaut';
            }
        })
        .catch((err) => console.log(err));
});