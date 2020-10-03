if(localStorage.getItem('USERNAME'))
    window.location.href = '/astronaut';

const signUpBtn = document.getElementById('signUpBtn');
const firstNameInput = document.getElementById('firstNameInput');
const lastNameInput = document.getElementById('lastNameInput');
const sleepGoalInput = document.getElementById('sleepGoalInput');
const caloriesGoalInput = document.getElementById('caloriesGoalInput');
const usernameInput = document.getElementById('usernameInput');
const passwordInput = document.getElementById('passwordInput');

document.getElementById('avatarBtn').addEventListener('click', () => {
    document.getElementById('avatarInput').click();
});

signUpBtn.addEventListener('click', () => {
    if(document.getElementById('avatarInput').files[0]) {
        const formData = new FormData();
        formData.append('username', usernameInput.value);
        formData.append('lastName', lastNameInput.value);
        formData.append('firstName', firstNameInput.value);
        formData.append('sleepGoal', sleepGoalInput.value);
        formData.append('username', usernameInput.value);
        formData.append('password', passwordInput.value);
        formData.append('caloriesGoal', caloriesGoalInput.value);
        formData.append('avatar', document.getElementById('avatarInput').files[0])
        fetch('/api/signup', {
            method: 'POST',
            body: formData
        })
            .then(res => res.json())
            .then(data => {
                if(data.status) {
                    localStorage.setItem('USERNAME', usernameInput.value);
                    window.location.href = '/astronaut';
                } else
                    alert('This username is taken, please choose another one.');
            });
    } else
        alert('Please add a avatar')
});