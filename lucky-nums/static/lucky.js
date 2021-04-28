/** processForm: get data from form and make AJAX call to our API. */

async function processForm(evt) {
    evt.preventDefault();
    respo = await axios.post('/api/get-lucky-num');
    handleResponse(respo);
}

/** handleResponse: deal with response from our lucky-num API. */

function handleResponse(resp) {
    $("lucky-results").text(resp)
}


$("#lucky-form").on("submit", processForm);

