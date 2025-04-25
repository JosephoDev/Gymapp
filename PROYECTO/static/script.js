document.addEventListener("DOMContentLoaded", function() {
    const form = document.getElementById("Inicio de Sesion");

    form.addEventListener("submit", function(event) {
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