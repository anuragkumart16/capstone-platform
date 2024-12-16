function submitForm() {
    usernameInput = document.getElementById('username').value;
    passwordInput = document.getElementById('password').value;
    message = document.getElementById('message')
    fetch('http://127.0.0.1:8000/mentor-login', {
      method: 'POST', // HTTP method (can also be PUT, DELETE, etc.)
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        username: usernameInput,
        password: passwordInput,
      }), 
    })
      .then(response => {
        if (!response.ok) {
          throw new Error(`HTTP error! Status: ${response.status}`);
        }
        return response.json();
      })
      .then(result => {
        console.log('Response from server:', result); 
        if(result.LoggedIn === true){
          window.location.href = `landing-page.html?username=${usernameInput}`;
        }else{
          message.innerHTML = result.message
        }
      })
      .catch(error => {
        console.error('Error sending data:', error);
      });
  }
  
  function validateForm() {
    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;
    const message = document.getElementById('message')

    if (username === '') {
      message.innerHTML = 'Username is verified!'
      return false;
    }
    else if (password === '') {
      message.innerHTML = 'Password is verified!'
      return false;
    }
    else{
        console.log('this is working')
        submitForm()
    }
  }
  
  