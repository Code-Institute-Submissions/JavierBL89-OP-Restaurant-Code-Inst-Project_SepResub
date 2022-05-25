
const form = document.getElementById("cancelation_form")
const email = document.getElementById("reservation_email")
const phone = document.getElementById("reservation_phone")
const date = document.getElementById("reservation_date");


/**
* INITIALIZE FORM VALIDATION
**/
function handleSubmitCancelation(event){
    form.addEventListener('submit', event => {
        if (!form.checkValidity()) {
      event.preventDefault();
      event.stopPropagation()
      validateInputs(event)

    }

    },false)
    }


function validateInputs(event){
    const emailValue = document.getElementById("reservation_email").value.trim()
    const phoneValue = document.getElementById("reservation_phone").value.trim()
    const dateValue = date.value.trim()

    if(emailValue === ""){
        setErrorForBlank(email, "Field cannot be blank");
      }else{
        emailValidation(emailValue)
      }
      if(phoneValue === ""){
        setErrorForBlank(phone, "Field cannot be blank");
      }else{
        checkLength(phoneValue)
      }
      if(dateValue === ""){
        date.className = "cancelation-input error"
      }else{
        dateValidation(dateValue)
      }
}


/**
 * 
 * EMAIL FORMAT VALIDATION 
 */
function emailValidation(emailValue){
    const validRegex = /^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$/;
    if(emailValue.match(validRegex)){
      setSuccessFor(email)
    }else{
      document.querySelector(".cancelationEmailError").innerText = "Enter a valid email"
    }
  }


  function checkLength(input){

    const userData =  input.getAttribute("id");
    const phoneValue = phone.value.trim()
    const emailValue = email.value.trim()
    
     if(userData == "phone" && phoneValue.length <=7 || phoneValue.length >=9){
      phone.className = "form-control error"
      document.querySelector("cancelation-form .phoneError").innerText = "Must have from 8 to 9 numbers"
    }else{
        setSuccessFor(input)
      }

}

/**
 * 
 * VALIDATE DATE TO BOOK ON A DATE AHEAD
 */
 function dateValidation(dateValue){
  const dayOfWeek =  new Date(dateValue).getDay()
  const month = parseInt(dateValue.slice(5,7));
  const day = parseInt(dateValue.slice(8,10));
  const year = parseInt(dateValue.slice(0,4));

  const currentDate = new Date();
  const currentYear = currentDate.getFullYear();
  const currentMonth = currentDate.getMonth() + 1;
  const currentDay = currentDate.getDate();
 
  if(year >= currentYear){
    if(month >= currentMonth){
      if(day >= currentDay){
        if(opening_days.includes(dayOfWeek)){
          setSuccessFor(date)
        }else{
          setErrorForDate(date, "Opening days from Tuesday to Saturday included")
          console.log("3")
        }
      }else{
        setErrorForDate(date, "Day must be from today onwards")
      }  
    }else{
      setErrorForDate(date, "Month must be ahead")
    }
  }else{
    setErrorForDate(date, "Year must be ahead")
  }
}

/**
 * ERROR MESSAGES FOR INCORRECT DATE
 */
 function setErrorForDate(bookingDate, message){
  bookingDate.className = "form-control error"
  document.querySelector(".cancelationDateError").innerText = message;
}

/**
 * ERROR WARNING AN MESSAGE FOR BLANK INPUTS
 */
 function setErrorForBlank(input, message){
    input.className = "cancelation-input error"
    input.setAttribute("placeholder", message)
  }

  /**
 * TURNS BORDER INPUT INTO GREEN IF DATA PASSES VALIDATION
 */
function setSuccessFor(input){
    input.className = "cancelation-input success"
  }