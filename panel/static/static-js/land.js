function closeModal(){
    const modal = document.getElementById('modal')
    modal.style.display = 'none'
}
function updateModel(){
    console.log('update data')
}

function openModal(key) {
    const modal = document.getElementById('modal')
    modal.style.display='flex'

  fetch("http://127.0.0.1:8000/get-student-data", {
    method: "POST", // HTTP method (can also be PUT, DELETE, etc.)
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      student: key,
    }),
  })
    .then((response) => {
      if (!response.ok) {
        throw new Error(`HTTP error! Status: ${response.status}`);
      }
      return response.json();
    })
    .then((result) => {
      document.getElementById('modal-username').value = result.username
      document.getElementById('modal-email').value = result.email
      document.getElementById('modal-figma').setAttribute('href',result.figma)
      document.getElementById('modal-figma').setAttribute('target','_blank')
      document.getElementById('modal-hosted-link').setAttribute('href',result.hosted_link)
      document.getElementById('modal-hosted-link').setAttribute('target','_blank')
      document.getElementById('modal-github').setAttribute('href',result.github_link)
      document.getElementById('modal-github').setAttribute('target','_blank')
      document.getElementById('modal-explanation').setAttribute('href',result.explanation_link)
      document.getElementById('modal-explanation').setAttribute('target','_blank')
    })
    .catch((error) => {
      console.error("Error sending data:", error);
    });
}

function createTable(result) {
  const tbody = document.getElementById("tbody");

  for (const [key, value] of Object.entries(result.data)) {
    // console.log(key, value);
    const tr = document.createElement("tr");
    const username = document.createElement("td");
    const email = document.createElement("td");
    const isSubmmited = document.createElement("td");

    tbody.appendChild(tr);
    tr.setAttribute("data-username", key);
    tr.setAttribute("id", key);
    tr.appendChild(username);
    tr.appendChild(isSubmmited);
    tr.appendChild(email);
    tr.addEventListener("click", function () {
      openModal(key); // Pass key when clicked
    });

    if (value.isSubmitted === true) {
      isSubmmited.innerHTML = "Submitted";
    } else {
      isSubmmited.innerHTML = "Not Submitted";
    }
    username.innerHTML = value.username;
    email.innerHTML = value.email;
  }
}

function getData(mentor) {
  message = document.getElementById("message");
  fetch("http://127.0.0.1:8000/mentor-student-data", {
    method: "POST", // HTTP method (can also be PUT, DELETE, etc.)
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      MentorName: mentor,
    }),
  })
    .then((response) => {
      if (!response.ok) {
        throw new Error(`HTTP error! Status: ${response.status}`);
      }
      return response.json();
    })
    .then((result) => {
      console.log(result);
      createTable(result);
    })
    .catch((error) => {
      console.error("Error sending data:", error);
    });
}

function updateMarks(){
    const html_structure = document.getElementById('modal-html-structure').value;
    const modal_css_design = document.getElementById('modal-css-design').value;
    const modal_debugging = document.getElementById('modal-debugging').value;
    const modal_responsiveness = document.getElementById('modal-responsiveness').value;
    const modal_funtional_design = document.getElementById('modal-funtional-design').value;
    const username = document.getElementById('modal-username').value;
    const email = document.getElementById('modal-email').value;
    fetch('http://127.0.0.1:8000/set-marks', {
      method: 'POST', // HTTP method (can also be PUT, DELETE, etc.)
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        name: username,
        email: email,
        html_structure: html_structure,
        css_design : modal_css_design,
        responsiveness: modal_responsiveness,
        functional_design: modal_funtional_design,
        debugging: modal_debugging
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
      })
      .catch(error => {
        console.error('Error sending data:', error);
      });
}
const params = new URLSearchParams(window.location.search);
const mentor = params.get("username");

function queryPage(){
  window.location.href = `query.html?username=${mentor}`;
}

getData(mentor);


// window.location.href = `landing-page.html?username=${usernameInput}`;