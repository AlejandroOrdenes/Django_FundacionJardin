import { nameValidate, passwordValidate, get, valid } from "./validaciones.js"

const validacion = (e) => {

    e.preventDefault();

    valid(nameValidate(get("floatingInput").value), "floatingInput", "errorEmailLog")

    valid(passwordValidate(get("floatingPassword").value), "floatingPassword", "errorPassLog")

}

get("floatingInput").addEventListener("blur", function(event) {
    valid(nameValidate(get("floatingInput").value), "floatingInput", "errorEmailLog")
}, true);

get("floatingPassword").addEventListener("blur", function(event) {
    valid(passwordValidate(get("floatingPassword").value), "floatingPassword", "errorPassLog")

}, true);

get("inicioUserBtn").addEventListener('click', validacion);