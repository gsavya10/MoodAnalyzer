// flatpickr(".datepicker", {});
//
// const choices = new Choices('[data-trigger]',
//       {
//         searchEnabled: false,
//         itemSelectText: '',
//       });

function validateForm() {
    var x = document.forms["myForm"]["expression"].value;
    if (x == "") {
        conditions.innerText = "Please tell us about your day!";
        return false;
    }
    console.log(x);
    return true;
}

document.getElementById("myVideo").playbackRate = 1;
