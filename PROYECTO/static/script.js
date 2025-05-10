document.addEventListener("DOMContentLoaded", function () {
    const form = document.getElementById("Inicio de Sesion");

    form.addEventListener("submit", function (event) {
        event.preventDefault(); // Evita el envío por defecto del formulario

        const usuario = document.getElementById("name").value;
        const contraseña = document.getElementById("psw").value;

        // Validación: el nombre de usuario solo puede contener letras mayúsculas y minúsculas
        const usernamePattern = /^[a-zA-Z]+$/;

        if (!usernamePattern.test(usuario)) {
            Swal.fire({
                icon: 'error',
                title: 'Error',
                text: 'El nombre de usuario solo puede contener letras mayúsculas y minúsculas.',
            });
            return;
        }

        // Aquí puedes agregar la lógica para verificar si el usuario y la contraseña son correctos
        /*
        if (usuarioExiste(usuario, contraseña)) {
            // Redirigir a la página principal
            window.location.href = 'pagina_principal.html'; // Cambia esto por la URL de tu página principal
        } else {
            Swal.fire({
                icon: 'warning',
                title: 'Usuario o contraseña incorrectos',
                text: 'Si no tienes cuenta, por favor crea una.',
            });
        }
        */

        // Si la validación es correcta, muestra un mensaje de éxito
        Swal.fire({
            title: 'Éxito!',
            text: 'Inicio de Sesión Completado.',
            icon: 'success',
            confirmButtonText: 'Aceptar'
        });

        setTimeout(() => {
            window.location.href = '/home';
        }, 2000); // Cambia esto por la URL de tu página principal
    });
});
function calcularIMC() {
    var peso = parseFloat(document.getElementById('peso').value);
    var altura = parseFloat(document.getElementById('altura').value);

    if (isNaN(peso) || isNaN(altura) || peso <= 0 || altura <= 0) {
        document.getElementById('resultado').textContent = "Por favor, ingresa valores válidos para el peso y la altura.";
        return;
    }

    var imc = peso / (altura * altura);
    var resultadoTexto = "Tu IMC es: " + imc.toFixed(2) + ". ";

    if (imc < 18.5) {
        resultadoTexto += "Tienes bajo peso.";
    } else if (imc >= 18.5 && imc < 24.9) {
        resultadoTexto += "Tienes un peso saludable.";
    } else if (imc >= 25 && imc < 29.9) {
        resultadoTexto += "Tienes sobrepeso.";
    } else {
        resultadoTexto += "Tienes obesidad.";
    }


    document.getElementById('resultado').textContent = resultadoTexto;
}


// Función para mostrar el tipo de cuerpo seleccionado
function mostrarTipo(tipo) {
    // Oculta todos los textos añadiendo la clase hidden
    document.getElementById("texto-ecto").classList.add("hidden");
    document.getElementById("texto-meso").classList.add("hidden");
    document.getElementById("texto-endo").classList.add("hidden");

    // Elimina la clase visible de todos los textos
    document.getElementById("texto-ecto").classList.remove("visible");
    document.getElementById("texto-meso").classList.remove("visible");
    document.getElementById("texto-endo").classList.remove("visible");

    // Muestra el texto correspondiente al tipo seleccionado
    const selectedText = document.getElementById(`texto-${tipo}`);
    selectedText.classList.remove("hidden"); // Muestra el elemento
    setTimeout(() => {
        selectedText.classList.add("visible"); 
    }, 10); 
}
