import { initializeApp } from "https://www.gstatic.com/firebasejs/9.15.0/firebase-app.js"
import { getDatabase,ref,push } from "https://www.gstatic.com/firebasejs/9.15.0/firebase-database.js"


const appSettings = {
    DatabaseURL: 'https://backend-nst-hackathon-default-rtdb.firebaseio.com/'
}

const app = initializeApp(appSettings)
console.log(app)

const database = getDatabase(app)
const reference = ref(database, 'tasks')

push(reference,'hello')