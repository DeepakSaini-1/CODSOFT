const url = "https://cat-fact.herokuapp.com/facts";
const factpara = document.querySelector("#fact");
const btn = document.querySelector("#btn");

const getFacts = async () => {
    console.log("Gettin data...");
    let response = await fetch(url);
    console.log(response)
    let data = await response.json();
    console.log(data[0].text)

    factpara.innerText = data[0].text;
};

/*
// using promise chain
function getFacts() {
    fetch(url).then((response) => {
        return response.json();
    }).then((data) => {
        console.log(data);
        factpara.innerText = data[0].text;

    })
}
*/

// getFacts();
btn.addEventListener("click", getFacts);


// const url2 = "https://pokeapi.co/api/v2/evolution-chain/1/";

// const getFacts = async ()=> {
//     console.log("getting data ....")
//     const response = await fetch(url2)
//     console.log(response)
//     const data=response.json();
//     console.log(data)
// }
// getFacts();