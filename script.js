const base_url = "https://cdn.jsdelivr.net/gh/fawazahmed0/currency-api@1/latest/currencies"

const base_url2 = "https://v6.exchangerate-api.com/v6/965a19103494e509fa1e15c1/latest"
// const base_url = "https://v6.exchangerate-api.com/v6/965a19103494e509fa1e15c1/latest/INR"

const dropdowns = document.querySelectorAll(".dropdown select");
const btn = document.querySelector("from button");
const fromCurr = document.querySelector(".from select")
const toCurr = document.querySelector(".to select")
const msg = document.querySelector(".msg")

for (let select of dropdowns) {
  for (currCode in countryList) {
    let newOption = document.createElement("option");
    newOption.innerText = currCode;
    newOption.value = currCode;
    if (select.name === "from" && currCode == "USD") {
      newOption.selected = "selected";
    }
    else if (select.name === "to" && currCode == "INR") {
      newOption.selected = "selected";
    }
    select.append(newOption);
  }
  select.addEventListener("change", (evt) => {
    updataflag(evt.target)
  })
}

const updataflag = (element) => {
  let cuurCode = element.value;
  let countryCode = countryList[cuurCode]
  let newSrc = `https://flagsapi.com/${countryCode}/flat/64.png`
  let img = element.parentElement.querySelector("img");
  img.src = newSrc;
}


btn.addEventListener("click", async (evt) => {
  evt.preventDefault(); // if you click on the button reload the pagge and show some detali in url. it's close this all
  let amount = document.querySelector(".amount input");
  let amtVal = amount.value;
  if (amtVal === "" || amtVal < 1) {
    amtVal = 1
    amount.value = "1"
  }

  // this api not work
  // console.log(fromCurr.value , toCurr.value.toLowerCase())
  // const url = `${base_url}/${fromCurr.value.toLowerCase()}/${toCurr.value.toLowerCase()}.json`;
  // let response = await fetch(url)
  // console.log(url)

  const url2 = `${base_url2}/${fromCurr.value}`;
  let response2 = await fetch(url2)
  let data = await response2.json();
  let rate = data.conversion_rates;
  msg.innerText = `${amtVal} ${fromCurr.value} = ${rate[fromCurr.value] * rate[toCurr.value]} ${toCurr.value}`

});
