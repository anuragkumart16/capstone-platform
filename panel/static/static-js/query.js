function closeModal() {
  const modal = document.getElementById("modal");
  modal.style.display = "none";
  location.reload(true);
}
function sendQueryResponse() {
  let kid = document.getElementById("modal-username").dataset.id;
  let answer = document.getElementById("modal-response").value;
  fetch("http://127.0.0.1:8000/query-handler", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      id: kid,
      answer: answer,
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
    })
    .catch((error) => {
      console.error("Error sending data:", error);
    });
}

function openModal(element) {
  console.log(element);
  const modal = document.getElementById("modal");
  modal.style.display = "flex";

  document.getElementById("modal-username").value = element.student;
  document.getElementById("modal-query").innerHTML = element.query;
  link = "http://127.0.0.1:8000/media/" + element.file;
  document.getElementById("modal-file-link").setAttribute("href", link);
  document.getElementById("modal-file-link").innerHTML = link;
  document.getElementById("modal-file-link").setAttribute("target", "_blank");
  document.getElementById("modal-username").setAttribute("data-id", element.id);

  // document.getElementById("modal-username").value = element.student;
  // document.getElementById("modal-hosted-link").setAttribute("target", "_blank");
}

function createTable(result) {
  const tbody = document.getElementById("tbody");

  const data = result.data.map((item) => {
    return {
      id: item.pk,
      file: item.fields.file,
      query: item.fields.query,
      is_answered: item.fields.is_answered,
      student: item.fields.student,
    };
  });
  console.log(data);
  data.forEach((element) => {
    console.log(element);
    // console.log(key, value);
    const tr = document.createElement("tr");
    const username = document.createElement("td");
    const isAnswered = document.createElement("td");

    tbody.appendChild(tr);
    tr.setAttribute("data-id", element.id);
    tr.appendChild(username);
    tr.appendChild(isAnswered);
    tr.addEventListener("click", function () {
      openModal(element); // Pass key when clicked
    });

    isAnswered.innerHTML = element.is_answered;
    username.innerHTML = element.student;
  });
}

function getData() {
  fetch("http://127.0.0.1:8000/get-query", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      mentor: mentor,
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

const params = new URLSearchParams(window.location.search);
const mentor = params.get("username");

getData();

function landPage() {
  window.location.href = `landing-page.html?username=${mentor}`;
}
