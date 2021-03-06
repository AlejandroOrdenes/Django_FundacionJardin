import { isEmail, nameValidate, addressValidate, passwordValidate, pass2Validate, get, valid } from "./validaciones.js"

let pass2 = pass2Validate(passwordValidate(get("inputPass").value), passwordValidate(get("inputPass2").value))
get("botonRegistrarse").disabled = true;
const validacion = (e) => {

    e.preventDefault();

    valid(nameValidate(get("inputNombre").value), "inputNombre", "errorNombre")
    valid(addressValidate(get("inputAddress").value), "inputAddress", "errorDireccion")
    valid(isEmail(get("inputEmail").value), "inputEmail", "errorEmail")

    valid(passwordValidate(get("inputPass").value), "inputPass", "errorPass")

    valid(pass2, "inputPass2", "errorPass2")

}

get("inputNombre").addEventListener("blur", function(event) {
    valid(nameValidate(get("inputNombre").value), "inputNombre", "errorNombre")
}, true);

get("inputAddress").addEventListener("blur", function(event) {
    valid(addressValidate(get("inputAddress").value), "inputAddress", "errorDireccion")
}, true);

get("inputEmail").addEventListener("blur", function(event) {
    valid(isEmail(get("inputEmail").value), "inputEmail", "errorEmail")
}, true);

get("inputPass").addEventListener("blur", function(event) {
    valid(passwordValidate(get("inputPass").value), "inputPass", "errorPass")

}, true);

get("inputPass2").addEventListener("blur", function(event) {
    pass2 = pass2Validate(passwordValidate(get("inputPass").value), passwordValidate(get("inputPass2").value))
    if (valid(pass2, "inputPass2", "errorPass2")) {
        get("botonRegistrarse").disabled = false
    }
}, true);


get("botonRegistrarse").addEventListener('submit', validacion);