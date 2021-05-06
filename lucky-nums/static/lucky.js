/** processForm: get data from form and make AJAX call to our API. */
const BASE_URL = "http://127.0.0.1:5000";


const theName = document.querySelector('#name');
const theYear = document.querySelector('#year');
const theEmail = document.querySelector('#email');
const theColor = document.querySelector('#color');
let theNameErr = document.querySelector('#name-err');
let theYearErr = document.querySelector('#year-err');
let theEmailErr = document.querySelector('#email-err');
let theColorErr = document.querySelector('#color-err');

async function processForm(evt) {
    evt.preventDefault();
    let response = await axios.get(`${BASE_URL}/api/get-lucky-num`)
    handleResponse(response);
}
}

/** handleResponse: deal with response from our lucky-num API. */

function handleResponse(resp) {
    let num_fact = resp.data.num.fact;
    let year = resp.data.year.year;
    let year_fact = resp.data.year.fact;
    $("#lucky-results").text(`Your lucky number fact: ${num_fact} Your birth year is ${year}. A fact about the year is ${year_fact}`)
}


$("#lucky-form").on("submit", processForm);

