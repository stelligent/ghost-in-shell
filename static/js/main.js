const handler = (e) => {
    e.preventDefault();

    const numElement = document.getElementById('num')
    const factorialElement = document.getElementById('factorial')
    const number = numElement.value;
    const options = {
        url: '/factorial/',
        body: JSON.stringify( {'number': number} ), 
        method: 'POST',
        headers: {
            'Content-type': 'application/json'
        } 
    };
    console.log('options', options)
    fetch('factorial/', options).then(response => {
        const json = response.json().then( json => {
            console.log('response', response)
            console.log('json', json)
            numElement.value = '';
            factorialElement.textContent = `The factorial of ${number} is ${json['factorial']}.`
        })
    })
};

const main = () => {
    document.getElementById('form').addEventListener('submit', handler)
    document.getElementById('submit').addEventListener('click', handler)
}

document.addEventListener('DOMContentLoaded', main)
